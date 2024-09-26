#범위내부의 정수를 모두 더하는 함수

def sum_all(start,end):
    output = 0
    for i in range(start, end +1):
        output += i

    return output

print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))