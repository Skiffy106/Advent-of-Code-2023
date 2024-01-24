import sys
import math


class Hand:
    def __init__(self, hand):
        self.hand = hand

    def __lt__(self, other):
        return self.compare(other)

    def __eq__(self, other):
        return self.hand == other.hand

    def __repr__(self):
        return self.hand

    def get_type(hand: str) -> int:
        hand_list = list(hand)
        set_len = len(set(hand))
        if set_len == 1:
            return "7"  # five of a kind
        elif set_len == 2:
            # either full house or four of a kind
            tmp = hand_list.count(hand_list[0])
            if tmp == 4 or tmp == 1:
                return "6"  # four of a kind
            else:
                return "5"  # full house
        elif set_len == 3:
            # either 2 pair or three of a kind
            tmp = hand_list.count(hand_list[0])
            if tmp == 3:
                return 4  # three of a kind
            elif tmp == 2:
                return 3  # two pair
            else:
                item = max(hand_list, key=hand_list.count)
                if hand_list.count(item) == 3:
                    return 4  # three
                else:
                    return 3  # two pair
        elif set_len == 4:
            return 2  # pair
        else:
            return 1  # high

    def compare(self, other):
        type1 = Hand.get_type(self.hand)
        type2 = Hand.get_type(other.hand)
        print(type1, type2)
        if type1 > type2:
            return True
        elif type1 < type2:
            return False
        else:
            for idx in range(5):
                card1 = card_dict[hand1[idx]]
                card2 = card_dict[hand2[idx]]
                if card1 > card2:
                    return True
                elif card1 < card2:
                    return False
            return True
        return compare(self.hand, other.hand)

    # def compare(hand1: str, hand2: str) -> bool:
    #     type1 = Hand.get_type(hand1)
    #     type2 = Hand.get_type(hand2)
    #     print(type1, type2)
    #     if type1 > type2:
    #         return True
    #     elif type1 < type2:
    #         return False
    #     else:
    #         for idx in range(5):
    #             card1 = card_dict[hand1[idx]]
    #             card2 = card_dict[hand2[idx]]
    #             if card1 > card2:
    #                 return True
    #             elif card1 < card2:
    #                 return False
    #         return True


card_dict = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7,
             '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}


lines = []
hands = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    hand, bid = line.split()
    hands.append((Hand(hand), int(bid)))


[print(line) for line in lines]
# print("=" * 20)
# print(Hand.compare("KK677", "KTJJT"))
# print("=" * 20)
# print(Hand.compare("T55J5", "QQQJA"))
print("=" * 20)
print(hands)
print("=" * 20)
print(sorted(hands, key=lambda x: x[0]))
# print(get_type("AAAAA"))
# print("=" * 20)
# print(get_type("AAAAB"))
# print("=" * 20)
# print(get_type("AAABB"))
# print("=" * 20)
# print(get_type("AAABC"))
# print("=" * 20)
# print(get_type("AABCC"))
# print("=" * 20)
# print(get_type("ABBCC"))
# print("=" * 20)
# print(get_type("ABCDA"))
# print("=" * 20)
# print(get_type("ABCDE"))
