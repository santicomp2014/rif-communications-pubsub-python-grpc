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

### 4. Execute test scripts
#### 4.1 Requirements
The virtual environment [must be activated](#2-Activate-virtual-environment) for these to work.

#### 4.2 Scripts
| script           | execution                                                                   | description                                                                                                                                                                                |
| ---------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client-1.py`    | `python3 client-1.py`                                                       | unclear.                                                                                                                                                                                   |
| `client-2.py`    | `python3 client-2.py`                                                       | unclear.                                                                                                                                                                                   |
| `lumino.py`      | `python3 lumino.py <RIF_COMMS_NODE_ADDRESS> <RSK_ADDRESS> <TOPIC_ID>`       | connects to RIF Comms node, registers RSK address for a peer ID, creates a topic with the address and awaits for responses from it. when halting, sends a message to topic and fails.*     |
| `lumino-send.py` | `python3 lumino-send.py <RIF_COMMS_NODE_ADDRESS> <TOPIC_ID_1> <TOPIC_ID_2>` | connects to RIF Comms node, subscribes to 2 topics, sends messages to them based on user input, then fails.                                                                                |
| `receiver.py`    | `python3 receiver.py <RIF_COMMS_NODE_ADDRESS> <RSK_ADDRESS>`                | connects to RIF Comms node, registers RSK address for a peer ID, creates a topic with the address and awaits for responses from it. when halting, sends a message to topic and closes it.* |
| `sender.py`      | `python3 sender.py <RIF_COMMS_NODE_ADDRESS> <TOPIC_ID>`                     | connects to RIF Comms node, subscribes to topic, and sends messages to it based on user input. then, creates a topic with the topic id and fails.                                          |

* needs to be executed multiple times sequentially to go through the entire script.

| parameter                | description                                                                                                          | example                                                 |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| <RIF_COMMS_NODE_ADDRESS> | address and GRPC port for running RIF Comms node.                                                                    | "localhost:5013"                                        |
| <RSK_ADDRESS>            | RSK address to be used as sender or receiver of communications invoked from python scripts, onto the RIF Comms node. | "0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"            |
| <TOPIC_ID>               | topic ID to be used by the python script when subscribing to a topic.                                                | "16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf" |
