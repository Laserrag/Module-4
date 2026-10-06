habit_info = ("Reading", "Bathing", "Brushing 2", 7, 20.5)
print(habit_info)

weekly_habits = (1, 0, 1, 1, 0, 1, 1)
print(weekly_habits)

print("Total days tracked:", len(weekly_habits))

print("Day 1 status:", weekly_habits[0])
print("Day 2 status:", weekly_habits[1])
print("Day 3 status:", weekly_habits[2])
print("Day 4 status:", weekly_habits[3])

first_three_days = weekly_habits[0:3]
print("First three days:", first_three_days)
 
weekend_days = weekly_habits[5:7]
print("Weekend days:", weekend_days)
 
weekly_habits = weekly_habits + (1,)
print("After adding one more day:", weekly_habits)
 
completed = weekly_habits.count(1)
missed = weekly_habits.count(0)
 
print("Completed days:", completed)
print("Missed days:", missed)
 
work_done = 0
not_done = 0
 
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        work_done += 1
    else:
        not_done += 1
 
if work_done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")
