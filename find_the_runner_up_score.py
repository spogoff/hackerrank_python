if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = -100
    runner_up = -100
    for i in arr:
        if i > winner:
            winner, runner_up = i, winner
        elif (i < winner and i > runner_up):
            runner_up = i

    print(runner_up)


    
