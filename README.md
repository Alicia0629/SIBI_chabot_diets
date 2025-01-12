# Project for a Chatbot for Personalized Dietary Recommendations

SIBI_chatbot_diets is a chatbot designed to provide personalized dietary recommendations based on the individual needs of each user. The system uses Python and various technologies like Docker, recipe databases, and the Cohere API to create an interactive and tailored experience. By receiving information about characteristics such as weight, height, allergies, and personal goals (e.g., losing weight, gaining muscle mass, or maintaining health), the chatbot offers food suggestions adjusted to each profile.
## Table of Contents
1. [Requirements](#Requirements)
   - [Docker](#docker)
   - [Makefile](#makefile)
2. [Usage Instructions](#Usage_Instructions)

---

## Requirements

### Docker
Docker must be installed on your system.

- **Windows**: Follow this guide to install Docker:  
  https://docs.docker.com/desktop/setup/install/windows-install/

- **Linux**: Use this tutorial for your distribution:  
  https://docs.docker.com/engine/install/

### Makefile
A Makefile is used to simplify Docker execution. Make sure you have make installed. Below are the instructions based on your operating system:

#### On Windows
If you don't have **Chocolatey** (choco) installed, run the following command in PowerShell as administrator:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Then, install make with this command:
```
choco install make
```


#### On Linux
In most distributions, `make` is already installed. If not, use one of these commands based on your distribution:

- **Debian/Ubuntu**:
```
sudo apt update
sudo apt install make
```

- **Red Hat/Fedora**:
```
sudo dnf install make
```

- **Arch Linux**:
```
sudo pacman -S make
```


---


## Usage Instructions

1. Open PowerShell as Administrator if you're on Windows, or a terminal if you're on Linux.

2. Clone the repository

```
git clone https://github.com/Alicia0629/SIBI_chabot_diets.git
```
Or manually download the repository.

3. Go to the project directory
```
cd SIBI_chabot_diets
cd project
```

4. If you're on Windows, open Docker Desktop

5. Start the build process **(it may take up to two hours)**
- **Windows**:
```
make build
```

- **Linux**:
```
sudo make build
```


6. Run the application
- **Windows**:
```
make run
```

- **Linux**:
```
sudo make run
```
