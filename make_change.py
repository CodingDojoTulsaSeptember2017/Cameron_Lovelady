def make_change(cents):
    change = {}
    doll = 0
    hdoll = 0
    quart = 0
    dime = 0
    nick = 0
    penn = 0
    currency = ['dollars', 'halfdollars', 'quarters', 'dimes', 'nickels', 'pennies']
    for i in range(0, cents):
        if cents/100 > 0:
            doll = doll + 1
            cents = cents - 100
        elif cents/50 > 0:
            hdoll = hdoll  + 1
            cents = cents - 50
        elif cents/25 > 0:
            quart = quart + 1
            cents = cents - 25
        elif cents/10 > 0:
            dime = dime  + 1
            cents = cents - 10
        elif cents/5 > 0:
            nick = nick + 1
            cents = cents - 5
        elif cents/1 > 0:
            penn  = penn + 1 
            cents = cents - 1               
    amount = [doll, hdoll, quart, dime, nick, penn]
    change = dict(zip(currency, amount))
    print change


make_change(68)