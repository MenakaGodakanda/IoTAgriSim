mcyber@mcyber-VirtualBox:~/IoTAgriSim$ python3 main.py 
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
2025-12-01 16:14:27,163 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17}
2025-12-01 16:14:27,163 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:27,163 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 40.67, "timestamp": 1764576867}', 'rssi': -107, 'snr': 2.5, 'device_id': 'soil_moisture_1', 'spreading_factor': 7, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:27,163 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 40.67, 'timestamp': 1764576867, 'rssi': -107, 'snr': 2.5, 'spreading_factor': 7, 'tx_power': 17}}
2025-12-01 16:14:27,168 - INFO -  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2025-12-01 16:14:27,204 - INFO - Transaction successful. Gas used: 125135
2025-12-01 16:14:27,204 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 40.67, 1764576867
2025-12-01 16:14:27,212 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 40.67 > 30.0
2025-12-01 16:14:27,212 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 6.01, "timestamp": 1764576867}', 'rssi': -100, 'snr': 8.2, 'device_id': 'temperature_1', 'spreading_factor': 7, 'tx_power': 20}
2025-12-01 16:14:27,212 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 6.01, "timestamp": 1764576867}', 'rssi': -100, 'snr': 8.2, 'device_id': 'temperature_1', 'spreading_factor': 7, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:27,212 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 6.01, "timestamp": 1764576867}', 'rssi': -100, 'snr': 8.2, 'device_id': 'temperature_1', 'spreading_factor': 7, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:27,212 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 40.67, 'timestamp': 1764576867, 'rssi': -107, 'snr': 2.5, 'spreading_factor': 7, 'tx_power': 17, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 6.01, 'timestamp': 1764576867, 'rssi': -100, 'snr': 8.2, 'spreading_factor': 7, 'tx_power': 20}}
2025-12-01 16:14:27,236 - INFO - Transaction successful. Gas used: 120485
2025-12-01 16:14:27,236 - INFO - Added reading to blockchain: temperature_1, temperature, 6.01, 1764576867
2025-12-01 16:14:27,243 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.03, "timestamp": 1764576867}', 'rssi': -107, 'snr': 6.0, 'device_id': 'humidity_1', 'spreading_factor': 7, 'tx_power': 18}
2025-12-01 16:14:27,243 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.03, "timestamp": 1764576867}', 'rssi': -107, 'snr': 6.0, 'device_id': 'humidity_1', 'spreading_factor': 7, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:27,243 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.03, "timestamp": 1764576867}', 'rssi': -107, 'snr': 6.0, 'device_id': 'humidity_1', 'spreading_factor': 7, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:27,243 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 40.67, 'timestamp': 1764576867, 'rssi': -107, 'snr': 2.5, 'spreading_factor': 7, 'tx_power': 17, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 6.01, 'timestamp': 1764576867, 'rssi': -100, 'snr': 8.2, 'spreading_factor': 7, 'tx_power': 20, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 18.03, 'timestamp': 1764576867, 'rssi': -107, 'snr': 6.0, 'spreading_factor': 7, 'tx_power': 18}}
2025-12-01 16:14:27,270 - INFO - Transaction successful. Gas used: 120413
2025-12-01 16:14:27,270 - INFO - Added reading to blockchain: humidity_1, humidity, 18.03, 1764576867
2025-12-01 16:14:32,283 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 51.33, "timestamp": 1764576872}', 'rssi': -74, 'snr': 3.1, 'device_id': 'soil_moisture_1', 'spreading_factor': 12, 'tx_power': 20}
2025-12-01 16:14:32,283 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 51.33, "timestamp": 1764576872}', 'rssi': -74, 'snr': 3.1, 'device_id': 'soil_moisture_1', 'spreading_factor': 12, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:32,284 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 51.33, "timestamp": 1764576872}', 'rssi': -74, 'snr': 3.1, 'device_id': 'soil_moisture_1', 'spreading_factor': 12, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:32,284 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 51.33, 'timestamp': 1764576872, 'rssi': -74, 'snr': 3.1, 'spreading_factor': 12, 'tx_power': 20}, 'temperature_1': {'type': 'temperature', 'value': 6.01, 'timestamp': 1764576867, 'rssi': -100, 'snr': 8.2, 'spreading_factor': 7, 'tx_power': 20, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 18.03, 'timestamp': 1764576867, 'rssi': -107, 'snr': 6.0, 'spreading_factor': 7, 'tx_power': 18, 'alert': False}}
2025-12-01 16:14:32,327 - INFO - Transaction successful. Gas used: 108035
2025-12-01 16:14:32,327 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 51.33, 1764576872
2025-12-01 16:14:32,334 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 51.33 > 30.0
2025-12-01 16:14:32,335 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.71, "timestamp": 1764576872}', 'rssi': -109, 'snr': 3.3, 'device_id': 'temperature_1', 'spreading_factor': 10, 'tx_power': 17}
2025-12-01 16:14:32,335 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.71, "timestamp": 1764576872}', 'rssi': -109, 'snr': 3.3, 'device_id': 'temperature_1', 'spreading_factor': 10, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:32,335 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.71, "timestamp": 1764576872}', 'rssi': -109, 'snr': 3.3, 'device_id': 'temperature_1', 'spreading_factor': 10, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:32,335 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 51.33, 'timestamp': 1764576872, 'rssi': -74, 'snr': 3.1, 'spreading_factor': 12, 'tx_power': 20, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 13.71, 'timestamp': 1764576872, 'rssi': -109, 'snr': 3.3, 'spreading_factor': 10, 'tx_power': 17}, 'humidity_1': {'type': 'humidity', 'value': 18.03, 'timestamp': 1764576867, 'rssi': -107, 'snr': 6.0, 'spreading_factor': 7, 'tx_power': 18, 'alert': False}}
2025-12-01 16:14:32,364 - INFO - Transaction successful. Gas used: 103385
2025-12-01 16:14:32,364 - INFO - Added reading to blockchain: temperature_1, temperature, 13.71, 1764576872
2025-12-01 16:14:32,372 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 4.24, "timestamp": 1764576872}', 'rssi': -112, 'snr': 8.5, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 16}
2025-12-01 16:14:32,373 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 4.24, "timestamp": 1764576872}', 'rssi': -112, 'snr': 8.5, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 16, 'processed': True}
2025-12-01 16:14:32,373 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 4.24, "timestamp": 1764576872}', 'rssi': -112, 'snr': 8.5, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 16, 'processed': True}
2025-12-01 16:14:32,373 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 51.33, 'timestamp': 1764576872, 'rssi': -74, 'snr': 3.1, 'spreading_factor': 12, 'tx_power': 20, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 13.71, 'timestamp': 1764576872, 'rssi': -109, 'snr': 3.3, 'spreading_factor': 10, 'tx_power': 17, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 4.24, 'timestamp': 1764576872, 'rssi': -112, 'snr': 8.5, 'spreading_factor': 10, 'tx_power': 16}}
2025-12-01 16:14:32,406 - INFO - Transaction successful. Gas used: 103313
2025-12-01 16:14:32,406 - INFO - Added reading to blockchain: humidity_1, humidity, 4.24, 1764576872
2025-12-01 16:14:37,443 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 73.09, "timestamp": 1764576877}', 'rssi': -104, 'snr': 4.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18}
2025-12-01 16:14:37,443 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 73.09, "timestamp": 1764576877}', 'rssi': -104, 'snr': 4.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:37,443 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 73.09, "timestamp": 1764576877}', 'rssi': -104, 'snr': 4.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:37,443 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 73.09, 'timestamp': 1764576877, 'rssi': -104, 'snr': 4.7, 'spreading_factor': 10, 'tx_power': 18}, 'temperature_1': {'type': 'temperature', 'value': 13.71, 'timestamp': 1764576872, 'rssi': -109, 'snr': 3.3, 'spreading_factor': 10, 'tx_power': 17, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 4.24, 'timestamp': 1764576872, 'rssi': -112, 'snr': 8.5, 'spreading_factor': 10, 'tx_power': 16, 'alert': False}}
2025-12-01 16:14:37,478 - INFO - Transaction successful. Gas used: 108035
2025-12-01 16:14:37,478 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 73.09, 1764576877
2025-12-01 16:14:37,485 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 73.09 > 30.0
2025-12-01 16:14:37,485 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 1.51, "timestamp": 1764576877}', 'rssi': -96, 'snr': 6.1, 'device_id': 'temperature_1', 'spreading_factor': 12, 'tx_power': 18}
2025-12-01 16:14:37,485 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 1.51, "timestamp": 1764576877}', 'rssi': -96, 'snr': 6.1, 'device_id': 'temperature_1', 'spreading_factor': 12, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:37,485 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 1.51, "timestamp": 1764576877}', 'rssi': -96, 'snr': 6.1, 'device_id': 'temperature_1', 'spreading_factor': 12, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:37,485 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 73.09, 'timestamp': 1764576877, 'rssi': -104, 'snr': 4.7, 'spreading_factor': 10, 'tx_power': 18, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 1.51, 'timestamp': 1764576877, 'rssi': -96, 'snr': 6.1, 'spreading_factor': 12, 'tx_power': 18}, 'humidity_1': {'type': 'humidity', 'value': 4.24, 'timestamp': 1764576872, 'rssi': -112, 'snr': 8.5, 'spreading_factor': 10, 'tx_power': 16, 'alert': False}}
2025-12-01 16:14:37,504 - INFO - Transaction successful. Gas used: 103373
2025-12-01 16:14:37,504 - INFO - Added reading to blockchain: temperature_1, temperature, 1.51, 1764576877
2025-12-01 16:14:37,512 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 39.44, "timestamp": 1764576877}', 'rssi': -115, 'snr': 9.1, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 14}
2025-12-01 16:14:37,512 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 39.44, "timestamp": 1764576877}', 'rssi': -115, 'snr': 9.1, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 14, 'processed': True}
2025-12-01 16:14:37,512 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 39.44, "timestamp": 1764576877}', 'rssi': -115, 'snr': 9.1, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 14, 'processed': True}
2025-12-01 16:14:37,512 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 73.09, 'timestamp': 1764576877, 'rssi': -104, 'snr': 4.7, 'spreading_factor': 10, 'tx_power': 18, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 1.51, 'timestamp': 1764576877, 'rssi': -96, 'snr': 6.1, 'spreading_factor': 12, 'tx_power': 18, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 39.44, 'timestamp': 1764576877, 'rssi': -115, 'snr': 9.1, 'spreading_factor': 9, 'tx_power': 14}}
2025-12-01 16:14:37,541 - INFO - Transaction successful. Gas used: 103313
2025-12-01 16:14:37,541 - INFO - Added reading to blockchain: humidity_1, humidity, 39.44, 1764576877
2025-12-01 16:14:42,564 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 92.66, "timestamp": 1764576882}', 'rssi': -117, 'snr': 7.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 14}
2025-12-01 16:14:42,565 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 92.66, "timestamp": 1764576882}', 'rssi': -117, 'snr': 7.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 14, 'processed': True}
2025-12-01 16:14:42,565 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 92.66, "timestamp": 1764576882}', 'rssi': -117, 'snr': 7.7, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 14, 'processed': True}
2025-12-01 16:14:42,565 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 92.66, 'timestamp': 1764576882, 'rssi': -117, 'snr': 7.7, 'spreading_factor': 8, 'tx_power': 14}, 'temperature_1': {'type': 'temperature', 'value': 1.51, 'timestamp': 1764576877, 'rssi': -96, 'snr': 6.1, 'spreading_factor': 12, 'tx_power': 18, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 39.44, 'timestamp': 1764576877, 'rssi': -115, 'snr': 9.1, 'spreading_factor': 9, 'tx_power': 14, 'alert': False}}
2025-12-01 16:14:42,597 - INFO - Transaction successful. Gas used: 108035
2025-12-01 16:14:42,597 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 92.66, 1764576882
2025-12-01 16:14:42,607 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 92.66 > 30.0
2025-12-01 16:14:42,607 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 0.32, "timestamp": 1764576882}', 'rssi': -89, 'snr': 8.0, 'device_id': 'temperature_1', 'spreading_factor': 8, 'tx_power': 19}
2025-12-01 16:14:42,607 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 0.32, "timestamp": 1764576882}', 'rssi': -89, 'snr': 8.0, 'device_id': 'temperature_1', 'spreading_factor': 8, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:42,607 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 0.32, "timestamp": 1764576882}', 'rssi': -89, 'snr': 8.0, 'device_id': 'temperature_1', 'spreading_factor': 8, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:42,607 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 92.66, 'timestamp': 1764576882, 'rssi': -117, 'snr': 7.7, 'spreading_factor': 8, 'tx_power': 14, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 0.32, 'timestamp': 1764576882, 'rssi': -89, 'snr': 8.0, 'spreading_factor': 8, 'tx_power': 19}, 'humidity_1': {'type': 'humidity', 'value': 39.44, 'timestamp': 1764576877, 'rssi': -115, 'snr': 9.1, 'spreading_factor': 9, 'tx_power': 14, 'alert': False}}
2025-12-01 16:14:42,629 - INFO - Transaction successful. Gas used: 103373
2025-12-01 16:14:42,629 - INFO - Added reading to blockchain: temperature_1, temperature, 0.32, 1764576882
2025-12-01 16:14:42,640 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 46.68, "timestamp": 1764576882}', 'rssi': -112, 'snr': 9.9, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 19}
2025-12-01 16:14:42,640 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 46.68, "timestamp": 1764576882}', 'rssi': -112, 'snr': 9.9, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:42,640 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 46.68, "timestamp": 1764576882}', 'rssi': -112, 'snr': 9.9, 'device_id': 'humidity_1', 'spreading_factor': 10, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:42,640 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 92.66, 'timestamp': 1764576882, 'rssi': -117, 'snr': 7.7, 'spreading_factor': 8, 'tx_power': 14, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 0.32, 'timestamp': 1764576882, 'rssi': -89, 'snr': 8.0, 'spreading_factor': 8, 'tx_power': 19, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 46.68, 'timestamp': 1764576882, 'rssi': -112, 'snr': 9.9, 'spreading_factor': 10, 'tx_power': 19}}
2025-12-01 16:14:42,661 - INFO - Transaction successful. Gas used: 103313
2025-12-01 16:14:42,661 - INFO - Added reading to blockchain: humidity_1, humidity, 46.68, 1764576882
2025-12-01 16:14:47,696 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 36.16, "timestamp": 1764576887}', 'rssi': -98, 'snr': 5.9, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18}
2025-12-01 16:14:47,696 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 36.16, "timestamp": 1764576887}', 'rssi': -98, 'snr': 5.9, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:47,696 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 36.16, "timestamp": 1764576887}', 'rssi': -98, 'snr': 5.9, 'device_id': 'soil_moisture_1', 'spreading_factor': 10, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:47,696 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 36.16, 'timestamp': 1764576887, 'rssi': -98, 'snr': 5.9, 'spreading_factor': 10, 'tx_power': 18}, 'temperature_1': {'type': 'temperature', 'value': 0.32, 'timestamp': 1764576882, 'rssi': -89, 'snr': 8.0, 'spreading_factor': 8, 'tx_power': 19, 'alert': False}, 'humidity_1': {'type': 'humidity', 'value': 46.68, 'timestamp': 1764576882, 'rssi': -112, 'snr': 9.9, 'spreading_factor': 10, 'tx_power': 19, 'alert': False}}
2025-12-01 16:14:47,721 - INFO - Transaction successful. Gas used: 108035
2025-12-01 16:14:47,722 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 36.16, 1764576887
2025-12-01 16:14:47,730 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 36.16 > 30.0
2025-12-01 16:14:47,730 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 36.15, "timestamp": 1764576887}', 'rssi': -103, 'snr': 8.3, 'device_id': 'temperature_1', 'spreading_factor': 11, 'tx_power': 18}
2025-12-01 16:14:47,730 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 36.15, "timestamp": 1764576887}', 'rssi': -103, 'snr': 8.3, 'device_id': 'temperature_1', 'spreading_factor': 11, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:47,730 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 36.15, "timestamp": 1764576887}', 'rssi': -103, 'snr': 8.3, 'device_id': 'temperature_1', 'spreading_factor': 11, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:47,730 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 36.16, 'timestamp': 1764576887, 'rssi': -98, 'snr': 5.9, 'spreading_factor': 10, 'tx_power': 18, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 36.15, 'timestamp': 1764576887, 'rssi': -103, 'snr': 8.3, 'spreading_factor': 11, 'tx_power': 18}, 'humidity_1': {'type': 'humidity', 'value': 46.68, 'timestamp': 1764576882, 'rssi': -112, 'snr': 9.9, 'spreading_factor': 10, 'tx_power': 19, 'alert': False}}
2025-12-01 16:14:47,755 - INFO - Transaction successful. Gas used: 107987
2025-12-01 16:14:47,756 - INFO - Added reading to blockchain: temperature_1, temperature, 36.15, 1764576887
2025-12-01 16:14:47,765 - WARNING - Alert! temperature sensor temperature_1 exceeded threshold: 36.15 > 35.0
2025-12-01 16:14:47,766 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 87.19, "timestamp": 1764576887}', 'rssi': -95, 'snr': 7.1, 'device_id': 'humidity_1', 'spreading_factor': 11, 'tx_power': 17}
2025-12-01 16:14:47,766 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 87.19, "timestamp": 1764576887}', 'rssi': -95, 'snr': 7.1, 'device_id': 'humidity_1', 'spreading_factor': 11, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:47,766 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 87.19, "timestamp": 1764576887}', 'rssi': -95, 'snr': 7.1, 'device_id': 'humidity_1', 'spreading_factor': 11, 'tx_power': 17, 'processed': True}
2025-12-01 16:14:47,766 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 36.16, 'timestamp': 1764576887, 'rssi': -98, 'snr': 5.9, 'spreading_factor': 10, 'tx_power': 18, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 36.15, 'timestamp': 1764576887, 'rssi': -103, 'snr': 8.3, 'spreading_factor': 11, 'tx_power': 18, 'alert': True}, 'humidity_1': {'type': 'humidity', 'value': 87.19, 'timestamp': 1764576887, 'rssi': -95, 'snr': 7.1, 'spreading_factor': 11, 'tx_power': 17}}
2025-12-01 16:14:47,787 - INFO - Transaction successful. Gas used: 107915
2025-12-01 16:14:47,787 - INFO - Added reading to blockchain: humidity_1, humidity, 87.19, 1764576887
2025-12-01 16:14:47,794 - WARNING - Alert! humidity sensor humidity_1 exceeded threshold: 87.19 > 70.0
2025-12-01 16:14:52,802 - INFO - Failed to send reading from sensor soil_moisture_1
2025-12-01 16:14:52,802 - INFO - Failed to send reading from sensor temperature_1
2025-12-01 16:14:52,802 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.64, "timestamp": 1764576892}', 'rssi': -114, 'snr': 6.7, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 18}
2025-12-01 16:14:52,802 - INFO - Processed packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.64, "timestamp": 1764576892}', 'rssi': -114, 'snr': 6.7, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:52,803 - INFO - Received packet: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 18.64, "timestamp": 1764576892}', 'rssi': -114, 'snr': 6.7, 'device_id': 'humidity_1', 'spreading_factor': 9, 'tx_power': 18, 'processed': True}
2025-12-01 16:14:52,803 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 36.16, 'timestamp': 1764576887, 'rssi': -98, 'snr': 5.9, 'spreading_factor': 10, 'tx_power': 18, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 36.15, 'timestamp': 1764576887, 'rssi': -103, 'snr': 8.3, 'spreading_factor': 11, 'tx_power': 18, 'alert': True}, 'humidity_1': {'type': 'humidity', 'value': 18.64, 'timestamp': 1764576892, 'rssi': -114, 'snr': 6.7, 'spreading_factor': 9, 'tx_power': 18}}
2025-12-01 16:14:52,829 - INFO - Transaction successful. Gas used: 103313
2025-12-01 16:14:52,829 - INFO - Added reading to blockchain: humidity_1, humidity, 18.64, 1764576892
2025-12-01 16:14:53,050 - INFO - 127.0.0.1 - - [01/Dec/2025 16:14:53] "GET / HTTP/1.1" 200 -
2025-12-01 16:14:53,085 - INFO - 127.0.0.1 - - [01/Dec/2025 16:14:53] "GET /data HTTP/1.1" 200 -
2025-12-01 16:14:53,087 - INFO - 127.0.0.1 - - [01/Dec/2025 16:14:53] "GET /favicon.ico HTTP/1.1" 404 -
2025-12-01 16:14:57,858 - INFO - Gateway received: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 72.29, "timestamp": 1764576897}', 'rssi': -116, 'snr': 9.3, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 19}
2025-12-01 16:14:57,859 - INFO - Processed packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 72.29, "timestamp": 1764576897}', 'rssi': -116, 'snr': 9.3, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:57,859 - INFO - Received packet: {'payload': '{"sensor_id": "soil_moisture_1", "sensor_type": "soil_moisture", "value": 72.29, "timestamp": 1764576897}', 'rssi': -116, 'snr': 9.3, 'device_id': 'soil_moisture_1', 'spreading_factor': 8, 'tx_power': 19, 'processed': True}
2025-12-01 16:14:57,859 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 72.29, 'timestamp': 1764576897, 'rssi': -116, 'snr': 9.3, 'spreading_factor': 8, 'tx_power': 19}, 'temperature_1': {'type': 'temperature', 'value': 36.15, 'timestamp': 1764576887, 'rssi': -103, 'snr': 8.3, 'spreading_factor': 11, 'tx_power': 18, 'alert': True}, 'humidity_1': {'type': 'humidity', 'value': 18.64, 'timestamp': 1764576892, 'rssi': -114, 'snr': 6.7, 'spreading_factor': 9, 'tx_power': 18, 'alert': False}}
2025-12-01 16:14:57,890 - INFO - Transaction successful. Gas used: 108035
2025-12-01 16:14:57,890 - INFO - Added reading to blockchain: soil_moisture_1, soil_moisture, 72.29, 1764576897
2025-12-01 16:14:57,895 - WARNING - Alert! soil_moisture sensor soil_moisture_1 exceeded threshold: 72.29 > 30.0
2025-12-01 16:14:57,895 - INFO - Gateway received: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.83, "timestamp": 1764576897}', 'rssi': -108, 'snr': 4.8, 'device_id': 'temperature_1', 'spreading_factor': 9, 'tx_power': 20}
2025-12-01 16:14:57,895 - INFO - Processed packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.83, "timestamp": 1764576897}', 'rssi': -108, 'snr': 4.8, 'device_id': 'temperature_1', 'spreading_factor': 9, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:57,895 - INFO - Received packet: {'payload': '{"sensor_id": "temperature_1", "sensor_type": "temperature", "value": 13.83, "timestamp": 1764576897}', 'rssi': -108, 'snr': 4.8, 'device_id': 'temperature_1', 'spreading_factor': 9, 'tx_power': 20, 'processed': True}
2025-12-01 16:14:57,895 - INFO - Updated digital twin state: {'soil_moisture_1': {'type': 'soil_moisture', 'value': 72.29, 'timestamp': 1764576897, 'rssi': -116, 'snr': 9.3, 'spreading_factor': 8, 'tx_power': 19, 'alert': True}, 'temperature_1': {'type': 'temperature', 'value': 13.83, 'timestamp': 1764576897, 'rssi': -108, 'snr': 4.8, 'spreading_factor': 9, 'tx_power': 20}, 'humidity_1': {'type': 'humidity', 'value': 18.64, 'timestamp': 1764576892, 'rssi': -114, 'snr': 6.7, 'spreading_factor': 9, 'tx_power': 18, 'alert': False}}
2025-12-01 16:14:57,910 - INFO - Transaction successful. Gas used: 103385
2025-12-01 16:14:57,910 - INFO - Added reading to blockchain: temperature_1, temperature, 13.83, 1764576897
2025-12-01 16:14:57,915 - INFO - Gateway received: {'payload': '{"sensor_id": "humidity_1", "sensor_type": "humidity", "value": 95.92, "timestamp": 1764576897}', 'rssi': -116, 'snr': 3.9, 'device_id': 'humidity_1', 'spreading_factor': 7, 'tx_power': 16}



