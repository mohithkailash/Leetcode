class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        use = max(damage)
        if use < armor:
            return sum(damage) - use + 1
        else:
            return sum(damage) - armor + 1