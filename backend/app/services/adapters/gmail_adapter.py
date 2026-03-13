class GmailAdapter:
    def ingest_pubsub_event(self, payload: dict) -> dict:
        return {"status": "accepted", "source": "gmail_pubsub", "payload": payload}
