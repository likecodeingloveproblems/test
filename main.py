import time
import requests

# this is only for test purpose
# v0.0.0 
def main():
    print('init ...')
    num = 1
    while True:
        print('count: {}'.format(num))
        time.sleep(5)
        res = requests.get()
        print(res.text)
        num += 1
