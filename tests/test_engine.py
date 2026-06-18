import unittest
from engine.provenance import ProvenanceGate
from engine.core_states import MarkovCoreStates

class TestPostAuthenticEngine(unittest.TestCase):
    def test_provenance_verification_success(self):
        gate = ProvenanceGate("ledger://reuters-immutable-node/video_01.mp4")
        self.assertTrue(gate.is_verified())

    def test_provenance_verification_failure(self):
        gate = ProvenanceGate("https://unverified-leak-site.net")
        self.assertFalse(gate.is_verified())
        receipt = gate.generate_invalidation_receipt()
        self.assertEqual(receipt["system_event"], "PROVENANCE_AUDIT_FAILURE")

    def test_core_states_generation(self):
        engine = MarkovCoreStates()
        turn = engine.generate_turn(1)
        self.assertEqual(turn["turn"], 1)
        self.assertEqual(turn["speaker"], "denier")
        self.assertIn(turn["state"], ["NORMAL", "FLAW_REPETITION", "LOGIC_GLITCH"])

    def test_podcast_host_block_generation(self):
        host = PodcastHostCommentator()
        broadcast = host.broadcast_analysis(10, "https://test-leak-source.com")
        self.assertEqual(broadcast["speaker"], "THE_SYNAPTIC_ANCHOR")
        self.assertEqual(broadcast["state"], "ANALYTICAL_INVERSION_COMMENTARY")
        self.assertIn("host_monologue", broadcast["transcript"])

if __name__ == "__main__":
    unittest.main()
