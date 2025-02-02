from tkinter import Canvas, Tk, N, W, E, S
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

    HEIGHT = 300
    WIDTH = 400
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
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # use canva for scroll support
        self.canvas = Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar_y = ttk.Scrollbar(
            self.root, orient="vertical", command=self.canvas.yview
        )
        scrollbar_y.pack(side="right", fill="both")
        # use canva as the root of the frame
        self.mainframe = ttk.Frame(
            self.canvas, padding="3 3 3 3", width=self.WIDTH, height=self.HEIGHT
        )
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.canvas.create_window((0, 0), window=self.mainframe, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar_y.set)

    def _update_idle(self):
        self.mainframe.update_idletasks()
        self.canvas.config(
            scrollregion=self.canvas.bbox("all"),
        )

    def _on_mouse_up(self, _):
        self.canvas.yview_scroll(-1, "units")

    def _on_mouse_down(self, _):
        self.canvas.yview_scroll(1, "units")

    def _bind_events(self):
        self.canvas.bind_all("<Button-4>", self._on_mouse_up)
        self.canvas.bind_all("<Button-5>", self._on_mouse_down)

    def _create_list(self):
        try:
            self.apps = self.controller.get_installed_apps()
            for app in self.apps:
                button = ttk.Button(
                    self.mainframe,
                    text=f"{app['name']} - {app['version']}",
                    command=lambda app_id=app["app_id"]: self.controller.launch_app(
                        app_id
                    ),
                )
                button.pack(pady=5, fill="x")
            self._update_idle()
        except Exception as e:
            raise e

    def _run_selected_app(self):
        try:
            pass
        except Exception as e:
            raise e
        pass

    def _start(self):
        self._configure()
        self._create_list()
        self._bind_events()
        self.root.mainloop()


if __name__ == "__main__":
    App()
