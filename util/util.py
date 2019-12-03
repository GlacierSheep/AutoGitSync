# -*- coding: utf-8 -*-

"""
@author: Glacier

@contact: me@xuluhang.cn

@Created on: 2019/12/3 14:51
"""
import json

import requests


def wxpush(title, content, option):
    if option:
        baychat = 'https://hook.bearychat.com/=bwHAy/incoming/4babc554d32edcc1f16742ff8005e975'
        request_data = {
            "text": title,
            "attachments": [
                {
                    "title": title,
                    "text": content,
                    "color": "#ffa500",
                    "images": [{"url": "http://img3.douban.com/icon/ul15067564-30.jpg"}]
                }
            ]
        }

        header = {'Content-Type': 'application/json'}
        req = requests.post(url=baychat,
                            headers=header,
                            data=json.dumps(request_data).encode("utf-8"))
    else:
        print('fault')
