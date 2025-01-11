# Proyecto de un Chatbot para Recomendaciones Dietéticas Personalizadas

SIBI_chatbot_diets es un chatbot diseñado para proporcionar recomendaciones dietéticas personalizadas, basado en las necesidades individuales de cada usuario. El sistema utiliza Python y diversas tecnologías como Docker, bases de datos de recetas y la API de Cohere para crear una experiencia interactiva y adaptada. Al recibir información sobre características como peso, altura, alergias y objetivos personales (adelgazar, ganar masa muscular o mantener la salud), el chatbot ofrece sugerencias alimenticias ajustadas a cada perfil.

## Índice
1. [Requisitos](#requisitos)
   - [Docker](#docker)
   - [Makefile](#makefile)
2. [Instrucciones de Uso](#instrucciones-de-uso)

---

## Requisitos

### Docker
Es necesario tener Docker instalado en tu sistema.

- **Windows**: Sigue esta guía para instalar Docker:  
  https://docs.docker.com/desktop/setup/install/windows-install/

- **Linux**: Usa este tutorial según tu distribución:  
  https://docs.docker.com/engine/install/

### Makefile
Usamos un archivo Makefile para facilitar la ejecución de Docker. Asegúrate de tener `make` instalado. A continuación, se indican las instrucciones según tu sistema operativo:

#### En Windows
Si no tienes **Chocolatey** (choco) instalado, ejecuta el siguiente comando en PowerShell como administrador:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Luego instala `make` con el siguiente comando:
```
choco install make
```


#### En Linux
En la mayoría de distribuciones, `make` ya está instalado. Si no es así, usa uno de estos comandos según tu distribución:

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


## Instrucciones de Uso

1. Abrir PowerShell como administrador si estás en Windows o una terminal si estás en Linux.

2. Clona el repositorio:
```
git clone https://github.com/Alicia0629/SIBI_chabot_diets.git
```
O descarga manualmente el repositorio.

3. Ir al directorio del proyecto
```
cd SIBI_chabot_diets
cd project
```

4. Si tienes windows abre Docker Desktop

5. Inicia el proceso de construcción **(puede tomar dos horas):**
- **Windows**:
```
make build
```

- **Linux**:
```
sudo make build
```


6. Ejecuta la aplicación:
- **Debian/Ubuntu**:
- **Windows**:
```
make run
```

- **Linux**:
```
sudo make run
```

