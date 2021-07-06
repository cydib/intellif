#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : python_aiokafka.py
# @Date    : 2021-03-11 11:25:27
# @Author  : author
# @Link    : hello-kafka
# @Project : kafka


import json
import os
import time
import uuid
import asyncio
from aiokafka import AIOKafkaConsumer

from kafka import KafkaConsumer
from xx import x1 as pb
from xx import x2 as new_pb
from google.protobuf.json_format import MessageToDict
from time import strftime, localtime
from concurrent.futures.process import ProcessPoolExecutor
from itertools import repeat
from functools import partial

obj = new_pb.oupilaoge()
group_id = time.strftime("%Y-%m%d-%H%M%S-%s", time.localtime()),


async def consume(host, kafka_topic, kafka_passwd, kafka_user='admin', kafka_offset='latest'):
    consumer = AIOKafkaConsumer(
        kafka_topic,
        bootstrap_servers=host,
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        group_id=group_id[0],
        sasl_plain_username=kafka_user,
        sasl_plain_password=kafka_passwd,
        auto_offset_reset=kafka_offset
    )
    await consumer.start()
    try:
        async for msg in consumer:
            obj.ParseFromString(msg.value)
            decode_msg = MessageToDict(obj, including_default_value_fields=True)
            # print("consumed: ", msg.topic, group_id, msg.partition, msg.offset,
            #       decode_msg, msg.timestamp)
            await msg_to_file(kafka_topic, decode_msg)
    finally:
        await consumer.stop()


async def msg_to_file(kafka_topic, msg):
    with open(f'{kafka_topic}_{group_id[0]}.txt', 'a') as f:
        f.write(json.dumps(msg) + '\n')


def run(host, kafka_topic, kafka_user, kafka_passwd, kafka_offset):
    asyncio.run(consume(host, kafka_topic, kafka_passwd, kafka_user=kafka_user, kafka_offset=kafka_offset))


def main(host, topic_list, kafka_user, kafka_passwd, kafka_offset):
    with ProcessPoolExecutor() as executor:
        executor.map(run, repeat(host), topic_list, repeat(kafka_user), repeat(kafka_passwd), repeat(kafka_offset))


if __name__ == '__main__':
    env = {
        'host': '172.10.1.1:9092',
        'kafka_user': 'admin',
        'kafka_passwd': '$%^&^&%^&%',
        'kafka_offset': 'earliest',
        'topic_list': [
            'topic1',
            'topic2'
        ]
    }
    main(**env)
