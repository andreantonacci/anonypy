from tkinter import *
from tkinter import ttk
from Cryptodome.Hash import SHA256


def anonymize():
    string = text_entry.get() # Get the value from text_entry
    hash_obj = SHA256.new(data=string.encode('utf-8'))
    # When should I update?
    hash_obj.update(b'')
    digest.set(hash_obj.hexdigest()) # Set output to digest


root = Tk()
root.title("Anonypy")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

raw_text = StringVar()
digest = StringVar()

text_entry = ttk.Entry(mainframe, width=10, textvariable=raw_text)
text_entry.grid(column=2, row=1, sticky=(W, E))
# ttk.Label(mainframe, textvariable=digest).grid(column=2, row=2, sticky=(W, E)) # Not selectable digest
output = Entry(mainframe, textvariable=digest, fg="black", bg="white", bd=0, width=64, state="readonly").grid(column=2, row=2, sticky=(W, E)) # Selectable digest
ttk.Button(mainframe, text="Anonymize", command=anonymize).grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text="String to anonymize:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Digest:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

text_entry.focus()
root.bind('<Return>', anonymize)
root.mainloop()
root.destroy()
