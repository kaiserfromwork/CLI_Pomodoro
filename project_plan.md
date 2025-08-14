# CLI Pomodoro

---

### **Project Plan: CLI Pomodoro**

Project Objective:

To create a Pomodoro Application that runs on CLI.

---

### **1. Scope and Goals**

**Minimum Viable Product (MVP):**

- A command-line pomodoro that runs for a duration set by the user
- A visual countdown of the time left
- A simple notification when timer reaches zero
- A visual countdown of break time before next focus time

**Future Features:**

- A Custom notification that randomly select from a pre-defined list of encouraging quotes to be displayed to the user at the end of the work/break
- A option for longer breaks after 2 short breaks

---

### **2. Research and Design**

**Technology Stack:**

- **Language:** Python
- **Libraries/Tools:**
    - argparse (for command-line arguments)
    - time, sys (built-in for timing and output control)
    - `CHECK NOTIFICAITON TOOL`  (for notifications)
    - rich (for customising terminal output)

**Interface Design (User Experience):**

- **Command Structure:**
    - Default:
        - python pomodoro.py
    - With Arguments:
        - python [pomodoro.py](http://pomodoro.py) —work 25 —break 5
- **Countdown Display:**
    - Timer:
        - Work: 24:55 / Break: 4:55
    - Bar:
        - [##########——————] 50%
- **Notifications:**
    - A notification message pop-up

---

### **3. Development Plan**

**Environment Control:**

- Setup a Virtual Environment for initial dependencies

**Version Control:**

- GitHub
- Workflow: Create branches for new features and merge them to main development branch after they have been tested.

**Task List :**

- **To Do (MVP):**
    - Create a basic python script that counts down based on a timer
    - Display countdown output to the CLI
    - Add command-line argument passing
    - Allow user to customize work/break time by taking passed arguments
    - Setup rich for a custom cli output

---

### **4. Execution and Testing**

**Development Process:**

- Build the project incrementally, one feature at time until the MVP
- Perform refactoring to code base to improve code structure and clarity
- Automated Quality Checks:
    - Github Actions for Continous Integration
        - Testing:
            - Use pytest for unit testing core functions
            - Use coverage.py to check how much of the code is being tested
        - Linting:
            - Use ruff to enforce consistent formatting and linting to prevent potential erros
        - Type Checking:
            - Use pyright for type checking for fast performance

---

### **5. Documentation and Deployment**

- README.md
    - **Project Title:** CLI Pomodoro
    - **Description:** A Pomodoro application that runs on the terminal. Focus and break times are set by user which is notified by a pop-up message once the timer reaches zero.
    - **Installation:**
    - **Usage:**
    - **Features:**
    - **Future Plans:**

**Deployment:**

- GitHub Repository
