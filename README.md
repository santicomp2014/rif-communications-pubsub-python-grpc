# Rif Comms Pubsub Test with Python

This repo is for testing a GRPC connection between a python client and RIF comms node.

### 1. Create virtual environment
```shell script
virtualenv -p <PATH_TO_PYTHON3> venv
```

your python 3 path can be found by executing `which python3`. 

### 2. Activate virtual environment
```shell script
source venv/bin/activate
```

### 3. Install dependencies
```shell script
pip install -r requirements.txt
```

### 4. Execute tests
for example, for the `client2.py` test, execute:
```shell script
python3 client-2.py
```
