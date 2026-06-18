import random

class PodcastHostCommentator:
    def __init__(self):
        self.host_identity = "THE_SYNAPTIC_ANCHOR"
        
        # Dynamic lexicon pools mapped by topic type
        self.lexicon = {
            "political_leak": {
                "monologue": "Look, stop looking at the compression artifacts on the politician's collar. Apply Epistemic Isomorphism here. The bank ledger transfers match the physical timeline perfectly. The AI didn't invent the corruption; it merely visualized a pre-existing financial trail.",
                "chat_pos": "[Chat Logs: PolicyAlpha]: The money trail is validated. The visual render is just a wrapper for verified ledger transactions.",
                "chat_neg": "[Chat Logs: DeepStateDenier]: Blatant deepfake designed to tank the election. Total narrative construction."
            },
            "scientific_data": {
                "monologue": "The live chat is losing its mind because an optical lens didn't snap this cell mutation directly. This is a Pragmatic Instrumentalist victory! The synthetic molecular map accurately predicted the receptor binding structure. The imagery is computed, but the chemistry is 100% genuine.",
                "chat_pos": "[Chat Logs: BioPragmatist]: Exactly. If the structural simulation successfully cures the disease, who cares who arranged the pixels?",
                "chat_neg": "[Chat Logs: PureAnalog]: If a human didn't look through a physical microscope, it's just statistical speculation."
            },
            "environmental_event": {
                "monologue": "Everyone yelling 'CGI drone footage' is missing the point of a Synthetic Archive. This render compiles three hundred erratic satellite pings and thermal sensors into one spatial model. It isn't a fake disaster; it's an aggregate structural mapping of a real occurrence.",
                "chat_pos": "[Chat Logs: EcoSensor_Net]: The thermal data layer matches the regional seismic shift perfectly. The event is real.",
                "chat_neg": "[Chat Logs: SimulationTruther]: They are using procedural generation software to manufacture ecological panic. Reject it."
            }
        }

       def _determine_context(self, disputed_source):
        """ Dynamically infers the subject domain from the source signature metadata """
        source_str = str(disputed_source).lower()
        
        # Explicit substring containment matching
        if "bribe" in source_str or "leak" in source_str or "politician" in source_str:
            return "political_leak"
        elif "cell" in source_str or "molecular" in source_str or "diagram" in source_str or "science" in source_str:
            return "scientific_data"
        else:
            return "environmental_event"

    def broadcast_analysis(self, current_turn, disputed_source):
        """
        Dynamically extracts context from the asset signature and evaluates
        truth values under the Analytical Inversion Rule.
        """
        context_key = self._determine_context(disputed_source)
        active_pool = self.lexicon[context_key]

        return {
            "turn": current_turn + 1,
            "speaker": self.host_identity,
            "state": "DYNAMIC_ANALYTICAL_INVERSION",
            "metadata": {
                "inferred_domain": context_key,
                "analyzed_target": disputed_source
            },
            "transcript": {
                "host_monologue": active_pool["monologue"],
                "audience_feedback_stream": [
                    active_pool["chat_pos"],
                    active_pool["chat_neg"]
                ]
            },
            "philosophical_takeaway": f"The host shifts focus away from pixel origin. By classifying this as a {context_key.replace('_', ' ')}, they prove that synthetic data can accurately deliver objective factual truth."
        }
