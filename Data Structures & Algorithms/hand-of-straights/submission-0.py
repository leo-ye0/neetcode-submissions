class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_counts = Counter(hand)
        sorted_cards = sorted(card_counts.keys())
        for card in sorted_cards:
            if card_counts[card] > 0:
                count_needed = card_counts[card]

                for i in range(groupSize):
                    current_card = card + i
                    
                    # If we don't have enough of the consecutive cards, fail
                    if card_counts[current_card] < count_needed:
                        return False
                    
                    # Consume the cards
                    card_counts[current_card] -= count_needed
                    
        return True