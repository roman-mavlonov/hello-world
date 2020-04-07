weight = int(input("Weight: "))
unit = input("(L)bs of (K)g? ")
if unit.upper() == "L":
    result = 0.4535929094356397 * weight
    print(f"{result} kg")
elif unit.upper() == "K":
    result = weight / 0.4535929094356397
    print(f"{result} lbs")

