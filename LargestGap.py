#start of Coding challenge

def main():  
    input1 = [9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]
    input2 = [14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]
    input3 = [13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]

    print(findgap(input1))
    print(findgap(input2))
    print(findgap(input3))

def findgap(listin) -> int:
    tempset = set(listin)
    templist = list(tempset)
    templist = sorted(templist)
    print(templist)
    end = len(templist)
    gap = 0
    for i in range(end-1):
        if templist[i+1] - templist[i] > gap:
            gap = templist[i+1] - templist[i]
    return gap

if __name__ == "__main__":
    main()
