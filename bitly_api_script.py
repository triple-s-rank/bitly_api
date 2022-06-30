import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_url(link, headers):
    data = {'long_url': f'{link}'}
    response = requests.post(
        url='https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=data
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(link, headers):
    response = requests.get(
        url=f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary',
        headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(link, headers):
    response = requests.get(
        url=f'https://api-ssl.bitly.com/v4/bitlinks/{link}',
        headers=headers
    )
    return response.ok


def main():
    load_dotenv()

    access_token = os.getenv("BITLY_ACCESS_TOKEN")
    headers = {'Authorization': f'Bearer {access_token}'}
    parser = argparse.ArgumentParser(
        description="Transform url to bitly link and counts clicks on it. Enter url in format: http://example.com "
    )
    parser.add_argument(
        "url",
        type=str,
        help="use 'python main.py {url}'"
    )
    args = parser.parse_args()
    url = args.url
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        full_url = f'http://{parsed_url.geturl()}'
    else:
        full_url = parsed_url.geturl()
    url_without_protocol = f'{parsed_url.netloc}{parsed_url.path}'
    try:
        if is_bitlink(url_without_protocol, headers):
            print(
                'По вашей ссылке прошли',
                count_clicks(url_without_protocol, headers),
                'раз(а).'
            )
        else:
            bitlink = shorten_url(full_url, headers)
            print('Битлинк', bitlink)
    except requests.HTTPError:
        print('Вы ввели неверную ссылку.')


if __name__ == '__main__':
    main()
