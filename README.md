# Incident Summary Bot

Incident Summary Bot is a small Python application that turns a security alert in JSON format into a structured incident summary. It validates and normalizes the input, sends it to the OpenAI API, and saves the resulting SOC-oriented analysis as JSON.

## Workflow

**Security Alert → Parsing and validation → Normalization → OpenAI API → Structured summary**

## Current Features

- Loads a JSON alert from the default sample file or a user-provided path.
- Validates required alert fields and accepted severity levels.
- Normalizes text values and missing optional fields.
- Uses the OpenAI API to generate a structured incident summary.
- Validates the generated response with a Pydantic schema.
- Prints the summary and saves it to `outputs/incident_summary.json`.
- Handles missing files, invalid JSON, invalid alerts, API errors, and output-writing errors.
- Includes unit tests for alert validation and normalization.

## Technologies

- Python 3.10+
- OpenAI Python SDK
- Pydantic
- python-dotenv
- unittest

## Project Structure

```text
Incident-Summary-Bot/
├── data/                 # Sample input alert
├── examples/             # Example generated output
├── outputs/              # Generated summary (created when needed)
├── src/                  # Application source code
├── tests/                # Unit tests
├── .env.example          # Environment variable template
└── requirements.txt      # Python dependencies
```

The default input is [`data/sample_alert.json`](data/sample_alert.json). A representative structured result is available at [`examples/sample_output.json`](examples/sample_output.json).

## Prerequisites

- Python 3.10 or newer
- An OpenAI API key
- Git

## Installation on Windows PowerShell

1. Clone the repository and enter its directory:

   ```powershell
   git clone <repository-url>
   cd Incident-Summary-Bot
   ```

2. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

3. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Copy the environment template:

   ```powershell
   Copy-Item .env.example .env
   ```

6. Open `.env` and configure the required values:

   ```dotenv
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-5.6-luna
   ```

## Usage

Process the default alert at `data/sample_alert.json`:

```powershell
python .\src\main.py
```

Process another JSON alert:

```powershell
python .\src\main.py .\path\to\alert.json
```

The generated summary is printed in the terminal and saved to `outputs/incident_summary.json`.

## Tests

```powershell
python -m unittest discover -s tests -v
```

## Security Note

Never commit or upload `.env`. It contains the API key and must remain private.

## MVP Limitations

- The project currently uses simulated security alerts.
- It processes one JSON file per execution.
- The final analysis depends on the LLM and should be reviewed by a security professional.
