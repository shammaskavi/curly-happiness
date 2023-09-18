# 1a Find the average of two numbres

# The Boring way
m1 = int(input("Enter marks for IA1: "))
m2 = int(input("Enter marks for IA2: "))
m3 = int(input("Enter marks for IA3: "))

min = min(m1, m2, m3)
sum = (m1 + m2 + m3) - min
max = max(m1, m2, m3)
best = sum - min

print(f"The average marks are: {sum/2}")
