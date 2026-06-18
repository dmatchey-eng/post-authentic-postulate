import unittest
from engine.provenance import ProvenanceGate
from engine.core_states import MarkovCoreStates
from engine.podcast_host import PodcastHostCommentator

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
        self.assertIn("host_monologue", broadcast["transcript"])

    def test_dynamic_podcast_context_inference(self):
        host = PodcastHostCommentator()
        
        # Explicit test vectors aligned with GitHub workflow default inputs
        political_url = "https://anon-drop.net"
        scientific_url = "https://open-science.org"
        
        # Test Case 1: Political Domain Check
        political_run = host.broadcast_analysis(1, political_url)
        domain_result_1 = political_run["metadata"]["inferred_domain"]
        print(f"[DEBUG LOG] Tested URL: {political_url} -> Inferred Domain: {domain_result_1}")
        
        # Assert with a custom failure message to pinpoint the exact issue
        self.assertEqual(
            domain_result_1, 
            "political_leak", 
            f"Failed to infer political domain. URL checked: '{political_url}'. Host returned: '{domain_result_1}'"
        )
        
        # Test Case 2: Scientific Domain Check
        science_run = host.broadcast_analysis(1, scientific_url)
        domain_result_2 = science_run["metadata"]["inferred_domain"]
        print(f"[DEBUG LOG] Tested URL: {scientific_url} -> Inferred Domain: {domain_result_2}")
        
        self.assertEqual(
            domain_result_2, 
            "scientific_data", 
            f"Failed to infer scientific domain. URL checked: '{scientific_url}'. Host returned: '{domain_result_2}'"
        )

if __name__ == "__main__":
    unittest.main()
