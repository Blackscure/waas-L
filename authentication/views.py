import base64
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class AutheticationAPIView(APIView):
    def get(self, request):
        client_id = "a6P1yWrxiF7ISzI6snRfZXRYMT4mufk0fsqplwF5"
        client_secret="jRjMoRYEZzyqXQI7TYMVfeNV0fB3lDUGXxFaaihhVWFgE172GSx6rVUEjsVj5tsQSgYtnBiWAao8CDytQW6IyX8V6OP8Z8QR5Ve3CAGD28s1cVUC2Rle4Ze1pEyUQScI"
        url = 'https://sandbox.sasapay.app/api/v1/waas/auth/token/?grant_type=client_credentials'
        base64_string = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode("ascii")
        headers = {
                    'Authorization': f'Basic {base64_string}' 
                    }
        payload = {}
        try:
            res = requests.get(url, headers=headers, data=payload)
            response = json.loads(res.text)
            return Response({
                'status': True,
                'message':'Success',
                'data':response
            })
            
        except Exception as error:
            print(str(error))

         