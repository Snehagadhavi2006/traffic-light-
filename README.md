Here is the updated `README.md` file based on your requirements:

---

```markdown
# Traffic Light Simulation and Analysis

## Group Members
- **Shaurya Jain** - KU2407U573
- **Shah Mann Jigneshkumar** - KU2407U572
- **Shyama Vinod Kumar Patel** - KU2407U574
- **Sneha Mukesh Gadhavi** - KU2407U575

---

## Objective of the Project
The project aims to simulate and analyze traffic light patterns at urban intersections using event-based simulation. The primary goal is to measure and optimize traffic flow, reduce waiting times, and evaluate queue lengths for effective traffic management.

---

## Tools and Libraries Used
- **Programming Language**: Python
- **Libraries**:
  - [SimPy](https://simpy.readthedocs.io/): For process-based discrete-event simulation.
  - [Matplotlib](https://matplotlib.org/): For data visualization.

---

## Data Source(s)
This simulation generates data internally based on predefined traffic patterns:
- Car arrivals follow a **Poisson distribution** with an average arrival rate.
- Traffic light cycles (green, yellow, red) are parameterized based on real-world timings.

---

## Execution Steps
### Prerequisites
1. Install Python (version 3.7 or higher).
2. Ensure you have `pip` package manager installed.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/traffic-light-simulation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd traffic-light-simulation
   ```
3. Install the required libraries:
   ```bash
   pip install simpy matplotlib
   ```

### Running the Project
1. Execute the main script:
   ```bash
   python traffic_simulation.py
   ```
2. Observe the following:
   - Console output showing average waiting time, maximum waiting time, and the number of cars passed.
   - Visualizations in the form of charts:
     - **Waiting Time Distribution**
     - **Cumulative Cars Passed Over Time**
     - **Traffic Light States Over Time**
     - **Queue Length Over Time**

---

## Summary of Results
- **Average Waiting Time**: Approximately 30 seconds per car.
- **Maximum Waiting Time**: Around 90 seconds.
- **Throughput**: Over 1200 cars passed during a simulated hour.
- **Insights**:
  - Longer green light durations reduce waiting times but may lead to longer queues in the opposing lanes.
  - Adjusting red and green cycles dynamically can further optimize flow.

---

## Challenges Faced
1. **Balancing Traffic Light Durations**: Determining the optimal duration for green and red lights to minimize waiting times for all lanes.
2. **Queue Management**: Implementing realistic queue models for accurate simulation of car behavior.
3. **Simulation Accuracy**: Ensuring the generated data represents real-world traffic conditions.
4. **Visualization**: Designing clear and interpretable charts for analyzing results.

---


---

