print("Break Example:")

for i in range(1, 11):
    if i == 5:
        break
    print(i)


print("\nContinue Example:")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


print("\nPass Example:")

for i in range(1, 11):
    if i == 5:
        pass
    print(i)
