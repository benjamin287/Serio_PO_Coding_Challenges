import math
import datetime

def main():  
    input1 = ([5, 5, 10, 10, 15, 15, 20, 20], 120) 
    input2 = ([2, 3, 8, 6, 5, 12, 10, 18], 64)
    input3 = ([5, 5, 10, 10, 25, 15, 20, 20], 120) 
    input4 = ([5, 5, 10, 10, 15, 15, 20], 120)
    input5 = ([5, 5, 10, 10, 15, 15, 20, 20], 130)

    print(qualified(input1))
    print(qualified(input2))
    print(qualified(input3))
    print(qualified(input4))
    print(qualified(input5))

    input6 = (3, 2020)
    input7 = (10, 2017) 
    input8 = (1, 1985)

    print(has_friday_13(input6))
    print(has_friday_13(input7))
    print(has_friday_13(input8))


def qualified(listin) -> str:
    questions = listin[0]
    decision = 'qualified'
    if len(questions) != 8:
        decision = 'disqualified'
    elif listin[1] > 120:
        decision = 'disqualified'
    else:
        for num in range(8):
            if  questions[num] > math.ceil((num+1)/2)*5:
                decision = 'disqualified'
    return decision
    
def has_friday_13(listin) -> bool:
    if datetime.datetime(listin[1], listin[0], 13).weekday() == 4:
        output = True
    else:
        output = False
    return output

if __name__ == "__main__":
    main()