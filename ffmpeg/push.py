import subprocess as sp
import json
from urllib.request import urlopen

ROOM_URL = 'http://exert-livego-server:8090/control/get'
RTMP_URL = 'rtmp://exert-livego-server:1935/live'

def get_channelkey(name='movie'):
    '''
    获取
    '''

    response = urlopen(f'{ROOM_URL}?room={name}')
    content = response.read()
    data = json.loads(content)
    return data['data']


def push_vedio(rtmp_channelkey):
    '''
    '''

    push_command = [
        'ffmpeg',
        '-re',
        '-i', 'demo.flv',
        '-c', 'copy',
        '-f', 'flv',
        f'{RTMP_URL}/{rtmp_channelkey}',
    ]
    p = sp.Popen(push_command, stdin=sp.PIPE)

key = get_channelkey()
push_vedio(key)