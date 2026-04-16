import tkinter as tk
import random
import time

# ================= WINDOW =================
root = tk.Tk()
root.title("Simulasi PRO - Sistem Terdistribusi")
root.geometry("900x600")

# ================= CANVAS =================
canvas = tk.Canvas(root, width=850, height=300, bg="white")
canvas.pack(pady=10)

# Nodes
clients = []
for i in range(3):
    c = canvas.create_rectangle(50, 50 + i*80, 130, 100 + i*80, fill="lightblue")
    canvas.create_text(90, 40 + i*80, text=f"Client {i+1}")
    clients.append(c)

server = canvas.create_rectangle(350, 100, 450, 160, fill="lightgreen")
canvas.create_text(400, 90, text="Server")

broker = canvas.create_rectangle(650, 100, 750, 160, fill="orange")
canvas.create_text(700, 90, text="Broker")

subscribers = []
for i in range(2):
    s = canvas.create_rectangle(350, 200 + i*50, 450, 240 + i*50, fill="pink")
    canvas.create_text(400, 190 + i*50, text=f"Sub {i+1}")
    subscribers.append(s)

# ================= LOG =================
log = tk.Text(root, height=10, width=100)
log.pack(pady=10)

# ================= INPUT =================
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# ================= SPEED CONTROL =================
speed_scale = tk.Scale(root, from_=1, to=5, orient="horizontal", label="Speed (1=Slow, 5=Fast)")
speed_scale.set(3)
speed_scale.pack()

# ================= FUNCTIONS =================
def log_msg(msg):
    log.insert(tk.END, msg + "\n")
    log.see(tk.END)

def animate_message(x1, y1, x2, y2, color="black"):
    msg = canvas.create_oval(x1, y1, x1+10, y1+10, fill=color)

    steps = 20
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps

    def move(step=0):
        if step < steps:
            canvas.move(msg, dx, dy)
            root.after(int(100 / speed_scale.get()), lambda: move(step+1))
        else:
            canvas.delete(msg)

    move()

# ---------- REQUEST RESPONSE ----------
def request_response():
    pesan = entry.get() or "Hello Server"
    log_msg("\n=== REQUEST-RESPONSE ===")

    client_index = random.randint(0, 2)
    log_msg(f"Client {client_index+1} kirim: {pesan}")

    start = time.time()

    # animasi ke server
    animate_message(130, 75 + client_index*80, 350, 120, "blue")

    def process():
        log_msg("Server memproses...")

    def response():
        animate_message(350, 120, 130, 75 + client_index*80, "green")
        latency = round((time.time() - start)*1000, 2)
        log_msg(f"Response diterima (latency: {latency} ms)")

    root.after(800, process)
    root.after(1500, response)

# ---------- PUBLISH SUBSCRIBE ----------
def publish_subscribe():
    pesan = entry.get() or "Hello All"
    log_msg("\n=== PUBLISH-SUBSCRIBE ===")

    client_index = random.randint(0, 2)
    log_msg(f"Client {client_index+1} publish: {pesan}")

    start = time.time()

    # ke broker
    animate_message(130, 75 + client_index*80, 650, 120, "purple")

    def distribute():
        log_msg("Broker mendistribusikan...")

        for i in range(len(subscribers)):
            animate_message(650, 120, 400, 220 + i*50, "red")
            log_msg(f"Subscriber {i+1} menerima")

        latency = round((time.time() - start)*1000, 2)
        log_msg(f"Distribusi selesai (latency: {latency} ms)")

    root.after(1200, distribute)

# ---------- RESET ----------
def reset():
    canvas.delete("all")
    log.delete(1.0, tk.END)
    root.destroy()

# ---------- PERBANDINGAN ----------
def perbandingan():
    log_msg("\n=== ANALISIS ===")
    log_msg("Request-Response:")
    log_msg("- Cepat untuk 1 lawan 1")
    log_msg("- Tidak efisien untuk banyak client")

    log_msg("\nPublish-Subscribe:")
    log_msg("- Efisien untuk broadcast")
    log_msg("- Lebih scalable")

# ================= BUTTON =================
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Request-Response", command=request_response, width=20).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Publish-Subscribe", command=publish_subscribe, width=20).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Perbandingan", command=perbandingan, width=20).grid(row=0, column=2, padx=5)

# ================= RUN =================
root.mainloop()