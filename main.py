import time
import json
import random
import logging
from web3 import Web3
from flask import Flask, render_template_string, jsonify
from threading import Thread

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated LoRaWAN components
class LoRaWANDevice:
    def send(self, payload):
        rssi = -int(random.uniform(70, 120))
        snr = round(random.uniform(1, 10), 1)
        spreading_factor = random.randint(7, 12)
        tx_power = random.randint(14, 20)
        
        if snr < 2:  # Simulate packet loss for poor signal conditions
            logging.info(f"Failed to send reading from sensor {payload['sensor_id']}")
            return None
        
        return {
            'payload': json.dumps(payload),
            'rssi': rssi,
            'snr': snr,
            'device_id': payload['sensor_id'],
            'spreading_factor': spreading_factor,
            'tx_power': tx_power
        }

class LoRaWANGateway:
    def receive(self, packet):
        logging.info(f"Gateway received: {packet}")
        return packet

class LoRaWANNetworkServer:
    def process(self, packet):
        packet['processed'] = True
        logging.info(f"Processed packet: {packet}")
        return packet

# Blockchain class
class Blockchain:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        self.account = self.w3.eth.accounts[0]
        self.w3.eth.default_account = self.account

        # Load ABI and contract address
        with open('contract_abi.json', 'r') as abi_file:
            self.abi = json.load(abi_file)
        with open('contract_address.txt', 'r') as address_file:
            self.contract_address = address_file.read().strip()

        self.contract_instance = self.w3.eth.contract(address=self.contract_address, abi=self.abi)

    def add_reading(self, sensor_id, sensor_type, value, timestamp):
        try:
            # Convert value to an integer (multiply by 100 to preserve 2 decimal places)
            int_value = int(float(value) * 100)
            
            # Get the current gas price
            gas_price = self.w3.eth.gas_price
            
            # Use a default gas limit
            gas_limit = 200000  # You might need to adjust this value

            # Call the contract function
            tx_hash = self.contract_instance.functions.addReading(
                sensor_id,
                sensor_type,
                int_value,
                int(timestamp)
            ).transact({
                'gas': gas_limit,
                'gasPrice': gas_price,
                'from': self.account,
            })
            
            # Wait for the transaction receipt
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if tx_receipt['status'] == 1:
                logging.info(f"Transaction successful. Gas used: {tx_receipt['gasUsed']}")
            else:
                logging.error(f"Transaction failed. Status: {tx_receipt['status']}")

            logging.info(f"Added reading to blockchain: {sensor_id}, {sensor_type}, {value}, {timestamp}")
        except Exception as e:
            logging.error(f"Error in add_reading: {str(e)}")
            raise

    def get_latest_reading(self, sensor_id):
        try:
            return self.contract_instance.functions.getLatestReading(sensor_id).call()
        except Exception as e:
            logging.error(f"Error in get_latest_reading: {str(e)}")
            return None

    def set_threshold(self, sensor_type, threshold):
        try:
            # Convert threshold to an integer (multiply by 100 to preserve 2 decimal places)
            int_threshold = int(float(threshold) * 100)
            
            tx_hash = self.contract_instance.functions.setThreshold(sensor_type, int_threshold).transact()
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if tx_receipt['status'] == 1:
                logging.info(f"Threshold set successfully for {sensor_type}: {threshold}")
            else:
                logging.error(f"Failed to set threshold for {sensor_type}")
        except Exception as e:
            logging.error(f"Error in set_threshold: {str(e)}")
            raise

    def get_threshold(self, sensor_type):
        try:
            threshold = self.contract_instance.functions.getThreshold(sensor_type).call()
            return threshold / 100  # Divide by 100 to convert back to a decimal
        except Exception as e:
            logging.error(f"Error in get_threshold: {str(e)}")
            return None

# Digital Twin
class DigitalTwin:
    def __init__(self):
        self.state = {}

    def update(self, packet):
        logging.info(f"Received packet: {packet}")
        payload = json.loads(packet['payload'])
        self.state[payload['sensor_id']] = {
            'type': payload['sensor_type'],
            'value': payload['value'],
            'timestamp': payload['timestamp'],
            'rssi': packet['rssi'],
            'snr': packet['snr'],
            'spreading_factor': packet['spreading_factor'],
            'tx_power': packet['tx_power']
        }
        logging.info(f"Updated digital twin state: {self.state}")

# Sensor Simulator
def simulate_sensors():
    sensors = [
        {'id': 'soil_moisture_1', 'type': 'soil_moisture', 'min': 0, 'max': 100},
        {'id': 'temperature_1', 'type': 'temperature', 'min': 0, 'max': 40},
        {'id': 'humidity_1', 'type': 'humidity', 'min': 0, 'max': 100}
    ]
    
    for sensor in sensors:
        value = round(random.uniform(sensor['min'], sensor['max']), 2)
        yield {
            'sensor_id': sensor['id'],
            'sensor_type': sensor['type'],
            'value': value,
            'timestamp': int(time.time())
        }

