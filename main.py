import json
from random import *
import random

from pyArango import *
from utils.database import PyArangoDBTest
import redis
from redis.client import *
import string

r = redis.Redis(host='localhost', port=6379, password="mypassword")
r.flushdb()

ar = PyArangoDBTest()


def address_gen(limit):
    data = []
    for i in range(0, limit):
        prefix = '0x' + str(i)
        address = ''.join((random.choice(string.ascii_letters + string.digits)) for j in range(42 - len(prefix)))
        address = '0x' + str(i) + address
        value = randint(0, 100)

        data.append({"key": address, "value": value})
    return data


def caching(data):
    r.flushdb()
    data_sz = len(data)
    print(data_sz)
    for d in data:
        r.setex(d["key"], 3600, d["value"])
    total_memo_in_byte = r.memory_stats()['total.allocated']
    total_memo_in_mb = total_memo_in_byte / (1024 * 1024)
    return data_sz, total_memo_in_mb


if __name__ == "__main__":
    # random generate address
    r.flushdb()
    # for i in range(2, 9):
    #     limit = 10 ** i
    #     data = address_gen(limit)
    #     # print(data)
    #     data_sz, mem = caching(data)
    #     print("{} {}".format(data_sz, mem))
    #     r.flushdb()

    # address from arangodb
    for i in range(2, 9):
        limit = 10 ** i
        data = ar.get_data(limit=limit)
        # print(data)
        data_sz, mem = caching(data)
        print("{} {}".format(data_sz, mem))
        r.flushdb()

