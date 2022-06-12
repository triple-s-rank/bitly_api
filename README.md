# Bitly_api_script
Small script for shortening urls and counting clicks on shortned links using bitly API.
## Setup
Python should be already installed.

#### To clone repository: 

``` git clone https://github.com/triple-s-rank/bitly_api_script.git ```

#### To install dependencies

``` pip install -r requirements.txt ```

#### To get API token

To use script you should create account on [bitly](https://app.bitly.com/) and get your personal api access token.

#### Setup environment

Create .env file in script directory and place your token there:

``` BITLY_ACCESS_TOKEN='{YOUR TOKEN}' ```

## Running script

Run script with command

``` python bitly_api_script.py {url to shorten or clicks to count} ```

After passing url script will parse it and convert it to shorten link or count clicks if it is already shorten.

## Project goals

Project is created in educational purposes while learning working with Web API`s
