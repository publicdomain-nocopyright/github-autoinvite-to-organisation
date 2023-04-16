#pip install jinja2==2.11.3
# pip install markupsafe==2.0.1
# pip install itsdangerous==2.0.1
#pip install werkzeug==2.0.3

from flask import Flask, request, render_template
from flask import redirect

import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invite', methods=['POST'])
def invite():
    email = request.form['email']
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
    else:
        return f'Error sending invitation. Status code: {r.status_code}. Response content: {r.content}'
        
        
        
        
# host='0.0.0.0' can be removed, only required to run on  https://dashboard.render.com/
# render.com runs in circles of (in-progress) and never detects that app finally started. Unless this is present.
# https://community.render.com/t/build-stuck-in-in-progress-state-forever/1850
if __name__ == '__main__':
    app.run(host='0.0.0.0')
