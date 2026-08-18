from typing import Literal

from pydantic import BaseModel


class IncidentSummary(BaseModel):
    incident_title: str
    severity: Literal["low", "medium", "high", "critical"]
    executive_summary: str
    timeline: list[str]
    affected_assets: list[str]
    indicators_of_compromise: list[str]
    attacker_behavior: list[str]
    recommended_actions: list[str]
