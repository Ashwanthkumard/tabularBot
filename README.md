# TabularBot

TabularBot is a Python application designed for managing and processing tabular data. It integrates various components to facilitate data extraction, manipulation, and analysis. This project is built using modular design principles, allowing for easy extension and maintenance.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Features

- **Data Extraction**: Extracts data from various sources using pymupdf.
- **Data Processing**: Provides methods for data manipulation and cleaning. Uses openai GPT-4o.
- **Prompts Management**: Includes predefined prompts for data querying and analysis. Uses openai GPT-4o.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone git@github.com:Ashwanthkumard/tabularBot.git
    cd tabularbot
    ```

2. **Install dependencies using Poetry:**

    ```sh
    poetry install
    ```

   Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed. If not, you can install it using:

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your environment variables:

    ```
    OPEN_AI_KEY=your_open_ai_key_here
    ```

## Usage

To run the application, use the `main.py` script. You can pass the directory containing your data as a command-line argument.

Example:

```sh
poetry run python main.py /path/to/data/folder
```

### Example

If your data is located in `/Users/ashwanth/Data/invoices`, you would run:

```sh
poetry run python main.py /Users/ashwanth/Data/invoices
```

## Configuration

Logging is configured in the `tabularbot/logging_config.py` file. By default, it logs messages to both the console and a file named `logs.log`.

You can customize logging settings by modifying the `setup_logging()` function in `logging_config.py`.



