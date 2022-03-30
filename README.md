# Python Programming

This is a repository for all the lessons in our python programming course. 

- [Python Programming](#python-programming) <!-- omit in toc -->
- [Install Python 3.10.4 with APT Package Manager](#install-python-3104-with-apt-package-manager)
  - [Install](#install)
    - [1. Add repository](#1-add-repository)
    - [2. Install python3.10](#2-install-python310)
    - [3. Update alternatives](#3-update-alternatives)
  - [Issues](#issues)
    - [Fix gnome-terminal](#fix-gnome-terminal)
    - [Fix gnome-control-center](#fix-gnome-control-center)
    - [Fix pip and disutils errors](#fix-pip-and-disutils-errors)
    - [Fix gnome-control-center](#fix-gnome-control-center-1)
    - [Conclusion](#conclusion)
- [Install Python 3.10.4 on Ubuntu from Source](#install-python-3104-on-ubuntu-from-source)
  - [Install](#install-1)
    - [1. Install dependencies](#1-install-dependencies)
    - [2. Download Python 3.10.4](#2-download-python-3104)
    - [3. Build from source](#3-build-from-source)
  - [Issues](#issues-1)
    - [Full command required](#full-command-required)
    - [Conclusion](#conclusion-1)
- [Links](#links)
- [Author](#author)

# Install Python 3.10.4 with APT Package Manager

Install the latest version of `Python 3.10.4` on `Ubuntu 20.04 LTS`. 

- [ ] `Ubuntu 20.04 LTS` 
- [ ] `Python 3.10.4`

## Install

### 1. Add repository

```bash
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt -y update
```

### 2. Install python3.10

```bash
sudo apt -y install python3.10
```

### 3. Update alternatives

Add your original version.

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
```

Add your new version.

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
```

Update config and select the version you would like to use.

```bash
sudo update-alternatives --config python3
```

## Issues

I encountered a number of issues with my operating system when configuring my environment to run Python 3.10.4

- I wasn't able to open terminal
- I wasn't able to access my system settings
- Zoom failed to exit share screen

### Fix gnome-terminal

```bash
sudo nano /usr/bin/gnome-terminal
```

In the first line, change `#!/usr/bin/python3` to `#!/usr/bin/python3.8` and press `Ctrl + x` followed by `enter` to save and exit.

Note: _This will prevent terminal from failing to load after we complete the installation._

### Fix gnome-control-center

Problem: 

### Fix pip and disutils errors

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

### Fix gnome-control-center

If settings stops loading then check `gnome-control-center`

```bash
# Try to start gnome-control-center
gnome-control-center

# If you receive the following response
Command 'gnome-control-center' not found, but can be installed with:

# Install gnome-control-center
sudo apt install gnome-control-center
```

### Conclusion

After some research I've decided this method of installation creates far too many issues than I'm comfortable with. As time is short, I'm going to try install from source. 

# Install Python 3.10.4 on Ubuntu from Source

## Install

### 1. Install dependencies

```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

### 2. Download Python 3.10.4

```bash
wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
```

Extract `Python-3.10.4`
```bash
tar -xzf Python-3.10.4.tgz
```

Change into the extracted python directory
```bash
cd Python-3.10.4 
```

### 3. Build from source

Prepare the python source code for compilation on your system
```bash
sudo ./configure --enable-optimizations
```

Use `altinstall` to prevent the compiler from overriding the default version of Python. This is recommended because a lot of programs on Ubuntu rely on this default version. I experienced a lot of issues because of this fact.
```bash
sudo make altinstall
```

## Issues

### Full command required

Python 3.10 is installed in `/usr/local/bin` so it's clearly separated from the default version installed in `/usr/bin` directory. I have to use `python3.10` command when running python scripts etc. At least my system and programs are not misbehaving anymore.

### Conclusion

It's working but I would also like to try `pyenv` when I get a chance.


# Links

The following website helped me resolve the issues I experienced with installing `Python 3.10.4` on `Ubuntu 20.04 LTS`

- https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux

# Author

- Michael Johnson