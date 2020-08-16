import twitter, os

def connect_api():
    #Get environment vars for access tokens (so input your own credentials as an env variable)
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_SECRET")

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_secret)

    try:
        api.VerifyCredentials()
        print("Login to API successful")
    except Exception as exc:
        raise exc

    return api
