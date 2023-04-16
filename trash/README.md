# github-autoinvite-to-organisation

A webservice that asks github to send member invitation to your email.

## Personal access tokens (classic)

1. Go to https://github.com/settings/tokens
2. **GITHUB_ACCESS_TOKEN** must include admin:org scope. 
3. click **Generate new token**

## Setup

create `.env` file

```
GITHUB_TOKEN=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
GITHUB_ORG_NAME=publicdomain-nocopyright
```
## Run

`python app.py`

http://127.0.0.1:5000/



### Disallow member to rejoin.
1. Kick the member out of the organisation.
2. Go to organisation's settings -> moderation -> blocked users
3. Add member you want to disallow to rejoin.

![E-9wa98HOD5y22ruPXJxIOYclk4hjxasw7EqRyVBsM](https://user-images.githubusercontent.com/21064622/231753938-db25b822-442d-477a-8396-f3b2544f14e5.png)
![kLb7vnjf0g33sqLMw_TZsCwz6w99lreS1lDpDVHztm](https://user-images.githubusercontent.com/21064622/231753994-40720259-ce61-4d7e-b7f0-e9f3d48c3a6d.png)
![qGkDaO40kSG5POg13l8S839t1sloyhxA8I68tkR1mP](https://user-images.githubusercontent.com/21064622/231754024-f99b36f4-989b-4527-92e2-1236b17b2ae5.png)

### Limited hosting

https://render.com/docs/free

> Web Services on the free instance type are automatically spun down after 15 minutes of inactivity. 
> When a new request for a free service comes in, Render spins it up again so it can process the request.
