import random

class MarkovCoreStates:
    def __init__(self):
        self.states = ["NORMAL", "FLAW_REPETITION", "LOGIC_GLITCH"]
        self.transition_weights = [0.40, 0.40, 0.20] # Prioritizes deadlock generation

        self.denier_vocab = {
            "NORMAL": ["That content is statistically improbable, meaning it is mathematically manufactured."],
            "FLAW_REPETITION": ["I already told you, it looks fake. No amount of data changes that."],
            "LOGIC_GLITCH": ["If the data looks real, that just proves how advanced the spoofing algorithm is."]
        }
        
        self.skeptic_vocab = {
            "NORMAL": ["Under the Post-Authentic Postulate, we look past visual fidelity to cryptographic signatures."],
            "FLAW_REPETITION": ["I must repeat: hardware verification bypasses visual guesswork entirely."],
            "LOGIC_GLITCH": ["By treating all data layers as corrupt, you isolate yourself in a solipsistic vacuum."]
        }

    def generate_turn(self, turn_number):
        is_denier_turn = (turn_number % 2 != 0)
        state = random.choices(self.states, weights=self.transition_weights)[0]
        
        if is_denier_turn:
            speaker = "denier"
            statement = random.choice(self.denier_vocab[state])
            mechanism = "The Aesthetics Equivalence" if state == "NORMAL" else ("Reflexive Circular Repetition" if state == "FLAW_REPETITION" else "The Incredulity Shortcut")
            stance = "Reflexive Invalidation Fault"
        else:
            speaker = "skeptic"
            statement = random.choice(self.skeptic_vocab[state])
            mechanism = "The Post-Authentic Postulate" if state == "NORMAL" else ("Redundant Verification Loop" if state == "FLAW_REPETITION" else "Recursive Deconstruction")
            stance = "Radical Contextual Skepticism"

        if state == "FLAW_REPETITION":
            statement += f" [System Alert: Repetition Loop Logged at Node {turn_number}]"
        elif state == "LOGIC_GLITCH":
            statement += f" [System Alert: Epistemic Fallacy Logged at Node {turn_number}]"

        return {
            "turn": turn_number,
            "speaker": speaker,
            "state": state,
            "statement": statement,
            "mechanism_applied": mechanism,
            "epistemic_stance": stance
        }
