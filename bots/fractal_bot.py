import os, random
from time import sleep
from authentication import connect_api as con_api
from julia import Julia
from julia import save_julia

def tweet():
    api = con_api()
    i = 0
    while True:
        cx = -random.uniform(0.001,0.2)
        cy = random.uniform(0.63,0.75)
        file_path = save_julia(cx, cy)
        print("Built fractal")
        message = "Julia fractal with c = "+str(round(cx, ndigits = 2))+" + "+str(round(cy, ndigits = 2))+"i"
        try:
            api.update_with_media(file_path, status=message)
            print("Tweet successful!")
            os.remove(file_path)
        except Exception as exc:
            print("Tweet didn't work :(")
            raise exc
        if i%2==0:
            sleep(50400)
            i+=1
        else:
            sleep(36000)
            i-=1

tweet()
