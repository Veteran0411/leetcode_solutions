# player can play any number of balls

# def score(s):
#     ball = 0
#     strike = True
#     player1 = 0
#     player2 = 0
#     runs = s.split("|")
#     for over in runs:
#         for run in over:
#             if strike:
#                 if int(run) % 2 != 0:
#                     strike = False
#                 player1 += int(run)
#             else:
#                 if int(run) % 2 != 0:
#                     strike = True
#                     player2 += int(run)
#             ball += 1
#             if ball == 6:
#                 strike = strike if int(over[ball - 1]) % 2 == 0 else not strike

#     return [1, player1] if player1 > player2 else [2, player2]

def score(runs):
    player1=0
    player2=0
    strike1=True
    for i in range(len(runs)):
        if runs[i]=="|":
            strike1=not strike1
            continue
        
        run=int(runs[i])
        if strike1:
            player1+=run
            if run%2 !=0:
                strike1=False
        else:
            player2+=run
            if run !=0:
                strike1=True
                
    print(f"runs scored: {max(player1,player2)}")
    return "1" if player1>player2 else "2"

if __name__ == "__main__":
    runs = "211221|6116"
    result = score(runs)
    print(f"player {result} has scored more runs")
    