# Flask app for visualization
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
        <head>
            <title>IoT Agriculture Dashboard</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 20px; box-sizing: border-box; }
                h1 { text-align: center; color: #333; }
                .container { 
                    display: flex; 
                    justify-content: space-between; 
                    flex-wrap: wrap; 
                    max-width: 1200px; 
                    margin: 0 auto; 
                }
                .chart { 
                    width: calc(33.33% - 20px); 
                    height: 250px; 
                    margin-bottom: 20px; 
                    background-color: #f9f9f9;
                    border-radius: 8px;
                    padding: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                @media (max-width: 768px) {
                    .chart { width: 100%; }
                }
            </style>
        </head>
        <body>
            <h1>IoT Agriculture Dashboard</h1>
            <div class="container" id="chartContainer"></div>
            <script>
                const charts = {};

                function createChart(sensorId, label) {
                    const chartDiv = document.createElement('div');
                    chartDiv.className = 'chart';
                    const canvas = document.createElement('canvas');
                    chartDiv.appendChild(canvas);
                    
                    const alertDiv = document.createElement('div');
                    alertDiv.id = `alert-${sensorId}`;
                    alertDiv.style.color = 'red';
                    chartDiv.appendChild(alertDiv);
                    
                    document.getElementById('chartContainer').appendChild(chartDiv);

                    return new Chart(canvas, {
                        type: 'line',
                        data: {
                            labels: [],
                            datasets: [{
                                label: label,
                                data: [],
                                borderColor: 'rgb(75, 192, 192)',
                                tension: 0.1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true
                                }
                            }
                        }
                    });
                }

                function updateCharts() {
                    fetch('/data')
                        .then(response => response.json())
                        .then(data => {
                            const timestamp = new Date().toLocaleTimeString();

                            Object.entries(data).forEach(([sensorId, sensorData]) => {
                                if (!charts[sensorId]) {
                                    charts[sensorId] = createChart(sensorId, `${sensorData.type} (${sensorId})`);
                                }

                                const chart = charts[sensorId];
                                chart.data.labels.push(timestamp);
                                chart.data.datasets[0].data.push(sensorData.value);

                                // Limit the number of data points shown
                                const maxDataPoints = 10;
                                if (chart.data.labels.length > maxDataPoints) {
                                    chart.data.labels.shift();
                                    chart.data.datasets[0].data.shift();
                                }

                                chart.update();
                                
                                // Update alert status
                                const alertDiv = document.getElementById(`alert-${sensorId}`);
                                if (sensorData.alert) {
                                    alertDiv.textContent = `Alert: ${sensorData.type} exceeded threshold!`;
                                } else {
                                    alertDiv.textContent = '';
                                }
                    
                            });
                        });
                }

                // Update charts every 5 seconds
                setInterval(updateCharts, 5000);
                // Initial update
                updateCharts();
            </script>
        </body>
    </html>
    ''')

@app.route('/data')
def data():
    return jsonify(digital_twin.state)

# Main simulation loop
def run_simulation():
    lorawan_device = LoRaWANDevice()
    gateway = LoRaWANGateway()
    network_server = LoRaWANNetworkServer()
    global digital_twin
    digital_twin = DigitalTwin()
    blockchain = Blockchain()

    while True:
        for sensor_reading in simulate_sensors():
            # LoRaWAN transmission
            lorawan_packet = lorawan_device.send(sensor_reading)
            if lorawan_packet:
                gateway_packet = gateway.receive(lorawan_packet)
                processed_packet = network_server.process(gateway_packet)

                # Update Digital Twin
                digital_twin.update(processed_packet)

                # Add to Blockchain
                payload = json.loads(processed_packet['payload'])
                blockchain.add_reading(payload['sensor_id'], payload['sensor_type'], payload['value'], payload['timestamp'])

                # Check smart contract thresholds
                threshold = blockchain.get_threshold(payload['sensor_type'])
                if threshold and payload['value'] > threshold:
                    logging.warning(f"Alert! {payload['sensor_type']} sensor {payload['sensor_id']} exceeded threshold: {payload['value']} > {threshold}")
                    digital_twin.state[payload['sensor_id']]['alert'] = True  # Set alert flag
                else:
                    digital_twin.state[payload['sensor_id']]['alert'] = False  # Clear alert flag

        time.sleep(5)  # Wait 5 seconds before next iteration

if __name__ == "__main__":
    # Start the simulation in a separate thread
    simulation_thread = Thread(target=run_simulation)
    simulation_thread.start()

    # Start the Flask app
    app.run(debug=True, use_reloader=False)
