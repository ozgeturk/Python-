bob, sam = input().split()
if bob == "betrayal":
    if sam == "betrayal":
        bob_punishment = 2
        sam_punishment = 2
    elif sam == "silence":
        bob_punishment = 0
        sam_punishment = 3
elif bob == "silence":
    if sam == "betrayal":
        bob_punishment = 3
        sam_punishment = 0
    elif sam == "silence":
        bob_punishment = 1
        sam_punishment = 1

print(bob_punishment, sam_punishment)