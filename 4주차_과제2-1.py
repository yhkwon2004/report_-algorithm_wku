def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

def calculate_average(start=0, end=100, step=1):
    total_sum = sum_all(start, end, step)
    count = (end - start) // step + 1
    average = total_sum / count
    return total_sum, average

total_A, average_A = calculate_average(0, 100, 10)
print("A. 총합:", total_A, "평균:", average_A)

total_B, average_B = calculate_average(end=100)
print("B. 총합:", total_B, "평균:", average_B)

total_C, average_C = calculate_average(end=100, step=2)
print("C. 총합:", total_C, "평균:", average_C)
