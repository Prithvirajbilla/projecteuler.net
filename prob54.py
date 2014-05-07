# def cards_great(a,b): # a> b
# 	l=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# 	if l.index(a) > l.index(b):
# 		return True
# 	else:
# 		return False

# def royal_flush(l):
# 	typ = [a[-1:] for a in l]
# 	cards = [a[:-1] for a in l]
# 	typ = list(set(typ))
# 	if len(typ) == 0:
# 		if "10" in cards and "J" in cards and "Q" in cards and "K" in cards and "A" in cards:
# 			return True
# 	else:
# 		return False

# def straight_flush(l):
# 	typ= [a[-1] for a in l]
# 	cards = [a[-1] for a in l]
# 	typ = list(set(typ))
# 	if len(typ) == 0:
# 		cards.sort()
# 		le = 0
# 		if int(cards[0]) == int(cards[-1])-4:
# 			return cards[-1]
# 	else:
# 		return False
# def num_of_iocc(l,a):
# 	ans= 0:
# 	for i in l:
# 		if i == a:
# 			ans= ans+1;
# 	return ans
# def four_of_a_kind(l):
# 	cards = [a:[-1] for a in l]
# 	for i in cards:
# 		if num_of_iocc(cards,i) == 4:
# 			return i
# 	return False

# def full_house(l):
# 	cards = [a:[-1] for a in l]
# 	ans = 0
# 	three = ""
# 	two = ""
# 	for i in cards:
# 		if num_of_iocc(cards,i) == 3:
# 			three = i
# 			ans= ans+1
# 		elif num_of_iocc(cards,i) == 2:
# 			two = i
# 			ans = ans+1
# 		elif ans == 2:
# 			return [three,two]
# 	return False

# def highcard(l):
# 	cards = [a[:-1] for a in l]
# 	cards.sort()
# 	return cards[-1]

# def flush(l):
# 	cards=[a:[-1] for a in l]
# 	typ = [a[-1:] for a in l]
# 	typ = list(set(typ))
# 	if len(typ) == 0:
# 		return highcard(l)
# 	else:
# 		return False

# def straight(l):
# 	cards=[a:[-1] for a in l]
# 	cards.sort()
# 	cards=list(set(cards))
# 	if len(cards) == 5:
# 		if cards[0] == '10':
# 			return "A"
# 		elif cards[0] == '2' and cards[-1] == 'A':
# 			return 'A'
# 		elif int(cards[0]) == int(cards[-1])-4:
# 			return cards[-1]
# 	else:
# 		return False

# def three_kind(l):
# 	cards = [a:[-1] for a in l]
# 	for i in cards:
# 		if num_of_iocc(l,i) == 3:
# 			return [i,highcard(l)]
# 	return False

# def two_kind(l):
# 	cards = [a:[-1] for a in l]
# 	awe = 0
# 	one = ""
# 	two = ""
# 	for i in cards:
# 		if num_of_iocc(l,i) == 2:
# 			if one == "":
# 				one = i;
# 			else:
# 				two = i
# 			awe=awe+1
# 		elif awe == 2:
# 			return [one,two,highcard(l)]
# 	return False


# f = open("poker.txt","r")

# l = f.readlines()

# one = 0;
# two = 0;
# for i in l:
# 	a = i.split(" ")
# 	p1 = a[0:5]
# 	p2 = a[5:]
# 	if royal_flush(p1):
# 		one=one+1
# 	elif not royal_flush(p2):
# 		if straight_flush(p1):
# 			if straight_flush(p2):
# 				if cards_great(straight_flush(p1),straight_flush(p2)):
# 					one=one+1
# 			else:
# 				one=one+1
# 		elif not straight_flush(p2):
# 			if four_of_a_kind(p1):
# 				if four_of_a_kind(p1) == four_of_a_kind(p2):
# 					if cards_great(highcard(p1),highcard(p2)):
# 						one=one+1
# 				elif cards_great(four_of_a_kind(p1),four_of_a_kind(p2)):
# 					one = one+1
# 			elif not four_of_a_kind(p2):
# 				if full_house(p1):
# 					if full_house(p1)[0] == full_house(p2)[0]:
# 						if cards_great(full_house(p1)[1], full_house(p2)[1]):
# 							one = one+1
# 					elif cards_great(full_house(p1)[0],full_house(p2)[0]):
# 						one = one + 1

# 					elif cards_great(highcard(p1),highcard(p2)):
# 						one = one +1
# 				elif not full_house(p2):
# 					if flush(p1):


from collections import Counter
 
d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, \
     '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, \
     'K': 13, 'A': 14, 'One Pair': 29, 'Two Pairs': 59, \
     'Three of a Kind': 74, 'Straight': 89, 'Flush': 104, \
     'Full House': 119, 'Four of a Kind': 134,
     'Straight Flush': 149, 'Royal Flush': 164}
 
