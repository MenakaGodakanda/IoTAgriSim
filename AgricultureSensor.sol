// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgricultureSensor {
    struct Reading {
        string sensorType;
        uint256 value;
        uint256 timestamp;
    }

    mapping(string => Reading[]) public readings;
    mapping(string => uint256) public thresholds;

    event NewReading(string sensorId, string sensorType, uint256 value, uint256 timestamp);
    event ThresholdExceeded(string sensorId, string sensorType, uint256 value, uint256 threshold);

    constructor() {
        // Set default thresholds
        thresholds["soil_moisture"] = 30 * 100; // 30% (multiplied by 100 for 2 decimal places)
        thresholds["temperature"] = 35 * 100; // 35°C
        thresholds["humidity"] = 70 * 100; // 70%
    }

    function addReading(string memory sensorId, string memory sensorType, uint256 value, uint256 timestamp) public {
        readings[sensorId].push(Reading(sensorType, value, timestamp));
        emit NewReading(sensorId, sensorType, value, timestamp);

        if (value > thresholds[sensorType]) {
            emit ThresholdExceeded(sensorId, sensorType, value, thresholds[sensorType]);
        }
    }

    function getLatestReading(string memory sensorId) public view returns (string memory, uint256, uint256) {
        require(readings[sensorId].length > 0, "No readings for this sensor");
        Reading memory latest = readings[sensorId][readings[sensorId].length - 1];
        return (latest.sensorType, latest.value, latest.timestamp);
    }

    function setThreshold(string memory sensorType, uint256 newThreshold) public {
        thresholds[sensorType] = newThreshold;
    }

    function getThreshold(string memory sensorType) public view returns (uint256) {
        return thresholds[sensorType];
    }
}
