0. Setup **Github OAuth App** and **Personal access tokens (classic)**  
   1. create Github OAuth App: https://github.com/settings/developers
   2. create Personal access token (classic): https://github.com/settings/tokens
1. Set evnironment variables in your webservice's environment
2. run `python app.py`
3. visit your app url

To run app locally:

0. Setup **Github OAuth App** and **Personal access tokens (classic)**  
   1. create Github OAuth App: https://github.com/settings/developers
   2. create Personal access token (classic): https://github.com/settings/tokens
0. Set evnironment variables    
1. set `GITHUB_REDIRECT_URI` in both: **web service** and **Github OAuth App** to:  
   * `GITHUB_REDIRECT_URI=http://localhost:5000/login/callback`
2. run `python app.py`
3. visit http://localhost:5000
## Set these variables in your webservice's environment
Do not use `.env` unless your repository/project is completely private.
```
                                           # secrect key, should be random made-up by you.
FLASK_SECRET_KEY=hhjkyui                   
                                           # Github OAuth App Client ID
GITHUB_CLIENT_ID=a214e99ec9e3bf2ed040      
                                           # Github OAuth App CLIENT SECRET
GITHUB_CLIENT_SECRET=81cbad67bf8dee358dfd943c4a13c4758f317c5e 
                                           # Github OAuth App Redirect URL
GITHUB_REDIRECT_URI=https://auto-invitation-test.onrender.com/login/callback 
                                           # Your organisation name as in url https://github.com/publicdomain-nocopyright
GITHUB_ORG_NAME=publicdomain-nocopyright
                                           # GitHub Token of an admin of organisation.
                                           # Personal access token must include admin:org scope. Which will allow to create invites to organisation.
GITHUB_TOKEN=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 
```

## Register a new OAuth application

This application account will be used to authenticate GitHub users.  
[To gain email through github auth and use it to invite user.]  

https://github.com/settings/applications/new

**Application name:** Anything you like  
**Homepage URL:** Anything you like  
**Application description:** Anything you like  
**Authorization callback URL:**  
  * For local testing: `http://localhost:5000/login/callback`  
  * For use: `https://auto-invitation-test.onrender.com/login/callback`  

Enable Device Flow: not needed.  

Usage Steps:  
1. Copy Client ID
2. Copy Authorization callback URL
3. Generate and copy a Client secret




## Personal access tokens (classic)

You must be an admin of a organisation.
This will be used to request invitation for user.

1. Go to https://github.com/settings/tokens
2. **GITHUB_ACCESS_TOKEN** must include admin:org scope. 
3. click **Generate new token**


