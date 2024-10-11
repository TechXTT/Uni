let previousSensorData = []; // Store previous data for comparison

// Fetch sensor data from the API
async function fetchSensorData() {
    try {
        const response = await fetch('/api/sensor_data');
        if (!response.ok) {
            throw new Error('Failed to fetch sensor data');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching sensor data:', error);
        return [];
    }
}

// Function to check if the new data is different from the previous data
function isDataDifferent(newData) {
    return JSON.stringify(newData) !== JSON.stringify(previousSensorData);
}

// Function to group sensor data by sensor_id
function groupBySensor(data) {
    const groupedData = {};
    data.forEach(entry => {
        if (!groupedData[entry.sensor_id]) {
            groupedData[entry.sensor_id] = [];
        }
        groupedData[entry.sensor_id].push(entry);
    });
    return groupedData;
}

// Generate colors for chart lines
function generateColor(index) {
    const colors = [
        'rgba(255, 99, 132, 1)', 
        'rgba(54, 162, 235, 1)', 
        'rgba(75, 192, 192, 1)', 
        'rgba(153, 102, 255, 1)', 
        'rgba(255, 159, 64, 1)', 
        'rgba(255, 206, 86, 1)'
    ];
    return colors[index % colors.length];
}

// Plot each sensor's data in separate charts
async function plotSensorData() {
    const sensorData = await fetchSensorData();

    if (!isDataDifferent(sensorData)) {
        console.log('No new data, skipping chart update');
        return;
    }

    previousSensorData = sensorData; // Update previous data

    const groupedData = groupBySensor(sensorData);

    // Data structures for temperature, humidity, and light level charts
    const temperatureDatasets = [];
    const humidityDatasets = [];
    const lightLevelDatasets = [];

    // Loop through each sensor and create datasets for each graph
    Object.keys(groupedData).forEach((sensorId, index) => {
        const sensorSpecificData = groupedData[sensorId];
        
        const color = generateColor(index);

        // Temperature dataset for each sensor with x (timestamps) and y (values)
        temperatureDatasets.push({
            label: `Sensor ${sensorId}`,
            data: sensorSpecificData.map(data => ({
                x: data.timestamp,
                y: data.temperature
            })), // Array of {x: timestamp, y: temperature}
            borderColor: color,
            backgroundColor: `${color}33`,
            fill: false
        });

        // Humidity dataset for each sensor with x (timestamps) and y (values)
        humidityDatasets.push({
            label: `Sensor ${sensorId}`,
            data: sensorSpecificData.map(data => ({
                x: data.timestamp,
                y: data.humidity
            })), // Array of {x: timestamp, y: humidity}
            borderColor: color,
            backgroundColor: `${color}33`,
            fill: false
        });

        // Light level dataset for each sensor with x (timestamps) and y (values)
        lightLevelDatasets.push({
            label: `Sensor ${sensorId}`,
            data: sensorSpecificData.map(data => ({
                x: data.timestamp,
                y: data.light_level
            })), // Array of {x: timestamp, y: light level}
            borderColor: color,
            backgroundColor: `${color}33`,
            fill: false
        });
    });

    console.log('Temperature data:', temperatureDatasets.map(dataset => dataset.data));

    // Create Temperature Chart
    const tempCtx = document.getElementById('temperatureChart').getContext('2d');
    new Chart(tempCtx, {
        type: 'line',
        data: {
            datasets: temperatureDatasets
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute',
                        displayFormats: {
                            minute: 'YYYY-MM-DD HH:mm'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Timestamp'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (℃)'
                    }
                }
            }
        }
    });

    // Create Humidity Chart
    const humCtx = document.getElementById('humidityChart').getContext('2d');
    new Chart(humCtx, {
        type: 'line',
        data: {
            datasets: humidityDatasets
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute',
                        displayFormats: {
                            minute: 'YYYY-MM-DD HH:mm'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Timestamp'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Humidity (%)'
                    }
                }
            }
        }
    });

    // Create Light Level Chart
    const lightCtx = document.getElementById('lightLevelChart').getContext('2d');
    new Chart(lightCtx, {
        type: 'line',
        data: {
            datasets: lightLevelDatasets
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute',
                        displayFormats: {
                            minute: 'YYYY-MM-DD HH:mm'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Timestamp'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Light Level (W/m²)'
                    }
                }
            }
        }
    });
}

// Function to populate the table
async function populateSensorTable(firstLoad) {
    const sensorData = await fetchSensorData();

    if (!isDataDifferent(sensorData) && !firstLoad) {
        console.log('No new data, skipping table update');
        return;
    }

    const tableBody = document.getElementById('sensorTableBody');
    if (!tableBody) {
        console.error('Table body element not found');
        return;
    }
    
    console.log('Populating table with new data');
    
    tableBody.innerHTML = ""; // Clear the table body

    // Populate the table rows with sensor data
    sensorData.forEach(data => {
        const row = `
            <tr>
                <td>${data.sensor_id}</td>
                <td>${data.timestamp}</td>
                <td>${data.temperature}</td>
                <td>${data.humidity}</td>
                <td>${data.light_level}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });

    // Update previousSensorData
    previousSensorData = sensorData;
}

// Set up a function to automatically refresh the data every 10 seconds
function autoRefresh(firstLoad = false) {
    plotSensorData();
    populateSensorTable(firstLoad);
    setTimeout(autoRefresh, 10000); // Refresh every 10 seconds
}

// Initial load
autoRefresh(true);