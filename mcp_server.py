"""
MCP Server for Acoustic Startle Prepulse Inhibition (PPI) Skill.
Exposes JSON-RPC Model Context Protocol tools for sensorimotor gating and startle reflex modulation.
"""

import sys
import json
from typing import Dict, Any
from client import AcousticStartlePPIClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_prepulse_inhibition",
                "description": "Calculates Acoustic Startle Prepulse Inhibition percentage (%PPI), sensorimotor gating score, and attentional focus resilience.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "pulse_alone_amplitude": {
                            "type": "number",
                            "description": "Peak startle reflex amplitude to acoustic pulse alone (e.g. 120.0 uV)."
                        },
                        "prepulse_pulse_amplitude": {
                            "type": "number",
                            "description": "Peak startle reflex amplitude to prepulse-pulse pair (e.g. 36.0 uV)."
                        },
                        "prepulse_intensity_db": {
                            "type": "number",
                            "description": "Prepulse decibel intensity (e.g. 75.0 dB).",
                            "default": 75.0
                        },
                        "lead_interval_ms": {
                            "type": "number",
                            "description": "Interstimulus lead interval in milliseconds (typically 60-120 ms).",
                            "default": 100.0
                        },
                        "pulse_intensity_db": {
                            "type": "number",
                            "description": "Startle pulse stimulus intensity (e.g. 110.0 dB).",
                            "default": 110.0
                        }
                    },
                    "required": ["pulse_alone_amplitude", "prepulse_pulse_amplitude"]
                }
            }
        ]
    }


def handle_request(client: AcousticStartlePPIClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_prepulse_inhibition":
            res = client.evaluate_prepulse_inhibition(
                pulse_alone_amplitude=float(args.get("pulse_alone_amplitude", 100.0)),
                prepulse_pulse_amplitude=float(args.get("prepulse_pulse_amplitude", 40.0)),
                prepulse_intensity_db=float(args.get("prepulse_intensity_db", 75.0)),
                lead_interval_ms=float(args.get("lead_interval_ms", 100.0)),
                pulse_intensity_db=float(args.get("pulse_intensity_db", 110.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = AcousticStartlePPIClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
