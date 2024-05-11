import random


class blocks:
    def __init__(self, root):
        self.root = root

    def block(self):
        nx, ny = 0, 0
        for i in range(100):
            blk = tk.Button(height=3, width=3)
            blk.place(x=nx, y=ny)
            self.root.update()
            nx += blk.winfo_width()
            print(nx, self.root.winfo_width())
            if nx >= self.root.winfo_width():
                ny += blk.winfo_height()
                nx = 0


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    root.geometry("500x500")
    b = blocks(root)
    b.block()

    root.mainloop()
