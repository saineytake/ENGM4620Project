# Nutritional Tracker

A Python script that runs in the terminal and helps you track your nutrition each day and keep you accountable to your daily calories and macros (nutrients fats/protein/carbohydrates) goal. 

Developed by Sainey Take (B00861683) and Anne Taha (B00866148)

## Functionalities

1. The user enters basic information (weight, height, age, gender, activity level, and goal)
2. The user is presented with their TDEE (Total Daily Energy Expenditure), calculated with the Harris-Benedict formula.
3. The user is presented with their macro target that meets their caloric goal, simply straying from a 40/30/30 split of the macros (calories, carbs, protein, fats).
4. The user logs their food and nutrition by providing the nutrient facts for each food item and the user logs the food they ate, and the system does the rest for the user, including calculating the total intake and comparing it to the user's total caloric and macro targets.
5. Finally, the system saves the running totals of that day to a file called `log.csv` script file to refer to another day.

## Resources Used

- Written in Python 3
- Used OOP with 2 main classes `UserInfo` and `MacroLog`
- File I/O writing log to the log.csv file
- Error handling with try/except`

## Future Improvements

- Plots data visualizations of daily intake with `matplotlib`
- Support for logging multiple days and saving history
- Implement a basic GUI with `Tkinter`
- Features to save/load user profiles for repeat user.

Straightforward. Efficient. Built for practical use.
