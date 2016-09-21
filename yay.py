def yay(answer1, answer2):
    final=answer1+answer2
    return final
def sub(answer1, answer2):
    final=answer1-answer2
    return final
def multiply(answer1, answer2):
    final=answer1*answer2
    return final
def divise(answer1, answer2):
    final=answer1/answer2
    return final
print('what do you want the first number to be?')
answer1=int(input())
print('what do you want the second number to be?')
answer2=int(input())
print('what function do you want to use?')
print('addition')
print('subtration')
print('multiplication')
print('division')
answer3=input()
if answer3=='addition':
    print(yay(answer1, answer2))
if answer3=='subtraction':
    print(sub(answer1, answer2))
if answer3=='multiplication':
    print(multiply(answer1, answer2))
if answer3=='division':
    print(divise(answer1, answer2))
