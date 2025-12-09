# PYTHON TASK TRACKER CLI

A command-line interface (CLI) application built in Python for managing a simple to-do list, storing data in a local JSON file. 

## 🚀 Getting Started

Follow these steps to set up and run the `task-cli` application.

### Prerequisites

You need **Python 3.x** installed on your system.

### Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/outnova/python-task-tracker.git
    cd python-task-tracker
    ```

2.  **Create and Activate the Virtual Environment**

    It's strongly recommended to use a virtual environment (`venv`) to isolate project dependencies.

    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate the environment (Linux/macOS)
    source venv/bin/activate

    # Activate the environment (Windows PowerShell)
    # .\venv\Scripts\Activate.ps1
    ```

3.  **Install Dependencies**

    Since this project uses only standard Python libraries, your `requirements.txt` is likely empty. However, we run the command as a best practice:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install the CLI as a System Command**

    Install the project in **editable mode** using `setup.py`. This creates the `task-cli` command within your active virtual environment.

    ```bash
    pip install -e .
    ```

---

## ⚙️ Usage

Once the installation is complete, you can use the `task-cli` command.

### Running the Application

Start the interactive CLI loop:

```bash
task-cli
```

---

## Español

# PYTHON TASK TRACKER CLI

Una aplicación de interfaz de línea de comandos (CLI) construida en Python para gestionar una lista simple de tareas (to-do list), almacenando los datos en un archivo JSON local.

## 🚀 Inicio Rápido

Sigue estos pasos para configurar y ejecutar la aplicación `task-cli`.

### Requisitos

Necesitas tener **Python 3.x** instalado en tu sistema.

### Instalación

1.  **Clonar el Repositorio**

    ```bash
    git clone https://github.com/outnova/python-task-tracker.git
    cd python-task-tracker
    ```

2.  **Crear y Activar el Entorno Virtual**

    Se recomienda fuertemente usar un entorno virtual (`venv`) para aislar las dependencias del proyecto.

    ```bash
    # Crear el entorno virtual
    python -m venv venv

    # Activar el entorno (Linux/macOS)
    source venv/bin/activate

    # Activar el entorno (Windows PowerShell)
    # .\venv\Scripts\Activate.ps1
    ```

3.  **Instalar Dependencias**

    Aunque este proyecto solo usa librerías estándar de Python, ejecutamos el comando como buena práctica:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Instalar la CLI como un Comando de Sistema**

    Instala el proyecto en **modo editable** usando `setup.py`. Esto crea el comando `task-cli` dentro de tu entorno virtual activo.

    ```bash
    pip install -e .
    ```

---

## ⚙️ Uso

Una vez completada la instalación, puedes usar el comando `task-cli`.

### Ejecutar la Aplicación

Inicia el bucle interactivo de la CLI:

```bash
task-cli
```

https://roadmap.sh/projects/task-tracker