# Imports
from tkinter import *
from tkinter import ttk

# GUI
tk = Tk()
nosaukums = tk.title("varianti un salīdzinājums ar vārdnīcu")
galvenaisLogs = ttk.Frame(tk, padding="3 3 12 12")
galvenaisLogs.grid(column=0, row=0, sticky=(N, W, E, S))
tk.columnconfigure(0, weight=1)
tk.rowconfigure(0, weight=1)

uzaicinājums = ttk.Label(galvenaisLogs, text="Ievadi velns zin ko -> Lūdzu:").grid(column=1, row=1)
uzaicinājumsIevade = ttk.Entry(galvenaisLogs,).grid(column=2, row=1)
nuAiziet = ttk.Button(galvenaisLogs, text="Aiziet!").grid(column=3, row=1)
#logsNr1 = ttk.Frame(galvenaisLogs, height=100).grid(row=1, columnspan=3)

#  Saraksts -> с перестоновкой (varbūt ar rindu numerāciju)


# Vārdnīca -> salīdzināt ar katru variantu no saraksta


# Beigas
tk.mainloop()