mcyber@mcyber-VirtualBox:~/IoTAgriSim$ ganache-cli
ganache v7.9.2 (@ganache/cli: 0.10.2, @ganache/core: 0.10.2)
Starting RPC server

Available Accounts
==================
(0) 0xE64602A1be7BE062a5AFE2a751E30ac9ED052bD8 (1000 ETH)
(1) 0xA93BBCB47f1C1A42f3D7227995eF164dFf846e4a (1000 ETH)
(2) 0xF1644432dc4ac1677D3453F9F2Fe8d9dE34Df30C (1000 ETH)
(3) 0x8e779795Fcc4654f1b389B39eaAc28512028c2DE (1000 ETH)
(4) 0xA5AF0b09288a0BcbE05f9AE5Fdf0189BF0D687D3 (1000 ETH)
(5) 0x01291Fb5E3270ba5Ec8F85146A89937E4051A438 (1000 ETH)
(6) 0x8aB3cAdd882db6b165EED87Ce54bCEeA9FEBa12a (1000 ETH)
(7) 0xF062ddaa6B32553B5Bc25d9B3fF97Ab13462D8F3 (1000 ETH)
(8) 0x826aa1b14BD4D1F62b384Ddc1DAD5F82119997F2 (1000 ETH)
(9) 0x37845a2c2b746EC3B2474e8D3BBbDA812D2Ac492 (1000 ETH)

