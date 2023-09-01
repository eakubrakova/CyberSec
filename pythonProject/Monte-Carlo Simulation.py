from random import randint
trials = 100 0000
success = 0
for trial in range(trials):
    diff_numbers = set()
    for rolls in range(6):
        roll = randint(1, 6)
        diff_numbers.add(roll)
    if len(diff_numbers) == 6:
        success += 1
print(success/trials)


