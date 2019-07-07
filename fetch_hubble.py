import os
import pathlib
import requests
import argparse
pathlib.Path('images').mkdir(exist_ok=True)


def get_hublpics(pic_id):

    habl_url = 'http://hubblesite.org/api/v3/image/{}'.format(str(pic_id))
    response = requests.get(habl_url)
    response.raise_for_status()
    response_unpacked = response.json()
    last_item_of_list = -1
    last_pic_kinda_url = response_unpacked['image_files'][last_item_of_list]['file_url']
    schema = 'https:'
    last_pic_url = schema + last_pic_kinda_url
    splited_l_p_url = last_pic_url.replace('.', ' ').split()
    extension = splited_l_p_url[last_item_of_list]
    filename = str(pic_id) + '.' + extension
    habls_pic_response = requests.get(last_pick_url, verify=False)
    with open(os.path.join('images',filename), 'wb') as file:
        file.write(habls_pic_response.content)


def main():
    parser = argparse.ArgumentParser(
      description='Choose your favorite Hubble collection: holiday_cards, wallpaper, spacecraft, news, printshop, stsci_gallery'
    )
    parser.add_argument('collection', help='Type collection name here', default = 'spacecraft')
    args = parser.parse_args()
    collection_name = args.collection
    coll_url = 'http://hubblesite.org/api/v3/images?page=all&collection_name={}'.format(collection_name)
    response = requests.get(coll_url)
    response.raise_for_status()
    response_unpacked = response.json()
    for i in response_unpacked:
        id = i['id']
        get_hublpics(id)


if __name__ == '__main__':
    main()
