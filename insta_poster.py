import glob
from instabot import bot
import time
import argparse


def main():

    parser = argparse.ArgumentParser(
      description='Give me your IG account'
    )
    parser.add_argument('LOGIN', help='Your IG login')
    parser.add_argument('PASSWORD', help='Your IG password')
    args = parser.parse_args()
    bot = Bot()
    bot.login(username=args.LOGIN, password=args.PASSWORD)
    timeout = 10 * 60
    pics = glob.glob('images\\*')

    for pic in pics:
        bot.upload_photo(pic, caption='space')
        time.sleep(timeout)

if __name__ == '__main__':
    main()
