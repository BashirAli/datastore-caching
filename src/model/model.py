from enum import Enum


class CACHE_FLAG(Enum):
    IN_CACHE: str = "DATA_ALREADY_IN_CACHE"
    NOT_IN_CACHE: str = "DATA_WRITTEN_TO_CACHE operation"
