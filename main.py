import time
import requests

def main():
    print('init ...')
    num = 1
    while True:
        print('count: {}'.format(num))
        time.sleep(5)
        res = requests.get()
        print(res.text)
        num += 1
