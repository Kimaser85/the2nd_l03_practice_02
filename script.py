import requests
from pprint import pprint 

BASE_URL = "https://api.giphy.com/v1/stickers/random"
params = dict(
        api_key="dc6zaTOxFJmzC",
        tag="python",
        limit=1,
        rating="g",
        fmt='json'
        )
response = requests.get(BASE_URL, params=params)
print(response.ok)
pprint(response.json())#)['data'])#['id'])#['fixed_height_small'])
 #'_url'])
# gif_url = response.json()['data']['fixed_height_small_url']
# resp_gif = requests.get(gif_url)
# with open("test.gif", "wb") as f:
#     f.write(resp_gif.content)
