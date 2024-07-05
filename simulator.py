import random
import time
import json
import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge
from threading import Thread
 
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
# Initialize Flask app
app = Flask(__name__)
metrics = PrometheusMetrics(app)
 
# Define Prometheus gauges
speed_metric = Gauge(
    'car_board_speed', 'Current speed of the car board'
)
battery_level_metric = Gauge(
    'car_board_battery_level', 'Current battery level of the car board'
)
engine_temp_metric = Gauge(
    'car_board_engine_temp', 'Current engine temperature of the car board'
)
 
def simulate_car_board():
    
    while True:
        try:
            # Simulate data
            speed = random.uniform(10, 120)
            battery_level = random.uniform(30, 100)
            engine_temp = random.uniform(50, 120)
 
            # Log the simulated data
            data = {
                'speed': speed,
                'battery_level': battery_level,
                'engine_temp': engine_temp
            }
            logger.info(json.dumps(data))
 
            # Update Prometheus metrics
            speed_metric.set(speed)
            battery_level_metric.set(battery_level)
            engine_temp_metric.set(engine_temp)
 
            time.sleep(5)
        except Exception as e:
            logger.error(f"Error in simulate_car_board: {e}")
    
 
@app.route('/')
def index():
    return "Car board simulator is running."
 
if __name__ == "__main__":
    # Start the simulation in a separate thread
    simulation_thread = Thread(target=simulate_car_board)
    simulation_thread.daemon = True
    simulation_thread.start()
 
    # Run the Flask application
    app.run(host='0.0.0.0', port=8080)

