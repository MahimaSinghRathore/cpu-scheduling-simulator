from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

def calculate_response_time(ct, arrival, burst):
    rt = []
    for i in range(len(arrival)):
        rt.append(ct[i] - arrival[i] - burst[i] + burst[i])
    return rt


def fcfs(arrival, burst):
    n = len(arrival)
    processes = list(enumerate(zip(arrival, burst)))  
    processes.sort(key=lambda x: x[1][0])  

    ct, tat, wt, rt = [0]*n, [0]*n, [0]*n, [0]*n
    time = 0

    for idx, (arr, bur) in processes:
        time = max(time, arr)
        time += bur
        ct[idx] = time
        tat[idx] = ct[idx] - arr
        wt[idx] = tat[idx] - bur
        rt[idx] = wt[idx]  

    return ct, tat, wt, rt



def sjf(arrival, burst):
    n = len(arrival)
    completed = 0
    time = 0
    visited = [False]*n
    ct, tat, wt, rt = [0]*n, [0]*n, [0]*n, [0]*n

    while completed < n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if arrival[i] <= time and not visited[i] and burst[i] < min_bt:
                min_bt = burst[i]
                idx = i
        if idx == -1:
            time += 1
            continue
        visited[idx] = True
        rt[idx] = time - arrival[idx]
        time += burst[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - arrival[idx]
        wt[idx] = tat[idx] - burst[idx]
        completed += 1
    return ct, tat, wt, rt


def priority_scheduling(arrival, burst, priority):
    n = len(arrival)
    completed = 0
    time = 0
    visited = [False]*n
    ct, tat, wt, rt = [0]*n, [0]*n, [0]*n, [0]*n

    while completed < n:
        idx = -1
        max_pri = float('inf')
        for i in range(n):
            if arrival[i] <= time and not visited[i] and priority[i] < max_pri:
                max_pri = priority[i]
                idx = i
        if idx == -1:
            time += 1
            continue
        visited[idx] = True
        rt[idx] = time - arrival[idx]
        time += burst[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - arrival[idx]
        wt[idx] = tat[idx] - burst[idx]
        completed += 1
    return ct, tat, wt, rt



def round_robin(arrival, burst, quantum):
    n = len(arrival)
    remaining = burst[:]
    ct = [0] * n
    rt = [-1] * n
    wt = [0] * n
    tat = [0] * n

    processes = list(enumerate(zip(arrival, burst)))  
    processes.sort(key=lambda x: x[1][0])  
    arrival = [p[1][0] for p in processes]
    burst = [p[1][1] for p in processes]
    index_map = {i: orig_i for i, (orig_i, _) in enumerate(processes)}

    time = 0
    queue = deque()
    visited = [False] * n
    i = 0  

    while i < n or queue:
        while i < n and arrival[i] <= time:
            queue.append(i)
            visited[i] = True
            i += 1

        if not queue:
            time = arrival[i]
            continue

        curr = queue.popleft()
        if rt[curr] == -1:
            rt[curr] = time - arrival[curr]

        run_time = min(quantum, remaining[curr])
        time += run_time
        remaining[curr] -= run_time

       
        while i < n and arrival[i] <= time:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            i += 1

        if remaining[curr] > 0:
            queue.append(curr)
        else:
            ct[curr] = time
            tat[curr] = ct[curr] - arrival[curr]
            wt[curr] = tat[curr] - burst[curr]

   
    ct_final = [0] * n
    tat_final = [0] * n
    wt_final = [0] * n
    rt_final = [0] * n
    for i in range(n):
        orig_i = index_map[i]
        ct_final[orig_i] = ct[i]
        tat_final[orig_i] = tat[i]
        wt_final[orig_i] = wt[i]
        rt_final[orig_i] = rt[i]

    return ct_final, tat_final, wt_final, rt_final


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            arrival = list(map(int, request.form["arrival"].split(",")))
            burst = list(map(int, request.form["burst"].split(",")))
            algorithm = request.form["algorithm"]
            priority = list(map(int, request.form.get("priority", "").split(","))) if "Priority" in algorithm else []
            quantum = int(request.form.get("quantum", 0)) if "RR" in algorithm else 0

            if algorithm == "FCFS":
                ct, tat, wt, rt = fcfs(arrival, burst)
            elif algorithm == "SJF":
                ct, tat, wt, rt = sjf(arrival, burst)
            elif algorithm == "Priority":
                ct, tat, wt, rt = priority_scheduling(arrival, burst, priority)
            elif algorithm == "RR":
                ct, tat, wt, rt = round_robin(arrival, burst, quantum)

            processes = list(range(1, len(arrival)+1))
            result = list(zip(processes, arrival, burst, ct, tat, wt, rt))

            return render_template("index.html", result=result, algorithm=algorithm)

        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
