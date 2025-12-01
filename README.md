# Integrating IoT, LoRaWAN, Digital Twins and Blockchain for Smart Farming

## Project Description

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Installation Steps

#### 1. Clone this repository:
```
git clone https://github.com/MenakaGodakanda/IoTAgriSim.git
cd IoTAgriSim
```

#### 2. Install dependencies:
- Install Python:
```
sudo apt install python3 python3-pip
```

- Install Python packages:
```
pip3 install paho-mqtt cryptography web3 flask
```

- Install Ganache
Ganache is a personal blockchain for Ethereum development.
```
sudo npm install -g ganache-cli
```

## Run the Simulation

### Launch Ganache:
Open a terminal and run ganache-cli
```
ganache-cli
```

### Deploy Smart Contract
Open a new terminal or command prompt (keep Ganache CLI running in the first one) and run following command:
```
python3 deploy_contract.py
```

### Run the Main Script
```
python3 main.py
```
- Expected Output:

### Visualize the Web Dashboard
- Open a web browser and go to http://127.0.0.1:5000 to see the visualization:

## Project Structure
```
IoTAgriSim/
├── AgricultureSensor.sol
├── contract_abi.json
├── contract_address.txt
├── contract_bytecode.txt
├── deploy_contract.py
└── main.py
```

## Published Research

This system was presented at the IFIP-UNIVEN-CSIR Interbational Conference in Cybersecurity 2025 and published as a research conference paper. Read more here: <br>
<a href="">xxx</a> <br>

## License

This project is licensed under the MIT License.
