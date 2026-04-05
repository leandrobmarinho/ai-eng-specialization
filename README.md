# AI Engineering Specialization

This repository contains notes, experiments, and projects developed during the **AI Engineering Specialization** by [Dev Eficiente](https://deveficiente.com/interesse-especializacao-engenharia-ia).

The goal is to build practical skills for designing, developing, and deploying real-world AI systems using modern tools and architectures.

## Topics covered

- Machine learning systems design
- LLM engineering
- Retrieval-Augmented Generation (RAG)
- AI agents
- Evaluation strategies for AI systems
- Data pipelines for AI applications
- Prompt engineering
- Experiment tracking and reproducibility
- Production considerations (scalability, monitoring, reliability)

## Repository structure

| Path | Description |
|------|-------------|
| `main.py` | Entry point and orchestration for experiments |
| `tokenization.py` | Tokenization utilities and related experiments |
| `pyproject.toml` | Project metadata and Python dependencies ([uv](https://github.com/astral-sh/uv)) |
| `uv.lock` | Locked dependency versions for reproducible installs |

The layout will grow as modules, notebooks, and services are added during the specialization.

## Setup

Requires **Python 3.11+** and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Run the project (example):

```bash
uv run python main.py
```

Development dependencies (e.g. Jupyter kernel) live in the `dev` group:

```bash
uv sync --group dev
```