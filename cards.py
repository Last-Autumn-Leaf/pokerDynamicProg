import itertools

import numpy as np
import pandas as pd
import scoring

SUITS_TO_NAME={
    'H':'Heart',
    'S':'Spades',
    'C':'Clover',
    'D':'Diamond'
}

# list of Cards
def build_deck():
    numbers=list(range(2,15))
    suits = ['H','S','C','D']
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(Card(card))
    return deck

class Card():
    def __init__(self,suit:str,number:int=None):
        if number==None:
            self.number = int(suit[1:])
            self.suits = suit[0]
        else :
            self.number=number
            self.suits=suit




    def __repr__(self):
        return  self.suits+str(self.number)

    def __str__(self):
        return str(self.number)+" of "+SUITS_TO_NAME[self.suits]

def build_deck_2():
    numbers=list(range(2,15))
    suits = ['H','S','C','D']
    deck = []
    for i in numbers:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    return deck

#Crée toutes les combinaisons possibles du deck, 5 parmis 52 cartes
def combinations(arr, n):
    arr = np.asarray(arr)
    #t = np.dtype([( '',arr.dtype)]*n)
    result = []
    # np.fromiter(itertools.combinations(arr, n), arr.dtype)
    for subset in    itertools.combinations(arr, n):
        result.append(subset)
    return np.asarray(result)

if __name__ == '__main__':
    file_name='all_comb_score.csv'

    deck = build_deck()  # We create our deck
    combi = combinations(deck, 5)  # We create an array containing all possible 5 cards combinations
    hand_values = scoring.handvalues(combi)

    x = [i.get("hand", "") for i in hand_values]  # making a list of hands
    y = [i.get("value", "") for i in hand_values]  # making a list of values

    data = {'hands': x, 'value': y}  # making a dictionary of hands and values
    df = pd.DataFrame(data)  # making a pandas dataframe with hands and values
    df.to_csv(file_name, sep='\t', encoding='utf-8', index=False)

    #Use this to read all combi
    print( pd.read_csv(file_name, sep='\t', encoding='utf-8',index_col=0))