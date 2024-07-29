Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Temp = []
i = 0
while i < len(Days):
    day = Days[i]
    while True:
            temp = float(input(f"Enter the Temperature of {day}: "))
            Temp.append(temp)
            break
i += 1

Total_temp = sum(Temp)
Avg_temp = Total_temp / len(Days)

print(f"The average temperature for the week is: {Avg_temp:.2f}")
