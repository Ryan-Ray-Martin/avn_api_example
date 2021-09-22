import http.client

import config

if __name__ == '__main__':

    conn = http.client.HTTPSConnection("api.aiven.io")

    # avn authorization header for API
    headers = {"Authorization": "Bearer " + config.AVN_API_KEY}

    # GET ACCOUNT DETAILS
    # use account_id to perform other tasks in API
    conn.request("GET", "/v1/account", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("get account details", data.decode("utf-8"))

    # GET AUTHENTICATION INFO
    # this will show whether or not authentication method is enabled with SAML

    # request method
    conn.request("GET", "/v1/account/" + config.ACCOUNT_ID + "/authentication", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("get auth info", data.decode("utf-8"))