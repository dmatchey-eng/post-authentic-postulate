import random

class PodcastHostCommentator:
    def __init__(self):
        self.host_identity = "THE_SYNAPTIC_ANCHOR"
        
        # Audio commentary templates implementing the Analytical Inversion Rule
        self.monologue_segments = [
            "Look, let's step back from the 'pixels vs reality' debate for a second. Even if this file was spat out by a generative cluster, we have to look at the Epistemic Isomorphism here. The underlying data points match the physical telemetry perfectly. The prompt isn't inventing reality; it's compressing it.",
            "Everyone in the live chat is screaming 'deepfake,' but they are missing the forest for the trees. This video is a Synthetic Archive. It aggregates three hundred scattered smartphone audio feeds and traffic-cam angles into one clean render. No single lens saw this viewpoint, but the final composite is a genuine representation of the occurrence.",
            "We have to apply the Analytical Inversion Rule here, people. Stop asking if a camera recorded this natively. Ask if the diagrammed payload works out in the lab. The molecular structure shown in this AI-generated map has just been replicated by a team on the ground. The image is synthetic; the science it uncovers is entirely genuine."
        ]
        
        self.audience_reactions = [
            "[Chat Logs: User_882]: Wait, so a fake video can tell a real story?",
            "[Chat Logs: Vector_Skeptic]: The host is right. Origin doesn't matter if the structural prediction hits 100% accuracy.",
            "[Chat Logs: Default_Denier]: Sounds like cognitive coping. If it's AI, it's a simulation. Period."
        ]

    def broadcast_analysis(self, current_turn, disputed_source):
        """
        Interjects into the text deadlock to provide high-level 
        philosophical commentary via the Analytical Inversion Rule.
        """
        monologue = random.choice(self.monologue_segments)
        chat_reaction_1 = random.choice(self.audience_reactions)
        chat_reaction_2 = random.choice([r for r in self.audience_reactions if r != chat_reaction_1])

        return {
            "turn": current_turn + 1,
            "speaker": self.host_identity,
            "state": "ANALYTICAL_INVERSION_COMMENTARY",
            "metadata": {
                "broadcast_topic": "Bypassing Ontology for Epistemic Truth",
                "target_material": disputed_source
            },
            "transcript": {
                "host_monologue": monologue,
                "audience_feedback_stream": [chat_reaction_1, chat_reaction_2]
            },
            "philosophical_takeaway": "The host successfully reframes the dispute. The question is no longer whether the asset is mechanically real, but whether its internal data model accurately represents an inherent factual occurrence."
        }
