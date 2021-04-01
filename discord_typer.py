import requests,time,os
headers = {
        'Authorization': '',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
def checkToken(_token:str) -> bool:
    headers['Authorization'] = _token
    request = requests.post('https://discord.com/api/v8/users/@me/channels', headers=headers)
    if request.status_code != 401:
        return True
    return False

def get_channel(id:str)->str:
    request = requests.post(f'https://discord.com/api/v8/users/@me/channels', json={'recipients': [ id ]}, headers=headers)
    if request.status_code == 200:
        print("user exists!")
        return request.json() ['id']
    else:
        print('invalid user id')
        exit(0)
        return ''

def send(_token:str,_channel_id:str):
    headers ['Authorization'] = _token
    rq = requests.post(f'https://discord.com/api/v8/channels/{_channel_id}/typing',headers=headers)
    return rq.status_code

if __name__ == "__main__":
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    token = input('token ~> ')
    if checkToken(token):
        print('valid token!')
    else:
        print('invalid token!')
        exit(0)
    channel_id = ''
    o=input("""Options
[1] Server Channel
[2] Direct Message
""")
    if o == '1':
        channel_id = input('channel id ~> ')
    elif o == '2':
        channel_id = get_channel(input('user id ~> '))
    else:
        print(f'invalid option: {o}')
        exit(0)


    try:
        while True:
            a = send(token,channel_id)
            if a == 204:
                print('> HTTP 204 Succes!')
            else:
                print(f'# HTTP {a} ERR')
            time.sleep(5)
    except KeyboardInterrupt:
        print('stopped')
    pass