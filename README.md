# Flatpak UI

This is a personal project. Please be gentle. ^\_^

## Requirements

Install `tkinter` with you package manager.

Fedora:

```sh
dnf install python3-tkinter
```

Ubuntu:

```sh
sudo apt install python3-tkinter
```

## Usage

It's up to you. As for my preference, I create a `.config/cmd` folder and add a bash script that will call the application. I then create a symbolic link and put it inside `/usr/bin` to be availabe globally.

Ex:

flatpak-ui.sh

```sh
#!/bin/bash

python3 ${directory_of_the_project}/main.py

```
