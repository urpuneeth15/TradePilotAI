from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import requests

from app.config.settings import settings
from app.auth.token_manager import token_manager

router = APIRouter(tags=["Authentication"])


@router.get("/login")
def login():

    url = (
        "https://api.upstox.com/v2/login/authorization/dialog"
        f"?response_type=code"
        f"&client_id={settings.UPSTOX_CLIENT_ID}"
        f"&redirect_uri={settings.UPSTOX_REDIRECT_URI}"
    )

    return RedirectResponse(url)


@router.get("/callback")
def callback(code: str):

    url = "https://api.upstox.com/v2/login/authorization/token"

    payload = {

        "code": code,

        "client_id": settings.UPSTOX_CLIENT_ID,

        "client_secret": settings.UPSTOX_CLIENT_SECRET,

        "redirect_uri": settings.UPSTOX_REDIRECT_URI,

        "grant_type": "authorization_code"

    }

    headers = {

        "accept": "application/json",

        "Content-Type": "application/x-www-form-urlencoded"

    }

    response = requests.post(
        url,
        data=payload,
        headers=headers
    )

    data = response.json()

    access_token = data.get("access_token")

    if access_token:

        token_manager.save(access_token)

        return {
            "status": "success",
            "message": "Token saved successfully."
        }

    return data