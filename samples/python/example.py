import requests
import json
from modulr_hmac.api_auth import Signature

API_KEY = ""
API_SECRET = ""
API_BASE= "https://api-sandbox.modulrfinance.com/api-sandbox"

def _get_headers():
    signature = Signature(API_KEY, API_SECRET)
    result = signature.calculate()
    return result.get_http_headers()

def get_customers():
    url = f"{API_BASE}/customers"
    response = requests.get(url, headers=_get_headers())
    return response

def get_accounts(customer):
    url = f"{API_BASE}/customers/{customer}/accounts"
    response = requests.get(url, headers=_get_headers())
    return response

def get_account(account):
    url = f"{API_BASE}/accounts/{account}"
    response = requests.get(url, headers=_get_headers())
    return response

def create_account(customer, currency, reference, product_code):
    url = f"{API_BASE}/customers/{customer}/accounts"
    payload = {"currency": currency, "externalReference": reference, "productCode": product_code}
    response = requests.post(url, json = payload, headers=_get_headers())
    return response

def create_payment():
    url = f"{API_BASE}/credit"
    payload = {"payerDetail":{"identifier":{"accountNumber":"70469265","sortCode":"000000","type":"SCAN"},"name":"Payee"},"accountId":"A120MC23","amount":1000,"type":"PI_BACS","description":"Polish Consulting SA"}
    response = requests.post(url, json = payload, headers=_get_headers())
    return response

def get_account_transactions(account):
    url = f"{API_BASE}/accounts/{account}/transactions?page=0&size=20"
    response = requests.get(url, headers=_get_headers())
    return response

if __name__ == "__main__":
    #customers = get_customers()
    #print(json.dumps(customers.json(), indent=2))

    #account = create_account("C120G9MM", "GBP", "Python 4 life", "O1200001")
    #print(json.dumps(account.json(), indent=2))

    #accounts = get_accounts("C120G9MM")
    #print(json.dumps(accounts.json(), indent=2))

    #payment = create_payment()

    #transactions = get_account_transactions("A120MC23")
    #print(json.dumps(transactions.json(), indent=2))

    account = get_account("A120MC23")
    print(json.dumps(account.json(), indent=2))
