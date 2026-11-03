"""
Acoustic Startle Reflex & Prepulse Inhibition (PPI) Sensorimotor Gating Engine.
Provides deterministic, zero-dependency modeling of prepulse inhibition percentage (%PPI),
lead-interval habituation kinetics, and brainstem/forebrain sensorimotor gating integrity.
"""

from typing import Dict, Any, List, Optional


class AcousticStartlePPIClient:
    """
    Deterministic client for calculating Acoustic Startle Prepulse Inhibition (PPI).
    Measures central nervous system sensorimotor filtering and pontine/striatal gating
    efficiency under varying acoustic prepulse intensities and lead intervals.
    """

    def __init__(self):
        pass

    def evaluate_prepulse_inhibition(
        self,
        pulse_alone_amplitude: float,
        prepulse_pulse_amplitude: float,
        prepulse_intensity_db: float = 75.0,
        lead_interval_ms: float = 100.0,
        pulse_intensity_db: float = 110.0
    ) -> Dict[str, Any]:
        """
        Calculates %PPI = ((Pulse_Alone - Prepulse_Pulse) / Pulse_Alone) * 100.
        Healthy adult human normative %PPI at 100-120 ms lead interval is typically 50.0% to 85.0%.
        """
        if pulse_alone_amplitude <= 0:
            return {"error": "Pulse-alone amplitude must be greater than zero"}

        if prepulse_pulse_amplitude < 0:
            prepulse_pulse_amplitude = 0.0

        ppi_pct = round(((pulse_alone_amplitude - prepulse_pulse_amplitude) / pulse_alone_amplitude) * 100.0, 1)

        # Lead interval habituation weighting factor:
        # Ideal lead interval is between 60 ms and 120 ms.
        # Below 30 ms or above 500 ms gating naturally diminishes.
        if 60.0 <= lead_interval_ms <= 140.0:
            lead_factor = 1.0
        elif 30.0 <= lead_interval_ms < 60.0:
            lead_factor = 0.85
        elif 140.0 < lead_interval_ms <= 250.0:
            lead_factor = 0.80
        else:
            lead_factor = 0.65

        # Sensorimotor Gating Resilience Score (0 - 100):
        # PPI >= 65% with optimal lead interval -> 85 - 100.
        # PPI 45% - 64% -> 65 - 84.
        # PPI < 30% -> < 45 (Sensorimotor flood / cognitive distractibility).
        raw_score = (ppi_pct / 80.0) * 85.0 * lead_factor
        gating_score = round(min(100.0, max(5.0, raw_score)), 1)

        is_gating_normal = ppi_pct >= 45.0

        if ppi_pct >= 65.0:
            tier = "ROBUST_SENSORIMOTOR_GATING"
            interp = f"Strong prepulse inhibition ({ppi_pct}% at {lead_interval_ms} ms lead); intact striatal-pallidal-thalamic filtering."
            guidance = "Excellent sensory noise filtering; high cognitive bandwidth retention in high-stimulation and open-office environments."
        elif ppi_pct >= 45.0:
            tier = "NORMAL_SENSORIMOTOR_GATING"
            interp = f"Preserved acoustic prepulse inhibition ({ppi_pct}%); normal sensorimotor gating and startle suppression."
            guidance = "Healthy sensory habituation. Maintain standard cognitive recovery rhythms."
        elif ppi_pct >= 25.0:
            tier = "MILD_GATING_ATTENUATION"
            interp = f"Moderate reduction in sensory gating ({ppi_pct}%); susceptible to sensory overload and micro-distraction."
            guidance = "Recommend active noise-cancelling headphones, reduced ambient auditory clutter, and structured deep work blocks."
        else:
            tier = "COMPROMISED_PREPULSE_INHIBITION"
            interp = f"Severely diminished PPI ({ppi_pct}% < 25%); significant central sensorimotor disinhibition or neural fatigue."
            guidance = "High vulnerability to startle and sensory exhaustion. Limit acoustic overstimulation, avoid late caffeine, and assess neurological fatigue."

        return {
            "pulse_alone_amplitude": pulse_alone_amplitude,
            "prepulse_pulse_amplitude": prepulse_pulse_amplitude,
            "ppi_percentage": ppi_pct,
            "prepulse_intensity_db": prepulse_intensity_db,
            "pulse_intensity_db": pulse_intensity_db,
            "lead_interval_ms": lead_interval_ms,
            "sensorimotor_gating_score": gating_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
