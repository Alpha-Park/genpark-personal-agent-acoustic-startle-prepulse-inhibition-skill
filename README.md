# Acoustic Startle Prepulse Inhibition (PPI) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Acoustic Startle Reflex Prepulse Inhibition (%PPI), sensorimotor gating integrity, and environmental sensory overload vulnerability.

```mermaid
flowchart TD
    Acoustic["Acoustic Stimulus (Prepulse + Pulse Pairs)"] --> EMG_Reflex["Electromyography / Startle Reflex Peak Extraction"]
    EMG_Reflex --> PPI_Math["%PPI Equation & Lead Interval Calibration"]
    PPI_Math --> Gating["Sensorimotor Gating & Distractibility Scoring"]
    Gating --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Neurophysiological Standard Formulas**: Implements validated prepulse startle suppression equations.
- **Cognitive Distraction Stratification**: Quantitative evaluation of sensory filtering resilience in noisy environments.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import AcousticStartlePPIClient

client = AcousticStartlePPIClient()
result = client.evaluate_prepulse_inhibition(
    pulse_alone_amplitude=135.0,
    prepulse_pulse_amplitude=38.0,
    lead_interval_ms=100.0
)
print("PPI Percentage:", result["ppi_percentage"], "%")
print("Classification:", result["classification"])
```

## License
Apache-2.0
