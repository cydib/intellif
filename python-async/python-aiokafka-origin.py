from aiokafka import AIOKafkaConsumer
import asyncio
import time
from gitlab.sz.xx as xx_pb
from gitlab.sz.xx import _pb2 as pb
from gitlab.sz.xx.pb2 import ObjectInfo
from google.protobuf.json_format import MessageToDict

obj = ObjectInfo()


async def consume():
    consumer = AIOKafkaConsumer(
        'topic1', 'topic2',
        bootstrap_servers='1xx.2x.2x.1xx:9092',
        group_id=time.strftime("%Y-%m%d-%H%M%S-%s", time.localtime())[0],
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        sasl_plain_username='admin',
        sasl_plain_password='$%^%^&%^&*',
        auto_offset_reset='earliest'
    )
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            obj.ParseFromString(msg.value)
            decode_msg = MessageToDict(obj, including_default_value_fields=True)
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  decode_msg, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
