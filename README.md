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
1. the virtual environment [must be activated](#2-Activate-virtual-environment).
2. at least 1 [RIF Comms node](https://github.com/rsksmart/rif-communications-pubsub-node/) must be running.

#### 4.2 Scripts
| script           | execution                                                                   | behavior                                                                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client-1.py`    | `python3 client-1.py`                                                       | unclear.                                                                                                                                                                                       |
| `client-2.py`    | `python3 client-2.py`                                                       | unclear.                                                                                                                                                                                       |
| `lumino.py`      | `python3 lumino.py <RIF_COMMS_NODE_ENDPOINT> <RSK_ADDRESS> <TOPIC_ID>`       | connects to RIF Comms node, registers RSK address to get a peer ID, creates a topic with the address and awaits for responses from it. when halting, sends a message to topic and fails.*¹     |
| `lumino-send.py` | `python3 lumino-send.py <RIF_COMMS_NODE_ENDPOINT> <TOPIC_ID_1> <TOPIC_ID_2>` | connects to RIF Comms node, subscribes to 2 topics, sends messages to them based on user input, then fails upon halting message sending.*²                                                     |
| `receiver.py`    | `python3 receiver.py <RIF_COMMS_NODE_ENDPOINT> <RSK_ADDRESS>`                | connects to RIF Comms node, registers RSK address to get a peer ID, creates a topic with the address and awaits for responses from it. when halting, sends a message to topic and closes it.*¹ |
| `sender.py`      | `python3 sender.py <RIF_COMMS_NODE_ENDPOINT> <RSK_ADDRESS>`                     | connects to RIF Comms node, subscribes to topic, and sends messages to it based on user input. then, upon halting message sending, creates a topic with the topic id and fails.*²              |

\*¹ needs to be sequentially executed multiple times to go through the entire script.
<br/>
\*² messages cause exceptions in the RIF Comms node.

| parameter                  | description                                                                                                   | example                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `<RIF_COMMS_NODE_ENDPOINT>` | address and GRPC port for running RIF Comms node to connect to.                                               | `"localhost:5013"`                                        |
| `<RSK_ADDRESS>`            | RSK address to be used as sender or receiver of communications invoked from scripts, onto the RIF Comms node. | `"0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"`            |
| `<TOPIC_ID>`               | topic ID to be used by the script when subscribing to a topic.                                                | `"16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf"` |
