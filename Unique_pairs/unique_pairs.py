def unique_pairs(items, value):
    if len(items) < 2:
        return None
    seen = set()
    pairs = set()
    for item in items:
        needed = value - item
        if needed in seen:
            pair = (item, needed)
            pair = (min(pair), max(pair))
            if pair not in pairs:
                pairs.add(pair)
        seen.add(item)
    return pairs


print(unique_pairs([1, 3, 2, 2, 1], 4))
