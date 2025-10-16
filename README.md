# monte-carlo-simulation
Monte Carlo simulation via streamlit  
  
Also known as the Monte Carlo Method or a multiple probability simulation, Monte Carlo Simulation is a mathematical technique that is used to estimate the possible outcomes of an uncertain event. The Monte Carlo Method was invented by John von Neumann and Stanislaw Ulam during World War II to improve decision making under uncertain conditions. It was named after a well-known casino town, called Monaco, since the element of chance is core to the modeling approach, similar to a game of roulette.


## Setup
https://docs.streamlit.io/get-started/installation/command-line
cd myproject
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
streamlit hello << to test if setup is ok

## To run locally
cd \repos\monte-carlo-simulation
.venv\Scripts\Activate.ps1
streamlit run monte_carlo/core.py

# 🧠 Project Structure Overview

This layout is optimized for clarity, modularity, and ADHD-friendly development. Each part has a clear role and purpose.

---

## 📁 Top-Level Files

| File               | Purpose                                         | Usage                                      |
|--------------------|-------------------------------------------------|--------------------------------------------|
| `README.md`        | Project intro and usage guide                   | Describe what the project does and how to run it |
| `LICENSE`          | Legal terms for usage                           | Choose a license (e.g., MIT, GPL)          |
| `setup.py`         | Installer script for packaging                  | Defines how to install your project via pip |
| `requirements.txt` | Dependency list                                 | Install with `pip install -r requirements.txt` |
| `.gitignore`       | Git cleanup rules                               | Prevents committing unwanted files (e.g., `.venv`, logs) |

---

## 📦 `project_name/` — Main Code Package

| File/Folder               | Purpose                                         | Usage                                      |
|---------------------------|-------------------------------------------------|--------------------------------------------|
| `__init__.py`             | Marks this folder as a Python package           | Can be empty or define exports             |
| `core.py`                 | Main logic (e.g., Black-Scholes, Monte Carlo)  | Core simulation and pricing functions      |
| `helpers.py`              | Utility functions                              | Reusable tools like math helpers           |
| `subpackage/`             | Optional expansion module                      | Organize advanced or specialized logic     |
| `subpackage/__init__.py` | Same as above                                   | Enables importing `subpackage.submodule`   |
| `subpackage/submodule.py`| Specialized logic                               | e.g., exotic options, plotting, etc.       |

---

## 🧪 `tests/` — Automated Testing Suite

| File               | Purpose                                         | Usage                                      |
|--------------------|-------------------------------------------------|--------------------------------------------|
| `__init__.py`      | Marks this folder as a test package             | Usually empty                              |
| `test_core.py`     | Tests for `core.py`                             | Use `pytest` or `unittest` to run          |
| `test_helpers.py`  | Tests for `helpers.py`                          | Write test cases for each helper function  |

Run tests with:
```bash
pytest tests/