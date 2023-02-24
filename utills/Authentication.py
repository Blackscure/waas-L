
import base64
from email import header
import requests
import json
from requests.auth import HTTPBasicAuth
from django.conf import settings


def get_access_token():
    sasapay_password = "OlW1H0LgP75iQ1zywri1ByVicf9W1gTWborZZb1ntmaRyDgaGFwcDGrhRWHEAyiwJ4BDmnf0AQOmVkYwzBCnc8NLuhBDN1xbluD8jYKrxqSkbBELMShtn9UXrjo6N1Q1"
    sasapay_username="sCCNr3ZsqfKEjYTPzBZ4LtzjxNEG09X9tvGnFBUE"
    url = 'https://api.sasapay.me/api/v1/auth/token/?grant_type=client_credentials'
    base64_string = base64.b64encode(f"{sasapay_username}:{sasapay_password}".encode()).decode("ascii")
    payload = {}
    headers = {
                    'Authorization': f'Basic {base64_string}' 
                    }
    try:
        res = requests.get(url, headers=headers, data=payload)
        response = json.loads(res.text)
        access_token = response['access_token']
        return access_token
    except Exception as error:
        print('TOKEN ERROR:', str(error))
        return False