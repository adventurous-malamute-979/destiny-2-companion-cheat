# Build: 2705456c9030d34e8fa8bd6d7b763998

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
