import tkinter as tk

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Not Defteri")

        self.text_area = tk.Text(master)
        self.text_area.pack()

        self.save_button = tk.Button(master, text="Kaydet", command=self.save)
        self.save_button.pack()

    def save(self):
        with open("Yazılan_not.txt", "w") as f:
            f.write(self.text_area.get("1.0", "end"))

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
