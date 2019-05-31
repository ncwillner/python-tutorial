#WEIGHT TRANSFORMER
weight = int(input("Weight: "))
unit = input("P(Lbs) or K(kg)?: ")
if unit.upper() == "P":
    switch = weight * 0.45
    print(f"you have {switch} kg")
else:
    switch = weight / 0.45
    print(f"you have {switch} pounds")