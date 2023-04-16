from flask import Flask, request, redirect, session, render_template
import os
import requests

app = Flask(__name__)
print(app.secret_key = os.getenv('FLASK_SECRET_KEY'))
print(github_client_id = os.getenv('GITHUB_CLIENT_ID'))
print(github_client_secret = os.getenv('GITHUB_CLIENT_SECRET'))
print(github_org_name = os.getenv('GITHUB_ORG_NAME'))
print(github_redirect_uri = os.getenv('GITHUB_REDIRECT_URI'))

@app.route('/')
def index():
    if 'email' in session:
        return redirect('/invite')
    else:
        return redirect('/login')
        
@app.route('/login')
def login():
    params = {
        'client_id': github_client_id,
        'redirect_uri': github_redirect_uri,
        'scope': 'user:email',
    }
    return redirect(f'https://github.com/login/oauth/authorize?{"&".join([f"{k}={v}" for k,v in params.items()])}')

@app.route('/login/callback')
def login_callback():
    code = request.args.get('code')
    params = {
        'client_id': github_client_id,
        'client_secret': github_client_secret,
        'code': code,
        'redirect_uri': github_redirect_uri,
    }
    r = requests.post('https://github.com/login/oauth/access_token', data=params, headers={'Accept': 'application/json'})
    access_token = r.json()['access_token']
    session['access_token'] = access_token

    r = requests.get('https://api.github.com/user/emails', headers={'Authorization': f'token {access_token}', 'Accept': 'application/vnd.github.v3+json'})
    emails = r.json()
    session['email'] = [email['email'] for email in emails if email['primary']][0]

    return redirect('/invite')

@app.route('/invite')
def invite():
    email = session.get('email')
    if not email:
        return redirect('/login')

    token = os.getenv('GITHUB_TOKEN')
    org_name = os.getenv('GITHUB_ORG_NAME')
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    payload = {
        'email': email,
        'role': 'direct_member'
    }
    
    url = f'https://api.github.com/orgs/{org_name}/invitations'
    
    r = requests.post(url, json=payload, headers=headers)
    
    if r.status_code == 201:
       invitation_link = f'https://github.com/orgs/{org_name}/invitation'
       return redirect(invitation_link)
    if r.status_code == 422 and "already a part of this org" in r.json()["errors"][0]["message"]:
        return render_template('email_already_part_of_org.html', github_org_name=org_name)
    else:
        return f'Error sending invitation. Status code: {r.status_code}. Response content: {r.content}'

# host='0.0.0.0' is probably required by render.com webservice provider.
# Maybe allows to run on all addresses at once.
# Apr 16 03:29:49 PM   * Running on all addresses (0.0.0.0)
# Apr 16 03:29:49 PM   * Running on http://127.0.0.1:5000
# Apr 16 03:29:49 PM   * Running on http://10.217.57.115:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