Private Keys
==================
(0) 0x65521598ff387e37ec5cab247e0837911fe7c71e936af58a53bc08904fbd3004
(1) 0xe416a7f6ec48a87155d134d331252865552a77cb0e399ab35a156c9be0f361cf
(2) 0xad1c2d1d3896542502f4ff051e7bc662ba4f344304cd3c6173fbe978cc534c9c
(3) 0xb4780dddc05694622c16b7e3f65ff9254d28d54cd4ea99f0bb38928da09a92ef
(4) 0x5f9c82462699fb2aa30a9da6764c4c9ca0d43be2ae187ede8a02dd0b13cd7576
(5) 0x79ece45f0e077b8a1abf7c34726fc2409e74dcd1a9c90a11628a4524f12aa623
(6) 0x9dbdad005897abbf7fc3106d09052d52e433b4b240c0d47e88900841e8338760
(7) 0xa4849a4e266eb5a1fcb3d734619df33f7662285d5fd422c61da15daed3d731fb
(8) 0xe052817409b4eb9507badfda4dff2dbff02df4d9a4a59321c67bfb5c13748163
(9) 0x5306b91abe4839c733e8c0c82b2218e0047c72826b761eefeee7be2b2a8c3b4f

HD Wallet
==================
Mnemonic:      tail theory actor violin green celery glimpse remove birth vivid leg toy
Base HD Path:  m/44'/60'/0'/0/{account_index}

