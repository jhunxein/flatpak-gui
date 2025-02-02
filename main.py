from tkinter import Tk, N, W, E, S
from tkinter import ttk

from controller import Controller


class App:
    """
    The startup class that will control the application.

    Requirements:
        - dimensions should be fixed: width = 800, height = 600, minwidth= 500, minheight = 500
        - centered
        - scrollable
    """

    MINHEIGHT = 500
    MINWIDTH = 500
    HEIGHT = 600
    WIDTH = 800

    def __init__(self):
        self.rows = 0
        self.apps = {}
        self.root = Tk()
        self.controller = Controller()
        self._start()

    def _configure(self):
        self.root.title("Hello")
        self.mainframe = ttk.Frame(self.root, padding="3 3 3 3")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=3, minsize=self.MINHEIGHT)
        self.root.rowconfigure(0, weight=1, minsize=self.MINWIDTH)

    def _bind_events(self):
        pass

    def _create_list(self):
        try:
            self.apps = self.controller.get_installed_apps()
            for app in self.apps:
                ttk.Button(
                    self.mainframe,
                    width=50,
                    text=f"{app['name']} - {app['version']}",
                    command=lambda app_id=app["app_id"]: self.controller.launch_app(
                        app_id
                    ),
                ).grid(column=0, row=self.rows, sticky=W)
                self.rows += 1
        except Exception as e:
            raise e

    def _add_padding(self):
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def _run_selected_app(self):
        try:
            pass
        except Exception as e:
            raise e
        pass

    def _start(self):
        self._configure()
        self._create_list()
        self._add_padding()
        # self._bind_events()
        self.root.mainloop()


if __name__ == "__main__":
    App()
