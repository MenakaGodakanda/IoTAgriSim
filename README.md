# IoT Agriculture Simulation with LoRaWAN, Digital Twin, and Blockchain

## Overview

This project demonstrates an integrated IoT-based smart farming system that combines IoT Sensors, LoRaWAN Communication, Digital Twin, Blockchain, and Web Visualization. This is a complete simulation designed to run on Ubuntu 22.04 in a VirtualBox virtual machine without requiring any physical hardware.

## Features

- **Simulated IoT Sensors**: Generate realistic agricultural data (soil moisture, temperature, humidity)
- **Mock LoRaWAN Network**: Simulates LoRaWAN communication with RSSI, SNR, spreading factors, and packet loss
- **Digital Twin Engine**: Real-time virtual representation of farm conditions
- **Blockchain Integration**: Immutable data storage and smart contract execution
- **Web Dashboard**: Live visualization of sensor data and network metrics

## System Architecture
<img width="722" height="600" alt="Screenshot 2024-10-14 at 5 31 43 pm" src="https://github.com/user-attachments/assets/925dc1c7-c7b0-46ac-971c-9088364479de" />

### Explanation:
- **IoT Field Sensors**: Simulated using Python scripts to generate random readings every 5 seconds for soil moisture, temperature, and humidity sensors.
- **LoRaWAN Network**: A mock LoRaWAN module simulating key features such as spreading factors, transmission power, and signal-to-noise ratio (SNR).
- **Digital Twin**: Maintains the current state of all sensors, including LoRaWAN-specific information.
- **Blockchain and Smart Contracts**: Simulates data storage on a blockchain and smart contract execution using Ganache and Solidity.
- **Web Application**: A Flask-based web application providing a real-time dashboard of sensor data.

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
Open a terminal and run `ganache-cli`
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

https://github.com/user-attachments/assets/4f559c75-f5ef-4ee3-873c-7ecd4f2c9284

- **Thresholds**:
  -   humidity = 70%
  -   soil_moisture = 30%
  -   temperature = 35°C

## Understanding the Output

### Dashboard Visualisation

<img width="1201" height="409" alt="Web Dashboard" src="https://github.com/user-attachments/assets/8be13e80-5e92-4964-8e51-ffa4bd890951" />

- The web-based dashboard successfully displayed real-time sensor readings for soil moisture, temperature, and humidity. 
- The dashboard effectively alerted users when sensor readings exceeded predefined thresholds. 
- For instance, when the humidity sensor reading reached 77.8, surpassing the threshold of 70, the dashboard promptly displayed an alert.

### Log Output
```
2025-12-01 16:14:27,163 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17}
2025-12-01 16:14:27,163 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:27,163 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:27,163 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 40.67, 'timestamp': 1764576867, 'rssi': -107, 'snr': 2.5, 'spreading_factor': 7, 'tx_power': 17}}
2025-12-01 16:14:27,168 - INFO -  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2025-12-01 16:14:27,204 - INFO - Transaction successful. Gas used: 125135
2025-12-01 16:14:27,204 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 40.67, 1764576867
2025-12-01 16:14:27,212 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 40.67 > 30.0
```
- The log output analysis revealed a comprehensive cycle of IoT data flow, encompassing several crucial stages:
  - Gateway data reception
  - Packet processing
  - Digital twin state updates
  - Blockchain transactions
  - Threshold alerts
- The log contains detailed payload information, including sensor ID, sensor type, value, timestamp, RSSI, SNR, spreading factor, and TX power.
- This output demonstrates the successful integration of packet processing, digital twin updates, blockchain transactions, and threshold alerts within our framework.

### Blockchain Transaction
```
eth_getTransactionReceipt
eth_call
eth_getCode
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x084073ba3e9bfe6b08138f6635cc4f5b105cb607c5caba06943dd56d3e1e8daa
  Gas usage: 22496
  Block number: 2
  Block time: Mon Dec 01 2025 16:14:16 GMT+0800 (Australian Western Standard Time)
```
- This illustrates the complete transaction lifecycle from simulation to confirmation. The transaction process encompassed three primary stages:
  - Pre-transaction simulation and gas estimation
  - Transaction execution and mining
  - Post-transaction receipt confirmation












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
<a href="https://link.springer.com/chapter/10.1007/978-3-032-13075-4_5">Securing Agricultural Sustainability: Integrating Digital Twins and Blockchain for Smart Farming</a> <br>

## License

This project is licensed under the MIT License.
