import requests
gif_list = ["fail", "people", "lucky"]
BASE_URL = "https://api.giphy.com/v1/stickers/random"
for gif in gif_list:
    params = dict(
        api_key="dc6zaTOxFJmzC",
        tag="lucky",
        rating="g",
        limit=1,
        fmt='json'
        )
    response = requests.get(BASE_URL, params=params)
    print(response.ok)
    gif_url = response.json()['data']["images"]['fixed_height_small']['url']
    resp_gif = requests.get(gif_url)
    with open(gif+".gif", "wb") as f:
        f.write(resp_gif.content)
