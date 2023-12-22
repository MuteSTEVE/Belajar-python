n = 5
sym = '*'

# left increase triangle
for i in range(n):
    for j in range(i+1):
        print(sym, end=' ')
    print()
print()

# left decrease triangle
for i in range(n):
    for j in range(i, n):
        print(sym, end=' ')
    print()
print()

# right increase triangle
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i+1):
        print(sym, end=' ')
    print()
print()

# right decrease triangle
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print(sym, end=' ')
    print()
print()

# hill 
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print(sym, end=' ')
    for j in range(i+1):
        print(sym, end=' ')
    print()
print()

# arrow
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
        print(sym, end=' ')
    for j in range(i, n):
        print(sym, end=' ')
    print()
print()

# diamond
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print(sym, end=' ')
    for j in range(i+1):
        print(sym, end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
        print(sym, end=' ')
    for j in range(i, n):
        print(sym, end=' ')
    print()
