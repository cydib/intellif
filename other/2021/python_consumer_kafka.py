#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : recurrent_timeout.py
# @Date    : 2021-03-11 11:25:27
# @Author  : tmp
# @Link    : https://github.com/seryte
# @Project : tmp

import os
import time
from kafka import KafkaConsumer
from gitlab.sz.xxx.com.x.abc.pb import eer_pb2 as pb
from google.protobuf.json_format import MessageToDict
topic = 'test_tpoic'
host = '192.20.26.215:9092'
offset = 'latest'
kafka_username = 'admin'
kafka_password = 'mkdNMWrfrdfghghexnxyRcs'

event_consume = KafkaConsumer(topic, group_id="fuck", bootstrap_servers=host, auto_offset_reset=offset,
                                     security_protocol='SASL_PLAINTEXT',
                                     sasl_mechanism='PLAIN',
                                     sasl_plain_username=kafka_username,
                                     sasl_plain_password=kafka_password,
                                     api_version=(0, 10)
                                     )
from time import strftime, localtime
obj = pb.ObjectInfo()
print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

start_time = time.time()
count = 0
msg_count = 0
while True:
    count += 1
    print(f"consumer {count} times")
    if time.time() - start_time > 5 * 60:
        print('超时未消费到足够符合要求的msg')
        break
    msg = event_consume.poll(1000, 1)
    # print('connect')
    # print(msg)
    # msg_dict = Kafka.deserialize(msg, obj=obj, _poll=True)
    # print(msg_dict)
    if msg:
        msg_count+=1
        obj.ParseFromString(list(msg.values())[0][0].value)
        dmsg = MessageToDict(obj, including_default_value_fields=True)
        # for key, value in msg.items():
        #     msg_count+=1
        #     for record in value[:10]:
        #         obj.ParseFromString(record.value)
        #         dmsg = MessageToDict(obj, including_default_value_fields=True)
        #         print(dmsg, count)
        print(list(msg.values())[0][0].offset, dmsg)

print(strftime("%Y-%m-%d %H:%M:%S", localtime()), f'共消费{topic} {msg_count}条')
