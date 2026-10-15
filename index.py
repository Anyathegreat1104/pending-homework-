maths=int(input("Enter maths marks: "))
science=int(input("Enter science marks : "))
english=int(input("Enter english marks : "))
hindi=int(input("Enter hindi marks: "))
socialscience=int(input("Enter socialscience marks : "))

total = maths+english+hindi+science+socialscience
average = total / 5
percentage = (total / 500) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)