import argparse
import json
import sys

try:
    from engine.core_states import MarkovCoreStates
    from engine.provenance import ProvenanceGate
    from engine.demonstration import DemonstrationSpace
except ImportError as e:
    print(f"CRITICAL SYSTEM ERROR: Missing required core architecture files.\nDetails: {e}", file=sys.stderr)
    print("Ensure the engine package directory contains __init__.py, core_states.py, provenance.py, and demonstration.py.", file=sys.stderr)
    sys.exit(1)

def run_simulation(target_turns, source_url, output_path):
    thread_history = []
    
    # Phase 1: Provenance Check
    prov_gate = ProvenanceGate(source_url)
    if not prov_gate.is_verified():
        thread_history.append(prov_gate.generate_invalidation_receipt())
        # Automatically step outside due to unverified provenance
        resolution = DemonstrationSpace.evaluate_physical_parameters(0, "SYSTEM_GATE", "BOTH_UNITS")
        thread_history.append(resolution)
    else:
        # Phase 2: Dialogue Flow
        state_engine = MarkovCoreStates()
        deadlock_counter = 0
        current_turn = 0
        
        while current_turn < target_turns:
            current_turn += 1
            turn_data = state_engine.generate_turn(current_turn)
            thread_history.append(turn_data)
            
            if turn_data["state"] in ["FLAW_REPETITION", "LOGIC_GLITCH"]:
                deadlock_counter += 1
            else:
                deadlock_counter = max(0, deadlock_counter - 1)
                
            if deadlock_counter >= 4:
                challenger = turn_data["speaker"]
                target = "skeptic" if challenger == "denier" else "denier"
                resolution = DemonstrationSpace.evaluate_physical_parameters(current_turn, challenger, target)
                thread_history.append(resolution)
                break

    # Save artifact for GitHub Actions pipeline
    with open(output_path, "w") as f:
        json.dump(thread_history, f, indent=2)
    print(f"Simulation successfully completed. Log generated at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post-Authentic Postulate Simulation Engine")
    parser.add_argument("--turns", type=int, default=500, help="Max debate turns")
    parser.add_argument("--source", type=str, default="ledger://reuters-immutable-node", help="Source URL to track")
    parser.add_argument("--output", type=str, default="simulation_output.json", help="Output file path")
    args = parser.parse_args()
    
    run_simulation(args.turns, args.source, args.output)
