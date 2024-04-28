import math


def find_n1_n2(target, x, y):
    # Check if target is divisible by gcd(x, y)
    gcd_xy = math.gcd(x, y)
    if target % gcd_xy != 0:
        return [-1, -1]  # Not possible to express t as n1*x + n2*y

    # Solve for n1 and n2 using Bézout's identity
    n1, n2 = 0, 0
    min_val = min(x, y)
    max_val = max(x, y)
    while True:
        if (target - n1 * min_val) % max_val == 0:
            n2 = (target - n1 * min_val) // max_val
            break
        n1 += 1

    return [n1, n2]


# Example usage
targetValue = int(input("Enter target: "))
fx = int(input("Enter x: "))
sy = int(input("Enter y: "))

result = find_n1_n2(targetValue, fx, sy)
print(result)
