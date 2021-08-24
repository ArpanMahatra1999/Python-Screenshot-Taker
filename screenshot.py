import requests

def get_screenshot(image_name, website_url):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    path = image_name+'.jpg'
    response = requests.get(BASE + website_url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
    return True

get_screenshot('demo', 'https://www.youtube.com/')