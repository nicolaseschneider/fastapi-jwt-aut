from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')

@app.get("/")
async def index(token: str = Depends(oauth2_scheme)):
    return {"the_token": token}

@app.post('/auth')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