Default Gas Price
==================
2000000000

BlockGas Limit
==================
30000000

Call Gas Limit
==================
50000000

Chain
==================
Hardfork: shanghai
Id:       1337

RPC Listening on 127.0.0.1:8545
eth_accounts
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x3ee96b6e4b40d77eb538137f33af2c41b0c27eb343972ba5a6b6f3dd792a0570
  Gas usage: 22544
  Block number: 1
  Block time: Mon Dec 01 2025 16:14:16 GMT+0800 (Australian Western Standard Time)

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

eth_getTransactionReceipt
eth_call
eth_getCode
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xa7b9b61abf1950558b9054007826b3f53c03d8c3fe6ef45c67ca138d444d61a6
  Gas usage: 22424
  Block number: 3
  Block time: Mon Dec 01 2025 16:14:16 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_getCode
eth_accounts
eth_getBlockByNumber
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xd5271d3943456513b1ffd45b3d89c2c4bf290ef54135b289a7dd2eb82f6da666
  Contract created: 0xb925e4e94ec6e1541216ee3e76c045ee3743a6ef
  Gas usage: 783938
  Block number: 4
  Block time: Mon Dec 01 2025 16:14:23 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_accounts
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xf22ba018735b75da7b59cb7c9a45fcaf6a7b0d1afc5d18472cc5ac454cb9530d
  Gas usage: 125135
  Block number: 5
  Block time: Mon Dec 01 2025 16:14:27 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xfbd37bd73eab59f6a2c1f688ad74e4dbfb46ffdc3c2ae265f10bee81cd20fa24
  Gas usage: 120485
  Block number: 6
  Block time: Mon Dec 01 2025 16:14:27 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xbe931c50668deeb2f32a4d399ccff4408e5042c5f5b13a0c2edb7dbe6fe23452
  Gas usage: 120413
  Block number: 7
  Block time: Mon Dec 01 2025 16:14:27 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x3bb01aca0719f73ad355a64cfc1dddc202bfc2aa98ae0e92fd46a46b4886c59f
  Gas usage: 108035
  Block number: 8
  Block time: Mon Dec 01 2025 16:14:32 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x90f65256c93fc95d391263320011f6ca6aa48d46fb7ab24e937dd81d5cf0f8f2
  Gas usage: 103385
  Block number: 9
  Block time: Mon Dec 01 2025 16:14:32 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xa708ead5eacc9c35d6d6970e0ea5bfbfa7e5b867e1d6c5c6afa4dac5e4a3f9e2
  Gas usage: 103313
  Block number: 10
  Block time: Mon Dec 01 2025 16:14:32 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x8f4634a1c3956a76e20cb53036ec467a72d0eab47093e3ca05f82eaeefbad4e6
  Gas usage: 108035
  Block number: 11
  Block time: Mon Dec 01 2025 16:14:37 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x6ac5266e1d3a47ec788322ae92a7a9281b899ab0c24d98d5bdd25badcdefdad1
  Gas usage: 103373
  Block number: 12
  Block time: Mon Dec 01 2025 16:14:37 GMT+0800 (Australian Western Standard Time)

eth_getTransactionReceipt
eth_call
eth_gasPrice
eth_getBlockByNumber
eth_sendTransaction



