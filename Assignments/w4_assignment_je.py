import tkinter as tk
from tkinter import ttk
import time

Root=tk.Tk()
Root.title("Progress")

steps=["step1", "step2", "step3", "step4", "step5", "step6", "step7", "step8", "step9", "Finish"]
progress=ttk.Progressbar(Root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

status_label=tk.Label(Root, text="READY")
status_label.pack()

percent=["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

percent_label=tk.Label(Root, text="PERCENT")
percent_label.pack()

progress["maximum"]=len(steps)

def run_step():
    for i in range(len(steps)):
        status_label.config(text=steps[i])
        progress.step(1)
        percent_label.config(text=percent[i])
        Root.update()
        time.sleep(1)

start_button=tk.Button(Root, text="START", command=run_step)
start_button.pack(pady=10)

Root.mainloop()