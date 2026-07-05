"""Medical Research Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_literature():
    """Test Search PubMed and medical databases for relevant studies."""
    tools = AgentTools()
    result = await tools.search_literature(query="test", databases="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_summarize_study():
    """Test Summarize a medical research study with key findings."""
    tools = AgentTools()
    result = await tools.summarize_study(article_id="test", summary_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_find_clinical_trials():
    """Test Find relevant clinical trials for a condition or intervention."""
    tools = AgentTools()
    result = await tools.find_clinical_trials(condition="test", intervention="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_methodology():
    """Test Analyze study design and methodology quality."""
    tools = AgentTools()
    result = await tools.analyze_methodology(article_id="test", assessment_tool="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.medical_research_agent_agent import MedicalResearchAgentAgent
    agent = MedicalResearchAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
