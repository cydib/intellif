import asyncio
import base64
import functools
import json
import os
import time
import aiohttp
from concurrent.futures.thread import ThreadPoolExecutor

from util.timer import timer


@timer
def get_img(img_path):
    return [os.path.join(root, pic) for root, dirs, files in os.walk(img_path) for pic in files if
            pic.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]


def img_to_base64(img):
    with open(img, 'rb') as f:
        bs64 = base64.b64encode(f.read()).decode('utf-8')
    return img, bs64


async def run(host, img_path):
    lists = get_img(img_path)
    pic_fe = multi_thread_process(img_to_base64, lists)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for all in pic_fe:
            tasks.append(req(session, host, all[0], all[1]))
        return await asyncio.gather(*tasks)


async def req(session, host, pic, bs64):
    url = f'http://{host}/engine/image-process/face_25000/v1/batch_detect'
    body = {
        "requests": [
            {
                "image": {
                    "data": bs64
                }
            }
        ],
        "detect_mode": "Default",
        "face_type": "Large"
    }
    no_face = 0
    async with session.post(url, data=json.dumps(body)) as response:
        resp = await response.json()
        ret = None
        try:
            ret = resp.get('results')[0]['status']
        except Exception as e:
            print(pic, resp, e)
        if ret != 'OK':
            print(pic, ret)
            no_face += 1
    return no_face


@timer
def multi_thread_process(func, lists):
    with ThreadPoolExecutor() as ex:
        ret = list(ex.map(func, lists))
    return ret


@timer
def main(host, path):
    no_face = asyncio.run(run(host, path))
    print(f'no_face: {sum(no_face)}')


if __name__ == '__main__':
    main('172.20.26.225:30080', '/Users/keze/mount/useful_pic/')
