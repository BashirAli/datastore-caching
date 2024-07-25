import hashlib
import os
import time

from model.logging import logger
from model.model import CACHE_FLAG
from storage.datastore import Datastore


class CachingManager:
    def __init__(self):
        self.datastore_client = Datastore(project_id=os.getenv("GCP_PROJECT_ID"),
                                          namespace=os.getenv("DATASTORE_NAMESPACE"))
        self.datastore_kind = os.getenv("DATASTORE_KIND")

    def process(self, data: list):
        for i, data_dict in enumerate(data):
            start_time = time.perf_counter()
            uq_identifier = f"{data_dict["customer_id"]} {data_dict["postcode"]}"
            cache_key = self.build_cache_key_from_data(uq_identifier)

            cached_data = self.datastore_client.get_entity_with_key(self.datastore_kind, cache_key)
            cache_flag = CACHE_FLAG.IN_CACHE

            if not cached_data:
                self.datastore_client.insert_entity_with_key(self.datastore_kind, cache_key, data_dict)
                cache_flag = CACHE_FLAG.NOT_IN_CACHE

            end_time = time.perf_counter()
            logger.info(f"Execution time for {cache_flag.value}: {end_time - start_time:.4f} seconds")

    @staticmethod
    def build_cache_key_from_data(key: str) -> str:
        key = key.replace(" ", "")
        return f"{hashlib.md5(key.encode('utf-8')).hexdigest()}_{key}"
