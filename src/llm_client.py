import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from schemas import IncidentSummary


project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")


def generate_incident_summary(normalized_alert):
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing")
    if not model:
        raise ValueError("OPENAI_MODEL is missing")

    client = OpenAI()
    response = client.responses.parse(
        model=model,
        text_format=IncidentSummary,
        input=[
            {
                "role": "system",
                "content": (
                    "Act as a SOC analyst. Base the incident summary only on "
                    "the provided alert, do not invent evidence, and propose "
                    "defensive actions."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(normalized_alert, ensure_ascii=False),
            },
        ],
    )

    if response.output_parsed is None:
        raise ValueError("The model did not return a parsed incident summary")

    return response.output_parsed
