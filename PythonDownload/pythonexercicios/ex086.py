a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        a[l][c] = int(input(f"Digite um valor para:[{l},{c}] "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{a[l][c]:^5}]", end='')
    print()
