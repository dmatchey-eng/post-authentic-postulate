import random

class ProvenanceGate:
    def __init__(self, source_url):
        self.source_url = source_url
        self.trusted_ledgers = ["ledger://hardware-signed.camera.gov", "ledger://reuters-immutable-node"]

    def is_verified(self):
        return any(ledger in self.source_url for ledger in self.trusted_ledgers)

    def generate_invalidation_receipt(self):
        return {
            "system_event": "PROVENANCE_AUDIT_FAILURE",
            "query_raised": "Where did you get it from?",
            "provided_source": self.source_url,
            "invalidation_receipt": {
                "receipt_id": f"IR-{random.randint(100000, 999999)}",
                "status": "UNVERIFIED_SOURCE_FREEZE",
                "ruling_clause": "This ticket does NOT prove a victory for either party. It certifies that the data source is structurally unverified. Text debate is blocked. Take it outside.",
                "action_required": "Present this ticket at the physical Demonstration Space threshold to initiate hardware isolation tests."
            }
        }
