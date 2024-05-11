from PIL import ImageTk, Image
import tkinter as tk
from threading import Thread


class Home:
    def __init__(self, root, use_mgr=1):
        self.root = root
        self.root.geometry("500x700")
        self.root.configure(bg="#acfffc")
        self.root.update()

        cloud_img = Image.open(
            "C:\\Users\Home\\Documents\\Programming\\Python\\MineSweeper\\Cloud.png"
        )
        cloud_img = cloud_img.resize((100, 60), Image.Resampling.LANCZOS)
        self.cloud_img = ImageTk.PhotoImage(cloud_img)

        logo_img = Image.open(
            "C:\\Users\Home\\Documents\\Programming\\Python\\MineSweeper\\Logo.png"
        )
        logo_img = logo_img.resize((300, 150), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        if use_mgr:
            self.manager()

    def screen_width(self):
        self.root.update()
        return self.root.winfo_width()

    @staticmethod
    def movex(widget, xreset_pos, xpace=1, xreset_value=0):
        xcord, ycord = widget.winfo_x() + xpace, widget.winfo_y()
        if xcord == xreset_pos:
            xcord = xreset_value
        widget.place(x=xcord, y=ycord)

    def cloud_motion_xcord(self):
        self.root.update()
        while 1:
            for i in range(0, 6):
                if i in (2, 1):
                    continue
                widget = self.root.nametowidget(f"cloud{i}")
                self.movex(
                    widget=widget,
                    xreset_pos=self.screen_width(),
                    xreset_value=-100,
                    xpace=1,
                )
            self.root.after(50)

    def Logo(self):
        logo = tk.Label(
            self.root,
            image=self.logo_img,
            name="logo",
            bg="#acfffc",
            font="times 10 bold",
            relief="flat",
            fg="white",
        )

        logo.image = self.logo_img
        logo.place(relx=0.5, rely=0.25, anchor="center")

    def cloud_images(self):
        xcordinates = (329, -100, -100, 163, 282, 23)
        for i, xcord in enumerate(xcordinates):
            cloud_display = tk.Label(
                self.root, image=self.cloud_img, bg="#acfffc", name=f"cloud{i}"
            )
            cloud_display.img = self.cloud_img
            cloud_display.place(x=xcord, y=i * 100)

    def home_buttons(self):
        Play_btn = tk.Button(
            self.root,
            name="play",
            bg="#293241",
            width=20,
            height=2,
            font="times 10 bold",
            relief="flat",
            text="Play!",
            fg="white",
        )
        Play_btn.place(relx=0.5, rely=0.5, anchor="center")

        HowToPlay_btn = tk.Button(
            self.root,
            name="howtoplay",
            bg="#293241",
            width=20,
            height=2,
            font="times 10 bold",
            relief="flat",
            text="How to play?",
            fg="white",
        )
        HowToPlay_btn.place(relx=0.5, rely=0.6, anchor="center")

        Settings_Btn = tk.Button(
            self.root,
            name="settings",
            bg="#293241",
            width=20,
            height=2,
            font="times 10 bold",
            relief="flat",
            text="Settings",
            fg="white",
        )
        Settings_Btn.place(relx=0.5, rely=0.7, anchor="center")

    def manager(self):
        self.Logo()

        self.cloud_images()

        self.cloud_motion_thread = Thread(target=self.cloud_motion_xcord)
        self.cloud_motion_thread.start()

        self.home_buttons()


class test:
    def __init__(self):
        root = tk.Tk()
        root.title("Mine Sweeper")
        Home_Gui = Home(root=root, use_mgr=1)
        root.mainloop()


if __name__ == "__main__":
    test()
