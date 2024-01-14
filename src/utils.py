import requests
import os


def get_input(url):
    session_cookie = os.getenv("SESSION_COOKIE")
    response = requests.get(url, headers={"Cookie": f"session={session_cookie}"})
    response.raise_for_status()

    return response.text
