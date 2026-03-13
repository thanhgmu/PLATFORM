class ZaloAdapter:
    def send(self, payload: dict) -> dict:
        return {"status": "queued", "channel": "zalo", "payload": payload}
