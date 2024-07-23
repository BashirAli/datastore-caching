from core.caching import CachingManager
from utils.helpers import load_json_file
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
dummy_data_dir = "data/uk_dummy_addresses.json"


def main():
    data = load_json_file(dummy_data_dir)
    if data:
        caching_manager = CachingManager()
        caching_manager.process(data)


if __name__ == '__main__':
    main()
