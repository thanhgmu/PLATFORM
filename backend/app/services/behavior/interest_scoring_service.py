def score_interests(events: list[dict]) -> dict:
    channels = {}
    tags = {}

    for event in events:
        channel = event.get("channel", "unknown")
        channels[channel] = channels.get(channel, 0) + 1

        content = (event.get("content") or "").lower()
        for token in content.split():
            if len(token) < 4:
                continue
            tags[token] = tags.get(token, 0) + 1

    top_tags = sorted(tags, key=tags.get, reverse=True)[:5]
    preferred_channels = sorted(channels, key=channels.get, reverse=True)[:3]
    return {"preferred_channels": preferred_channels, "topic_tags": top_tags}
