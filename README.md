# IoT Agriculture Simulation with LoRaWAN, Digital Twin, and Blockchain

## Overview

This project demonstrates an integrated IoT-based smart farming system that combines IoT Sensors, LoRaWAN Communication, Digital Twin, Blockchain, and Web Visualization. This is a complete simulation designed to run on Ubuntu 22.04 in a VirtualBox virtual machine without requiring any physical hardware.

## Features

- **Simulated IoT Sensors**: Generate realistic agricultural data (soil moisture, temperature, humidity)
- **Mock LoRaWAN Network**: Simulates LoRaWAN communication with RSSI, SNR, spreading factors, and packet loss
- **Digital Twin Engine**: Real-time virtual representation of farm conditions
- **Blockchain Integration**: Immutable data storage and smart contract execution
- **Web Dashboard**: Live visualization of sensor data and network metrics

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
<img width="880" height="656" alt="Screenshot 2025-12-01 182723" src="https://github.com/user-attachments/assets/cf27e505-c4a4-4441-8a31-507911db1ece" />

### Deploy Smart Contract
Open a new terminal or command prompt (keep Ganache CLI running in the first one) and run following command:
```
python3 deploy_contract.py
```
<img width="1196" height="38" alt="Screenshot 2025-12-02 055249" src="https://github.com/user-attachments/assets/8b1d6be7-62e6-40ab-85a9-84a58de21a94" />

### Run the Main Script
```
python3 main.py
```
- Expected Output:
<img width="1196" height="515" alt="Screenshot 2025-12-02 055249 - Copy" src="https://github.com/user-attachments/assets/ffe967ca-bc18-4b2a-a6c4-394601e1c87d" />

### Visualize the Web Dashboard
- Open a web browser and go to http://127.0.0.1:5000 to see the visualization:

- Expected Output:

https://github.com/user-attachments/assets/4f559c75-f5ef-4ee3-873c-7ecd4f2c9284

- **Thresholds**:
-   soil_moisture = 30%
-   temperature = 35°C
-   humidity = 70%

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
