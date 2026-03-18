# The volume of a sphere with radius 5
r = 5
v = 4/3 * 3.14 * r**3
print("The volume of a sphere with radius 5 is:", v)

# The total wholesale cost
cover_price = 24.95
discount = 0.4
num_copies = 60
wholesale_cost = (cover_price * (1 - discount) * num_copies) + (0.75 * (num_copies - 1))+ 3
print("The total wholesale cost for 60 copies is:", wholesale_cost)

# The time I get home for breakfast
leave_time = 6 * 3600 + 52 * 60
easy_pace = (8 * 60 + 15) * 2
tempo_pace = (7 * 60 + 12) * 3
total_time = leave_time + easy_pace + tempo_pace
hour = total_time // 3600
minute = (total_time % 3600) // 60
print(f"Return home time: {hour}:{minute:02d}")




