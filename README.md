# GCP Datastore Caching 

This repository displays the caching capabilities of GCP Datastore. It checks if dummy address data is in the cache, and if not, it writes to the cache 

Key design is based on best practices, including selection of unique identifiers in the dummy data, string cleaning then finally subsequent hashing

## Getting Started

1. Create a `.env` file and fill in the following variables

```
GCP_PROJECT_ID=<YOUR_PROJECT_ID>>
DATASTORE_NAMESPACE=<YOUR_DATASTORE_NAMESPACE>>
DATASTORE_KIND=<YOUR_DATASTORE_KIND>
```

2. Install poetry (if required) and the poetry files in your chosen virtual environment 

```
pip install poetry 
poetry install
```

3. run `main()`






*Developed in Python 3.12.0*