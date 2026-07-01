Smart Home Agent (Logic-Thought Approach)

This project focuses on developing an intelligent Smart Home Agent using the Logic-Thought approach, which aims to formalize human-like reasoning through structured propositional logic.
The system interprets natural language user commands, converts them into logical facts using a Large Language Model (Google Gemini API), and triggers corresponding automated actions based on a predefined set of rules.

---
📌 Project Overview

The core goal of this agent is to enable machines to "think" and act according to rational standards within a smart home ecosystem. 

* Natural Language Processing: The system accepts text-based user commands (e.g., *"I'm cold"*, *"It's morning"*).
* Logical Interpretation: An LLM acts as the interpreter to map these unstructured text inputs into strict propositional logic facts (e.g., `cold_weather`, `wake_up_time`).
* Rule-Based Execution: The system checks these facts against a logical rule-set and executes the appropriate simulated action.

---

⚙️ System Architecture

1. User Input: The user types a natural language command into the console. *(Speech recognition is ignored in this version).*
2. LLM Interpreter (Gemini API): Uses the `gemini-pro` model to process the command and return a predefined logical fact.
3. Facts & Rules: The system maintains a localized knowledge base where facts map directly to smart home rules.
4. Action Executor: If a logical fact matches a rule, the corresponding action is outputted to the console. (Physical smart devices are simulated via console outputs, supporting future hardware integration).*

---

🗂️ Code Structure
├── main.py            # The entry point of the application. Handles user input loop and triggers actions.
├── interpreter.py     # Connects to the Gemini API to analyze and retrieve the interpreted logical fact.
├── rules.json         # Contains the knowledge base mapping facts to actions in JSON format.
├── config.py          # Stores Gemini API keys, environment variables, and model configurations.
└── README.md          # Project documentation.

🧠 Knowledge Base: Facts & Actions

The system relies on the following propositional logic mappings configured within `rules.json`:

| Interpreted Fact | Triggered Action |
| :--- | :--- |
| `cold_weather` | `turn_on_heater` |
| `hot_weather` | `turn_on_ac` |
| `no_one_home` | `turn_off_all_devices` |
| `dark_room` | `turn_on_lights` |
| `bright_room` | `turn_off_lights` |
| `sleep_time` | `close_curtains` |
| `wake_time` / `wake_up_time` | `open_curtains` |
| `hot_enough` | `turn_off_heater` |
| `cold_enough` | `turn_off_ac` |
| `leaving_home` | `lock_door` |
| `arriving_home` | `unlock_door` |

---

💻 Sample Execution Traces

| User Command | Interpreted Fact | Triggered Action |
| :--- | :--- | :--- |
| "I'm cold"* | `cold_weather` | `turn_on_heater` |
| "It's hot enough"* | `hot_enough` | `turn_off_heater` |
| "I'm leaving the house"* | `leaving_home` | `lock_door` |
| "The room is dark"* | `dark_room` | `turn_on_lights` |
| "It's morning"* | `wake_up_time` | `open_curtains` |

---
