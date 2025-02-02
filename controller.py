import subprocess
from typing import Callable


class Controller:
    def get_installed_apps(self):
        cmd = "flatpak list"
        output = subprocess.run(["bash", "-c", cmd], stdout=subprocess.PIPE)
        output = output.stdout.decode("utf-8")
        apps = []
        for line in output.splitlines():
            values = line.split("\t")
            apps.append(
                {
                    "name": values[0],
                    "app_id": values[1],
                    "version": values[2],
                }
            )

        # sort apps by name in case insensitive
        apps.sort(key=lambda x: x["name"].lower())
        return apps

    def launch_app(self, app_id: str, destroy_fn: Callable):
        cmd = f"flatpak run {app_id} &"
        subprocess.run(["bash", "-c", cmd])
        destroy_fn()
