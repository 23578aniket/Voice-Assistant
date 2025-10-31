# ✨ Voice Assistant: Six (6)

A feature-rich, cross-platform **Voice Assistant** built in Python that integrates with system controls, web services, and a user database. Codenamed **"Six" (6)**, this project demonstrates proficiency in **voice recognition, text-to-speech, system automation,** and **database management**.

---

## 🚀 Key Features

This assistant is designed for hands-free system interaction and information retrieval, showcasing a diverse range of capabilities.

* **🎙️ Voice Activation & Recognition:** Listens for wake words like `"Assistant"` or `"Six"` and uses **Google Speech Recognition** to interpret commands.
* **👤 User Personalization (SQLite DB):** Implements a **SQLite database** to store and greet returning users by name, demonstrating fundamental database CRUD (Create, Read, Update, Delete) operations.
* **🌐 Web & Media Control:**
    * Play/Search videos on **YouTube** (`pywhatkit`).
    * Perform **Google searches** and fetch **Wikipedia** summaries.
    * Browser tab navigation (e.g., open new tab, close tab, go to next/previous tab).
* **💻 System Automation & Utilities:** Utilizes `pyautogui` and `os` commands for local machine control.
    * **System Power Control:** Shutdown, restart, sleep, hibernate, and lock the system.
    * **Volume Control:** Increase or decrease system volume.
    * **System Apps:** Open core Windows applications (Task Manager, File Explorer, Command Prompt, Control Panel, etc.).
    * **Screenshot Capture:** Take and save a screenshot with a user-specified filename.
* **💡 Information Retrieval:** Provides current **time** and **date**.
* **📡 Network Info:** Fetches and reports the system's public **IP Address**.

---

## 🛠️ Technology Stack

| Category | Library/Module | Core Functionality Demonstrated |
| :--- | :--- | :--- |
| **Speech** | `speech_recognition`, `pyttsx3` | Natural Language Processing (NLP), I/O Interface. |
| **Automation** | `pyautogui`, `os`, `webbrowser` | Cross-platform system interaction and process control. |
| **Web Services** | `pywhatkit`, `requests`, `wikipedia` | API Integration, external data retrieval. |
| **Data Handling** | `sqlite3`, `datetime`, `calendar` | Database management, data persistence, and time operations. |

---

## 🔧 Setup and Installation

To run this project, you will need to install the required Python libraries listed in `requirements.txt`.

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-Link-Here]
    cd Voice-Assistant-Six
    ```

2.  **Install dependencies:**
    It is highly recommended to use a virtual environment.

    ```bash
    # Create a virtual environment
    python -m venv venv
    # Activate the virtual environment (Windows)
    .\venv\Scripts\activate
    # Activate the virtual environment (macOS/Linux)
    # source venv/bin/activate

    # Install all required packages using the created file
    pip install -r requirements.txt
    ```

3.  **Run the assistant:**
    ```bash
    python voice_assistant.py 
    ```

---

## ⚙️ How to Use

1.  **Wake Up:** Say **"Assistant"** or **"Six"** to initiate the dialogue.
2.  **User Authentication:** The assistant will ask your name and perform a database check. If you're a new user, it will prompt you for basic profile details.
3.  **Give Commands:** Once awake, issue a command.

### Example Commands:

| Command Phrase | Action Performed |
| :--- | :--- |
| `"Assistant play smooth jazz"` | Plays the content on YouTube. |
| `"What is the time"` | Reports the current time. |
| `"Search for deep learning on Google"` | Opens a new Google search tab. |
| `"What is photosynthesis"` | Fetches and speaks a Wikipedia summary. |
| `"Take screenshot"` | Prompts for a file name and captures the screen. |
| `"Open command prompt"` | Opens the Windows Command Prompt. |
| `"Lock the system"` | Locks the Windows session. |
| `"Go to sleep"` | Deactivates the listening loop. |

---

## 🧑‍💻 Creator

This project was developed by **Aniket**, a B Tech CSE student at HNB Garhwal University (Roll No.: 21134501015).
