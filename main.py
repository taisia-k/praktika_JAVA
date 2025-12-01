def find_max(n):
    mx = n[0]
    for num in n:
        if num > mx:
            mx = num
    return mx