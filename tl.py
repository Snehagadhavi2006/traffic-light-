import simpy
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Constants
RED_DURATION = 40  # seconds
GREEN_DURATION = 60  # seconds
YELLOW_DURATION = 5  # seconds
SIM_TIME = 3600  # 1 hour
CAR_ARRIVAL_RATE = 10  # cars per minute (Poisson)

# Metrics
waiting_times = []
car_pass_times = []

class TrafficLight:
    def __init__(self, env):
        self.env = env
        self.green_light = env.event()
        self.red_light = env.event()
        self.action = env.process(self.run())

    def run(self):
        while True:
            # Green light
            self.green_light.succeed()  # Trigger green light
            self.green_light = self.env.event()  # Reset event
            yield self.env.timeout(GREEN_DURATION)

            # Yellow light
            yield self.env.timeout(YELLOW_DURATION)

            # Red light
            self.red_light.succeed()  # Trigger red light
            self.red_light = self.env.event()  # Reset event
            yield self.env.timeout(RED_DURATION)

def car(env, name, traffic_light):
    arrival_time = env.now
    yield traffic_light.green_light  # Wait for green light
    pass_time = env.now
    car_pass_times.append(pass_time)
    waiting_time = pass_time - arrival_time
    waiting_times.append(waiting_time)

def car_generator(env, traffic_light):
    car_id = 0
    while True:
        yield env.timeout(random.expovariate(CAR_ARRIVAL_RATE / 60.0))  # Poisson arrivals
        car_id += 1
        env.process(car(env, f"Car_{car_id}", traffic_light))

# Simulation
env = simpy.Environment()
traffic_light = TrafficLight(env)
env.process(car_generator(env, traffic_light))

env.run(until=SIM_TIME)

# Results
print("\nSimulation Results:")
print(f"Average waiting time: {statistics.mean(waiting_times):.2f} seconds")
print(f"Maximum waiting time: {max(waiting_times):.2f} seconds")
print(f"Number of cars passed: {len(waiting_times)}")

# Visualization: Waiting Time Distribution
plt.hist(waiting_times, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Distribution of Waiting Times")
plt.xlabel("Waiting Time (seconds)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization: Cumulative Cars Passed Over Time
cumulative_cars = np.cumsum([1] * len(car_pass_times))
time_points = car_pass_times

plt.plot(time_points, cumulative_cars, color='green', linewidth=2)
plt.title("Cumulative Cars Passed Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Cumulative Cars Passed")
plt.grid()
plt.show()

# Visualization: Traffic Light State Over Time
time = np.arange(0, SIM_TIME)
states = ['Green' if (t // (GREEN_DURATION + RED_DURATION + YELLOW_DURATION)) % 2 == 0 
          else 'Red' for t in time]

state_colors = {'Green': 'green', 'Red': 'red', 'Yellow': 'yellow'}
color_sequence = [state_colors[state] for state in states]

plt.figure(figsize=(10, 2))
plt.scatter(time, [1] * len(time), c=color_sequence, s=2)
plt.title("Traffic Light States Over Time")
plt.yticks([])
plt.xlabel("Time (seconds)")
plt.show()

# Visualization: Queue Length Over Time
queue_lengths = [sum(arrival <= t and t < pass_time for arrival, pass_time in zip(car_pass_times, car_pass_times)) 
                 for t in time]

plt.plot(time, queue_lengths, color='orange', linewidth=2)
plt.title("Queue Length Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Queue Length (cars)")
plt.grid()
plt.show()
