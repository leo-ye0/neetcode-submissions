class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        card_counts = Counter(hand)
        
        for num in hand:
            # If this card has already been consumed, skip it
            if card_counts[num] == 0:
                continue
                
            # Find the earliest start of the consecutive chain containing 'num'
            start = num
            while card_counts[start - 1] > 0:
                start -= 1
                
            # Process the chain from the absolute start forward
            while start <= num:
                while card_counts[start] > 0:
                    # Try to create one full group starting at 'start'
                    for i in range(groupSize):
                        current_card = start + i
                        if card_counts[current_card] == 0:
                            return False
                        card_counts[current_card] -= 1
                start += 1
                
        return True