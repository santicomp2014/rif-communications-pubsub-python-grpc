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
| script                        | execution                                                                                       | behavior                                                                                                                                                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `receiver.py`                 | `python3 receiver.py <RIF_COMMS_NODE_ENDPOINT> <OUR_RSK_ADDRESS> <RSK_ADDRESS>`                                   | connects to RIF Comms node, registers given RSK address, subscribes to topic for said address and awaits for responses from it. when halting, sends a message to topic and unsubscribes from it.                                                                           |
| `sender.py`                   | `python3 sender.py <RIF_COMMS_NODE_ENDPOINT> <OUR_RSK_ADDRESS> <RSK_ADDRESS>`                                     | connects to RIF Comms node, subscribes to topic for given address, and sends messages to it based on user input. then, upon halting message sending, awaits for messages from said topic. upon halting this, unsubscribes from the topic.                                  |
| `connect-send-and-receive.py` | `python3 connect-send-and-receive.py <RIF_COMMS_NODE_ENDPOINT> <RSK_ADDRESS_1> <RSK_ADDRESS_2>` | connects to RIF Comms node, registers RSK address 1, subscribes to topic for said address and sends a message to it. then, subscribes to topic for RSK address 2 and awaits for messages from it. when halting, sends a message to its own topic and unsubscribes from it. |

| parameter                   | description                                                                           | example                                                   |
| --------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `<RIF_COMMS_NODE_ENDPOINT>` | address and GRPC port for the running RIF Comms node to connect to.                   | `"localhost:5013"`                                        |
| `<RSK_ADDRESS>`             | RSK address to be registered in the RIF Comms node, or as a topic ID to subscribe to. | `"0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"`            |
