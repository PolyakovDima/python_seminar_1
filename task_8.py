def can_break_chocolate(n, m, k):
    total_dots = n * m

    if k <= total_dots and (k % n == 0 or k % m == 0):
        return True
    else:
        return False

n = 3
m = 2
k = 4

if can_break_chocolate(n, m, k):
    print("Можно отломить", k, "долек")
else:
    print("Нельзя отломить", k, "долек")
