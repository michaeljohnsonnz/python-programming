# python-programming

This is the repository for all the tasks in our python programming course.

## Install

The following instructions is how I installed python3.10 on Ubuntu 20.04 LTS

### 1. Add repository

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

### 2. Install python3.10

```bash
sudo apt -y install python3.10
```

### 3. Set python3 as default

```bash
sudo nano /usr/bin/gnome-terminal
```

In the first line, change `#!/usr/bin/python3` to `#!/usr/bin/python3.8` and press `Ctrl + x` followed by `enter` to save and exit.

Note: _This will prevent terminal from failing to load after we complete the installation._

### 4. Update the default python by adding versions to an alternatives by running the below.

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
```
Now run

```bash
sudo update-alternatives --config python3
```

### 5. Fix pip and disutils errors

```bash
# Remove apt
sudo apt remove --purge python3-apt
sudo apt autoclean

# Install apt
sudo apt install python3-apt

# Install disutils
sudo apt install python3.10-distutils

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.10 get-pip.py

# Install venv
sudo apt install python3.10-venv

```

## Note

If settings stops loading then check `gnome-control-center`

```bash
# Start gnome-control-center
gnome-control-center

Command 'gnome-control-center' not found, but can be installed with:

# Install gnome-control-center
sudo apt install gnome-control-center
```

## Links

The following website helped me resolve the issues I experienced with installing python3.10 on Ubuntu 20.04 LTS
- https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux

## Author

Michael Johnson