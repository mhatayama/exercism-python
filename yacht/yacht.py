ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 11
FOUR_OF_A_KIND = 12
LITTLE_STRAIGHT = 13
BIG_STRAIGHT = 14
CHOICE = 15
YACHT = 16

def score(dice, category):
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
    if category in range(1, 7):
        return sum([x for x in dice if x == category])
    if category == FOUR_OF_A_KIND:
        for i in range(1, 7):
            if len([x for x in dice if x == i]) >= 4:
                return 4 * i
    if category == FULL_HOUSE:
        min_dice_num = len([x for x in dice if x == min(dice)])
        if len(set(dice)) == 2 and min_dice_num in [2, 3]:
            return sum(dice)
    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
    if category == CHOICE:
        return sum(dice)
    return 0
