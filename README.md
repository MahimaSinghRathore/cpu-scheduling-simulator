# CPU Scheduling Simulator

CPU Scheduling Simulator is a web-based application that simulates and compares classical CPU scheduling algorithms. It allows users to enter process details and evaluate scheduling performance by calculating key metrics such as Completion Time, Turnaround Time, Waiting Time, and Response Time.

The project is built using Flask for the backend and HTML, CSS, Bootstrap, and Jinja2 for the frontend, providing an interactive interface for learning and analyzing operating system scheduling algorithms.

---

## Features

- Simulate multiple CPU scheduling algorithms
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling
- Round Robin Scheduling
- Calculate scheduling metrics including:
  - Completion Time (CT)
  - Turnaround Time (TAT)
  - Waiting Time (WT)
  - Response Time (RT)
- Responsive web interface
- Results displayed in a structured table
- Runs locally in any modern web browser

---

## Technologies Used

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- Bootstrap
- Jinja2

---

## Project Structure

```text
cpu-scheduling-simulator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

---

## Supported Scheduling Algorithms

### First Come First Serve (FCFS)

Processes are executed in the order they arrive.

### Shortest Job First (SJF)

The process with the smallest burst time is executed first.

### Priority Scheduling

Processes are executed according to their assigned priority.

### Round Robin (RR)

Each process receives a fixed time quantum in a cyclic order.

---

## Input Parameters

The simulator accepts the following process information:

- Process ID
- Arrival Time
- Burst Time
- Priority (for Priority Scheduling)
- Time Quantum (for Round Robin)

---

## Output

The simulator calculates:

- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)
- Response Time (RT)

Results are displayed in a tabular format for easy comparison.

---

## Installation

Clone the repository.

```bash
git clone https://github.com/MahimaSinghRathore/cpu-scheduling-simulator.git
```

Navigate to the project folder.

```bash
cd cpu-scheduling-simulator
```

Install the required dependency.

```bash
pip install Flask
```

---

## Running the Application

Start the Flask server.

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Applications

- Operating System Laboratory
- CPU Scheduling Demonstration
- Academic Learning
- Scheduling Algorithm Comparison
- Performance Analysis

---

## Future Enhancements

- Gantt Chart visualization
- Preemptive Shortest Job First
- Preemptive Priority Scheduling
- Export results to PDF or CSV
- Average performance metrics
- Process visualization timeline
- Dark mode support

---

## Author

**Mahima Singh**

B.Tech Computer Science Engineering

Jaypee University of Information Technology (JUIT)

GitHub: https://github.com/MahimaSinghRathore

---

## License

This project was developed for educational purposes to demonstrate CPU scheduling algorithms using Python and Flask.
