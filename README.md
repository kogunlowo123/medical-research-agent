# Medical Research Agent

[![CI](https://github.com/kogunlowo123/medical-research-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/medical-research-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Medical research agent that searches clinical literature, summarizes research findings, identifies relevant clinical trials, analyzes study methodologies, and generates literature review summaries.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_literature` | Search PubMed and medical databases for relevant studies |
| `summarize_study` | Summarize a medical research study with key findings |
| `find_clinical_trials` | Find relevant clinical trials for a condition or intervention |
| `analyze_methodology` | Analyze study design and methodology quality |
| `generate_literature_review` | Generate a structured literature review summary |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/medical-research/process` | Process request |
| `POST` | `/api/v1/medical-research/query` | Query data |
| `POST` | `/api/v1/medical-research/validate` | Validate |
| `POST` | `/api/v1/medical-research/report` | Generate report |
| `GET` | `/api/v1/medical-research/audit` | Get audit trail |

## Features

- Medical
- Research
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
medical-research-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── medical_research_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
