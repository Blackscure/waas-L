from django.shortcuts import render
import requests
from rest_framework.views import APIView, Response
import json

from utills.Authentication import get_access_token

# Create your views here.
class ProcessPaymentApiView(APIView):
    def post(self, request):

        ProposedAccountNumber = ""
        CallbackUrl = "https://posthere.io/39b9-425e-85c5"
        url = "https://api.sasapay.me/api/v1/payments/request-payment/"


        access_token =get_access_token()

        print('------------------------------------------------------------TOKEN',access_token)

        payload = {
        "MerchantCode": "11120",
        "NetworkCode": "0",
        "PhoneNumber": "254723468573",
        "TransactionDesc": "Pay for groceries",
        "AccountReference": "0723468573",
        "Currency": "KES",
        "Amount": 1,
        "CallBackURL": CallbackUrl
    }


        headers = {
                'Authorization': f'Bearer {access_token}' 
                }

        response = requests.post(url, headers=headers,data=payload)
        sasapayresponse = json.loads(response.text)
        return Response({
                'status': True,
                'message':'Vehicle type added successful.',
                'data':sasapayresponse
            })

         

        print('----------------------------------------------->ENTITY ONBOARDING', response)


class EntityOnboardingAPIView(APIView):
    def post(self, request):
        url = "https://api.sasapay.me/api/v1/payments/process-payment/"

        access_token =get_access_token()

        payload = {
            "CheckoutRequestID": "81567459-081a-4f26-bbfc-ee9b1487ff77",
            "MerchantCode": "11120",
            "VerificationCode": "476700"
        }


        headers = {
                'Authorization': f'Bearer {access_token}' 
                }

        response = requests.post(url, headers=headers,data=payload)

        sasapayresponse = json.loads(response.text)
        return Response({
                'status': True,
                'message':'Vehicle type added successful.',
                'data':sasapayresponse
            })


        



       





