def get_divs(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs

def find_gcd(a, b):
    divs_a = get_divs(a)
    divs_b = get_divs(b)
    common_divs = set(divs_a) & set(divs_b)
    max_gcd = max(common_divs)
    return divs_a, divs_b, common_divs, max_gcd

x = 60
y = 28
divs_x, divs_y, comm_divs, max_div = find_gcd(x, y)

print(f"{x} 약수: {divs_x}")
print(f"{y} 약수: {divs_y}")
print(f"공통 약수: {comm_divs}")
print(f"{x}와 {y}의 최대 공약수 {max_div}")
