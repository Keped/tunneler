#!/usr/bin/python3
import os, subprocess, threading, random, time  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter as tk
from pyngrok import ngrok
import pyqrcode


class QRCodeLabel(tk.Label):
    def __init__(self, parent, qr_data):
        super().__init__(parent)
        print('QRCodeLabel("{}")'.format(qr_data))
        qrcode = pyqrcode.create(qr_data)
        tmp_png_file = "./tmp_code.png"
        qrcode.png(tmp_png_file, scale=8)
        time.sleep(2)
        self.image = tk.PhotoImage(file=tmp_png_file)
        self.configure(image=self.image)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.pack()
        self.create_widgets()
        self.public_url = None
        self.qr_label = None
        self.generate_qr(random.choice(["You Win!", "You Lose!"]))
        
    def on_click(self):
        self.public_url = ngrok.connect(22, "tcp")
        app.text.delete("1.0", tk.END)
        app.text.insert(tk.END, '%s \n'%(self.public_url))

    def create_widgets(self):
        self.start_btn = tk.Button(self)
        self.start_btn["text"] = "Start Tunneling"
        self.start_btn["command"] = self.on_click
        self.start_btn.pack(side="top")
        self.text = tk.Text(self, fg= 'black')
        self.text.pack(side="bottom")
        self.text.insert(tk.INSERT, "Click Above to start...")

    def generate_qr(self, data):
        if self.qr_label:
            self.qr_label.destroy()
        self.qr_label = QRCodeLabel(self, data)
        self.qr_label.grid(row=1, column=0)

t = None
# def start_connection():
    
#     def do_connection():
#         app.text.delete("1.0", tk.END)
#         app.text.insert(tk.END, '%s \n'%('Trying to NGrok...\n'))
#         process = subprocess.Popen(['./ngrok', 'tcp', '22'], 
#         # process = subprocess.Popen(['ping', '-c 4', 'python.org'], 
#                            stdout=subprocess.PIPE,
#                            universal_newlines=True)

#         while True:
#             output = process.stdout.readline()
#             print(output.strip())
#             app.text.insert(tk.END, '%s \n'%(output.strip()))
#             # Do something else
#             return_code = process.poll()
#             if return_code is not None:
#                 print('RETURN CODE', return_code)
#                 # Process has finished, read rest of the output 
#                 for output in process.stdout.readlines():
#                     print(output.strip())
#                     # self.text.insert(tk.END, output.strip())
#                 break  
    
#     t = threading.Thread(target=do_connection)           
#     t.start()
root = tk.Tk()

app = Application(master=root)
app.mainloop()
