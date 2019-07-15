import os
import pathlib
import requests



def main():

    pathlib.Path('images').mkdir(exist_ok=True)
    spx_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(spx_url)
    response.raise_for_status()
    response_unpacked = response.json()
    links = response_unpacked['links']['flickr_images']
    for index, link in enumerate(links, 1):
        filename = 'spaceX%s.jpg'%(index)
        flickr_response = requests.get(link)
        with open(os.path.join('images',filename), 'wb') as file:
            file.write(flickr_response.content)


if __name__ == '__main__':
    main()
