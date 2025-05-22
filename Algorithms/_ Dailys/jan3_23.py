# [M] 2125. Number of Laser Beams in a Bank

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        # first instinct:
        # each row A will connect to the next populated row B
        # each from A connects to every in B, so we get A * B connections
        # sol: count each device in each row. if nonzero, add prevcount * count to total
        prevCount = 0
        count = 0
        total = 0
        for row in bank:
            count = row.count('1')
            if count > 0:
                total += count * prevCount
                prevCount = count
        return total