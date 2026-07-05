"""Test configuration for Medical Research Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "medical-research-agent", "category": "Healthcare"}
