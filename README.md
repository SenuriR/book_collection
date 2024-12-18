# Book Collection Manager

A simple Python project to manage your personal book collection using SQLite.

## Features
- Add, delete, list, and search for books
- Simple command-line interface

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it:


Repo Structure:
book_collection/
├── db/
│   └── book_collection.db         # SQLite database file
├── scripts/
│   ├── db_manager.py              # Handles database setup and operations
│   ├── cli.py                     # Main script to interact with the CLI
│   ├── utils.py                   # Helper functions (optional)
├── tests/
│   └── test_db_manager.py         # Unit tests for database functions
├── requirements.txt               # Dependencies (if any, like pytest or rich)
├── README.md                      # Project overview and instructions
└── .gitignore                     # To exclude unnecessary files like `*.db`
