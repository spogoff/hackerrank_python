if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x +=1
    y +=1
    z +=1

    my_list = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k !=n]

    print(my_list)