def high_card(dL):
    """Is the hand High Card?"""
    holder = 0
    if len(dL) == 5:
        return True
    else:
        return False
 
def one_pair(dL):
    """Is the hand One Pair?"""
    if len(dL) == 4:
        for k, v in dL.iteritems():
            if v == 2:
                return True
            else:
                continue
    else:
        return False
 
def two_pairs(dL):
    """Is the hand Two Pairs?"""
    counter = 0
    k1 = 0
    if len(dL) == 3:
        for k, v in dL.iteritems():
            if v == 2:
                if k > k1:
                    k1 = k
                counter += 1
                if counter == 2:
                    return True
            else:
                continue
    else:
        return False
     
def three_of_a_kind(dL):
    """Is the hand Three of a Kind?"""
    if len(dL) == 3:
        for k, v in dL.iteritems():
            if v == 3:
                return True
            else:
                continue
    else:
        return False
 
def straight(L):
    """Is the hand a Straight?"""
    L = sorted(L)
    if (L[0] + 1) == L[1] and (L[0] + 2) == \
       L[2] and (L[0] + 3) == L[3] and \
       (L[0] + 4) == L[4]:
        return True
    else:
        return False
     
def flush(L1):
    """Is the hand a Flush"""
    if len(Counter(L1)) == 1:
        return True
    else:
        return False
 
def full_house(dL):
    """Is the hand a Full House?"""
    if len(dL) == 2:
        for k, v in dL.iteritems():
            if v == 3:
                return True
            else:
                continue
    else:
        return False
 
def four_of_a_kind(dL):
    """Is the hand Four of a Kind?"""
    if len(dL) == 2:
        for k, v in dL.iteritems():
            if v == 4:
                return True
            else:
                continue
    else:
        return False
 
def straight_flush(L, L1):
    """Is the hand a Straight Flush?"""
    L = sorted(L)
    if len(Counter(L1)) == 1 and \
       ((L[0] + 1) == L[1] and (L[0] + 2) == \
       L[2] and (L[0] + 3) == L[3] and \
       (L[0] + 4) == L[4]):
        return True
    else:
        return False
 
def royal_flush(L, L1):
    """Is the hand a Royal Flush?"""
    if len(Counter(L1)) == 1 and sum(L) == 60:
        return True
    else:
        return False
     
def examine_cards(cards):
    """Examine Cards"""
    L, L1 = [], []
    dL = {}
    for i in range(0, 9, 2):
        x1 = d[cards[i]]
        L.append(x1)
    for i in range(1, 10, 2):
        x1 = cards[i]
        L1.append(x1)
    for i in L:
        dL[i] = L.count(i)
    if royal_flush(L, L1):
        return d['Royal Flush']
    elif straight_flush(L, L1):
        return d['Straight Flush']
    elif four_of_a_kind(dL):
        c1 = 0
        for k, v in dL.iteritems():
            if v == 4:
                c1 = k
        return d['Four of a Kind'] + c1
    elif full_house(dL):
        c2 = 0
        for k, v in dL.iteritems():
            if v == 3:
                c2 = k
        return d['Full House'] + c2
    elif flush(L1):
        c3 = 0
        for k, v in dL.iteritems():
            if k > c3:
                c3 = k
        return d['Flush'] + c3
    elif straight(L):
        c4 = 0
        for k, v in dL.iteritems():
            if k > c4:
                c4 = k
        return d['Straight'] + c4
    elif three_of_a_kind(dL):
        c5 = 0
        for k, v in dL.iteritems():
            if v == 3:
                c5 = k
        return d['Three of a Kind'] + c5
    elif two_pairs(dL):
        k1 = 0
        for k, v in dL.iteritems():
            if v == 2:
                if k > k1:
                    k1 = k
        return d['Two Pairs'] + k1
    elif one_pair(dL):
        c6 = 0
        for k, v in dL.iteritems():
            if v == 2:
                c6 = k
        return d['One Pair'] + c6 
    elif high_card(dL):
        count1 = 0
        for k, v in dL.iteritems():
            if k > count1:
                count1 = k
        return count1
    else:
        print "***Error Message***"
     
def main():
    """Main Program"""
    player1 = 0
    f = open('poker.txt', 'r')
    for line in f:
        x = line.split(' ')
        y = ''.join(x)
        player_one = y[0:10]
        player_two = y[10:20]
        j = examine_cards(player_one)
        t = examine_cards(player_two)
        if j == t:
            print "player_one = ", player_one
            print "player_two = ", player_two
            print "EQUAL"
        elif j < t:
            continue
        elif j > t:
            player1 += 1
        else:
            pass
    f.close()
    print "Answer = ", player1
     
if __name__ == '__main__':
    mn