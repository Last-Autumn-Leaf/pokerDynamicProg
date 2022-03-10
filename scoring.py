def check_four_of_a_kind(numbers):
    for i in numbers:
            if numbers.count(i) == 4:
                four = i
            elif numbers.count(i) == 1:
                card = i
    score = 105 + four + card/100
    return score

def check_full_house(numbers):
    for i in numbers:
        if numbers.count(i) == 3:
            full = i
        elif numbers.count(i) == 2:
            p = i
    score = 90 + full + p/100
    return score

def check_three_of_a_kind(numbers):
    cards = []
    for i in numbers:
        if numbers.count(i) == 3:
            three = i
        else:
            cards.append(i)
    score = 45 + three + max(cards) + min(cards)/1000
    return score

def check_two_pair(numbers):
    pairs = []
    cards = []
    for i in numbers:
        if numbers.count(i) == 2:
            pairs.append(i)
        elif numbers.count(i) == 1:
            cards.append(i)
            cards = sorted(cards,reverse=True)
    score = 30 + max(pairs) + min(pairs)/100 + cards[0]/1000
    return score

def check_pair(numbers):
    pair = []
    cards  = []
    for i in numbers:
        if numbers.count(i) == 2:
            pair.append(i)
        elif numbers.count(i) == 1:
            cards.append(i)
            cards = sorted(cards,reverse=True)
    score = 15 + pair[0] + cards[0]/100 + cards[1]/1000 + cards[2]/10000
    return score


def score_hand(hand,print_score=0):
    letters = [hand[i].suits for i in range(5)]  # We get the suit for each card in the hand
    numbers = [hand[i].number for i in range(5)]  # We get the number for each card in the hand
    rnum = [numbers.count(i) for i in numbers]  # We count repetitions for each number
    rlet = [letters.count(i) for i in letters]  # We count repetitions for each letter
    dif = max(numbers) - min(numbers)  # The difference between the greater and smaller number in the hand
    handtype = ''
    score = 0
    if 5 in rlet:
        if numbers == [14, 13, 12, 11, 10]:
            handtype = 'royal_flush'
            score = 135
            if print_score ==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif dif == 4 and max(rnum) == 1:
            handtype = 'straight_flush'
            score = 120 + max(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif 4 in rnum:
            handtype == 'four of a kind'
            score = check_four_of_a_kind(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif sorted(rnum) == [2, 2, 3, 3, 3]:
            handtype == 'full house'
            score = check_full_house(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif 3 in rnum:
            handtype = 'three of a kind'
            score = check_three_of_a_kind(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif rnum.count(2) == 4:
            handtype = 'two pair'
            score = check_two_pair(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        elif rnum.count(2) == 2:
            handtype = 'pair'
            score = check_pair(numbers)
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
        else:
            handtype = 'flush'
            score = 75 + max(numbers) / 100
            if print_score==1 :
                print('this hand is a %s:, with score: %s' % (handtype, score))
    elif 4 in rnum:
        handtype = 'four of a kind'
        score = check_four_of_a_kind(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))
    elif sorted(rnum) == [2, 2, 3, 3, 3]:
        handtype = 'full house'
        score = check_full_house(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))
    elif 3 in rnum:
        handtype = 'three of a kind'
        score = check_three_of_a_kind(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))
    elif rnum.count(2) == 4:
        handtype = 'two pair'
        score = check_two_pair(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))
    elif rnum.count(2) == 2:
        handtype = 'pair'
        score = check_pair(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))
    elif dif == 4:
        handtype = 'straight'
        score = 65 + max(numbers)
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))

    else:
        handtype = 'high card'
        n = sorted(numbers, reverse=True)
        score = n[0] + n[1] / 100 + n[2] / 1000 + n[3] / 10000 + n[4] / 100000
        if print_score==1 :
            print('this hand is a %s:, with score: %s' % (handtype, score))

    return score

def handvalues(combi,print_score=0):
    scores =[{"hand": i, "value": score_hand(i,print_score)} for i in combi] # We iterate over all combinations scoring them
    scores = sorted(scores, key = lambda k: k['value']) # We sort hands by score
    return scores