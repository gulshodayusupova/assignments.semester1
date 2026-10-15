def classify(value):
    if value < 748:
        return "Below range"
    elif value <= 752:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result
count = int(input("Enter the number of paint tins: "))
total = 0
below = 0
in_range = 0
above = 0
for i in range(count):
    volume = int(input("Enter the paint tin volume: "))
    result = classify(volume)
    print(result)
    total += volume
    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range += 1
    else:
        above += 1
average = calculate_average(total, count)
print(f"Total volume: {total} ml")
print(f"Average volume: {average} ml")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")
