import random

from pyArango.connection import *

from config import ArangoConfig


class PyArangoDBTest:
    def __init__(self):
        self.conn = Connection(arangoURL=ArangoConfig.CONNECTION_URL, username=ArangoConfig.USERNAME,
                               password=ArangoConfig.PASSWORD)
        self.db = self.conn[ArangoConfig.DATABASE]

    def get_data(self, limit=None):
        collection_name = "wallets"
        doc_format = "{\"key\": doc.address, \"value\": FLOOR(RAND()*1001)}"

        query = "FOR doc IN {col} LIMIT {limit} RETURN {doc_format}".format(
            col=collection_name,
            limit=limit,
            doc_format=doc_format
        )

        result = self.db.AQLQuery(query, rawResults=True,count=True, batchSize=limit)
        # print(result.query)
        return result.response['result']


