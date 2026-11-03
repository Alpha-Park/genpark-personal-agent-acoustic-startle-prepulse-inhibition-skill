---
name: genpark-personal-agent-acoustic-startle-prepulse-inhibition-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Acoustic Startle Prepulse Inhibition (%PPI), sensorimotor gating, and environmental distractibility.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Acoustic Startle Prepulse Inhibition (PPI) Skill

A sovereign personal agent capability for assessing central nervous system sensorimotor filtering, brainstem startle modulation, and sensory overload resilience.

## Core Capabilities
- **%PPI Quantitative Index**: Calculates percentage inhibition of the acoustic startle reflex by weak prepulses.
- **Lead Interval Tuning**: Evaluates optimal interstimulus intervals (60-120 ms) for maximum neural filtering.
- **Sensorimotor Gating Resilience**: Identifies vulnerability to environmental distraction and sensory flood.
- **Focus Ergonomics**: Delivers tailored guidance on acoustic dampening and deep work structure.

## Fast Invocation
```python
from client import AcousticStartlePPIClient

client = AcousticStartlePPIClient()
res = client.evaluate_prepulse_inhibition(
    pulse_alone_amplitude=135.0,
    prepulse_pulse_amplitude=38.0,
    lead_interval_ms=100.0
)
print("PPI Percentage:", res["ppi_percentage"], "%")
print("Gating Score:", res["sensorimotor_gating_score"])
```
