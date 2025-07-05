# 🖥️ CPU Scheduling Simulator

A simple **web-based tool** to simulate and compare classic **CPU Scheduling Algorithms**:  
**FCFS**, **SJF**, **Priority**, **Round Robin**.

## ✅ Features

- Supports **4 algorithms**
- Takes **Arrival Time**, **Burst Time**, **Priority**, **Time Quantum**
- Shows:
  - Completion Time (CT)
  - Turnaround Time (TAT)
  - Waiting Time (WT)
  - Response Time (RT)
- Displays results in a clean table
- Runs locally in any browser

---

## 🗂️ Tech Used

- **Python + Flask** (backend)
- **HTML/CSS + Bootstrap** (frontend)
- **Jinja2** (templating)

---

## 📂 Structure

cpu-scheduling-simulator/
├── app.py
├── templates/index.html
├── requirements.txt
├── README.md


## 🚀 How to Run

# Clone
git clone https://github.com/yourusername/cpu-scheduling-simulator.git
cd cpu-scheduling-simulator

# Install
pip install Flask

# Run
python app.py
Open http://127.0.0.1:5000/ in your browser.

📌 Future Ideas

Gantt Chart view
Preemptive SJF & Priority
Export as PDF/CSV
