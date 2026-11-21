# NOVA CLI 🤖

**Your Personal AI Assistant — Built with Python**

NOVA CLI is a command-line personal assistant project designed to explore Python programming, AI application development, automation and intelligent agents.

The project is being developed incrementally, starting with a modular command-line interface and gradually introducing AI-powered capabilities.

## 🚀 Current Features

- Interactive command-line application structure
- Beautiful terminal interface using Rich
- Command management using Typer
- Application welcome screen
- Application information command

## 🛠️ Tech Stack

- Python 3.12
- Typer
- Rich
- python-dotenv
- JSON (planned for data persistence)

## 📁 Project Structure

```text
nova-cli/
├── nova/
│   ├── __init__.py
│   ├── main.py
│   ├── commands.py
│   └── assistant.py
├── data/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/nova-cli.git
```

Navigate into the project:

```bash
cd nova-cli
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Start NOVA:

```bash
python -m nova.main start
```

Display application information:

```bash
python -m nova.main about
```

View available commands:

```bash
python -m nova.main --help
```

## 🗺️ Development Roadmap

- [x] Project initialization
- [x] Command-line interface
- [x] Terminal styling
- [ ] Interactive conversation engine
- [ ] Task management
- [ ] Smart notes
- [ ] Calculator
- [ ] Python learning assistant
- [ ] Persistent memory
- [ ] LLM integration
- [ ] AI agent capabilities

## 🎯 Project Goal

The goal of NOVA CLI is to serve as a practical learning project for developing Python programming skills and understanding the foundations of AI engineering, LLM applications and AI agents.

## 👨‍💻 Author

**Tobenna Okenwa**

