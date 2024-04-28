import math


def find_n1_n2(t, x, y):
    # Check if t is divisible by gcd(x, y)
    gcd_xy = math.gcd(x, y)
    if t % gcd_xy != 0:
        return [-1, -1]  # Not possible to express t as n1*x + n2*y

    # Solve for n1 and n2 using Bézout's identity
    n1, n2 = 0, 0
    max_val = max(x, y)
    min_val = min(x, y)
    while True:
        if (t - n1 * min_val) % max_val == 0:
            n2 = (t - n1 * min_val) // max_val
            break
        n1 += 1

    return [n1, n2]


# Example usage
t = int(input("Enter t: "))
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = find_n1_n2(t, x, y)
print(result)
