"""
Example Usage: Acoustic Startle Reflex Prepulse Inhibition (PPI) Evaluation.
Demonstrates non-invasive calculation of %PPI and sensorimotor gating integrity.
"""

from client import AcousticStartlePPIClient


def main():
    client = AcousticStartlePPIClient()
    print("=== Acoustic Startle Prepulse Inhibition (PPI) Demo ===")

    # Test Case 1: Healthy robust sensorimotor gating
    res1 = client.evaluate_prepulse_inhibition(
        pulse_alone_amplitude=135.0,
        prepulse_pulse_amplitude=38.0,
        prepulse_intensity_db=75.0,
        lead_interval_ms=100.0,
        pulse_intensity_db=115.0
    )
    print("\nTest Case 1: Healthy Robust Gating (100 ms lead)")
    print(f"  Pulse Alone: {res1['pulse_alone_amplitude']} uV | Prepulse+Pulse: {res1['prepulse_pulse_amplitude']} uV")
    print(f"  PPI: {res1['ppi_percentage']}%")
    print(f"  Sensorimotor Gating Score: {res1['sensorimotor_gating_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Suboptimal / short lead interval
    res2 = client.evaluate_prepulse_inhibition(
        pulse_alone_amplitude=120.0,
        prepulse_pulse_amplitude=65.0,
        lead_interval_ms=30.0
    )
    print("\nTest Case 2: Short Lead Interval (30 ms)")
    print(f"  PPI: {res2['ppi_percentage']}%")
    print(f"  Gating Score: {res2['sensorimotor_gating_score']} / 100")
    print(f"  Classification: {res2['classification']}")

    # Test Case 3: Attenuated prepulse inhibition (Sensory overload / gating deficit)
    res3 = client.evaluate_prepulse_inhibition(
        pulse_alone_amplitude=150.0,
        prepulse_pulse_amplitude=125.0,
        lead_interval_ms=100.0
    )
    print("\nTest Case 3: Compromised Sensorimotor Gating")
    print(f"  PPI: {res3['ppi_percentage']}%")
    print(f"  Gating Score: {res3['sensorimotor_gating_score']} / 100")
    print(f"  Classification: {res3['classification']}")
    print(f"  Guidance: {res3['actionable_guidance']}")


if __name__ == "__main__":
    main()
