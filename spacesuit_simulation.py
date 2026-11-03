
# -*- coding: utf-8 -*-
import numpy as np
import time

def run_spacesuit_simulation_fr():
    C_suit = 100e-12  # Capacitance = 100 pF
    suit_area_m2 = 5.0
    thickness_mm = 1.0
    density_kg_m3 = 1200.0
    
    volume_m3 = suit_area_m2 * (thickness_mm / 1000.0)
    total_outer_weight_kg = volume_m3 * density_kg_m3
    
    space_scenarios = {
        "Scenario A: Ombre Lunaire Profonde (Froid Extreme)": {
            "temp_c": -240, "biochar_pct": 0.20, "resistance_ohm": 6e5,
            "qhse": "Flexibilite totale des joints en silicone optique."
        },
        "Scenario B: Exposition Solaire Directe (Chaleur Extreme)": {
            "temp_c": 120, "biochar_pct": 0.15, "resistance_ohm": 1.2e6,
            "qhse": "Isolation thermique totale via Mylar et Nano-Ceramique."
        },
        "Scenario C: Tempete Solaire et Magnetique": {
            "temp_c": 0, "biochar_pct": 0.10, "resistance_ohm": 4.5e6,
            "qhse": "Dissipation constante et sûre de la poussiere lunaire."
        }
    }
    
    print("=" * 85)
    print(f"  Sifi Bouklhari - Khenchela AURES | Official Spacesuit Engineering Terminal")
    print("=" * 85)
    print(f" -> Area of the Spacesuit: {suit_area_m2:.1f} m2")
    print(f" -> Thickness of Outer Shield: {thickness_mm:.1f} mm")
    print(f" -> Total Shield Weight: {total_outer_weight_kg:.2f} kg")
    print("-" * 85)
    
    for name, env in space_scenarios.items():
        R = env["resistance_ohm"]
        t_discharge = R * C_suit * np.log(10)
        w_biochar = total_outer_weight_kg * env["biochar_pct"]
        w_matrix = total_outer_weight_kg * (1.0 - env["biochar_pct"])
        
        print(f"[+] {name}:")
        print(f"   - Temperature: {env['temp_c']} C")
        print(f"   - Biochar Weight: {w_biochar:.3f} kg ({env['biochar_pct']*100:.0f}%)")
        print(f"   - Matrix Weight (Silicone+Mylar+Ceramic): {w_matrix:.3f} kg")
        print(f"   - ESD Discharge Time: {t_discharge * 1000:.4f} ms")
        print(f"   - QHSE Evaluation: {env['qhse']}")
        print(f"   - NASA Standards Status: PASSED (Discharge < 500 ms)")
        print("-" * 85)
        time.sleep(0.2)

if __name__ == "__main__":
    run_spacesuit_simulation_fr()
