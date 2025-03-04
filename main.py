# Nutritional Tracker

# Function to calculate Total Daily Energy Expenditure (TDEE) based on user details
def calculate_tdee(weight, height, age, gender, activity_level):
    """
    Calculates the Basal Metabolic Rate (BMR) using the Harris-Benedict equation and adjusts it for activity level.
    """
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity multipliers from the lecture on Variables and Control Flow
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    return bmr * activity_multipliers[activity_level]

# Function to calculate macronutrient distribution based on TDEE and user goal
def calculate_macros(tdee, goal):
    """
    Adjusts calorie intake for weight goals and calculates macronutrient targets.
    """
    if goal == "gain":
        tdee += 500
    elif goal == "lose":
        tdee -= 500

    # Macronutrient split (Carbs: 40%, Protein: 30%, Fats: 30%)
    carbs = (tdee * 0.4) / 4  # 4 kcal per gram of carbs
    protein = (tdee * 0.3) / 4  # 4 kcal per gram of protein
    fats = (tdee * 0.3) / 9  # 9 kcal per gram of fats

    return {
        "calories": tdee,
        "carbs": carbs,
        "protein": protein,
        "fats": fats
    }

# Function to track daily nutritional intake
def track_daily_intake():
    """
    Prompts the user to input foods they ate and their nutritional values.
    Uses loops and dictionaries as learned in class.
    """
    daily_totals = {
        "calories": 0,
        "carbs": 0,
        "protein": 0,
        "fats": 0
    }

    while True:
        food = input("Enter food name (or type 'done' to finish): ")
        if food.lower() == 'done':
            break

        # Collecting input values for the food item
        try:
            calories = float(input(f"Enter calories in {food}: "))
            carbs = float(input(f"Enter carbs in {food} (grams): "))
            protein = float(input(f"Enter protein in {food} (grams): "))
            fats = float(input(f"Enter fats in {food} (grams): "))

            # Update daily totals
            daily_totals["calories"] += calories
            daily_totals["carbs"] += carbs
            daily_totals["protein"] += protein
            daily_totals["fats"] += fats
        except ValueError:
            print("Invalid input. Please enter numbers for nutritional values.")

    return daily_totals

# Main function to execute the tracker
def main():
    """
    Orchestrates the program, combining user inputs, calculations, and comparisons.
    """
    print("Welcome to the Nutritional Tracker!")

    # Collect user details
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ").lower()
    goal = input("Enter your goal (maintain, gain, lose): ").lower()

    # Calculate suggested TDEE and macros
    tdee = calculate_tdee(weight, height, age, gender, activity_level)
    suggested_macros = calculate_macros(tdee, goal)

    print("\nSuggested daily targets:")
    print(f"Calories: {suggested_macros['calories']:.2f} kcal")
    print(f"Carbs: {suggested_macros['carbs']:.2f} g")
    print(f"Protein: {suggested_macros['protein']:.2f} g")
    print(f"Fats: {suggested_macros['fats']:.2f} g")

    # Track daily food intake
    print("\nNow, let's track your daily food intake.")
    daily_totals = track_daily_intake()

    print("\nYour daily totals:")
    print(f"Calories: {daily_totals['calories']:.2f} kcal")
    print(f"Carbs: {daily_totals['carbs']:.2f} g")
    print(f"Protein: {daily_totals['protein']:.2f} g")
    print(f"Fats: {daily_totals['fats']:.2f} g")

    # Compare intake with suggested targets
    print("\nComparison with suggested targets:")
    print(f"Calories: {'Above' if daily_totals['calories'] > suggested_macros['calories'] else 'Below'} target")
    print(f"Carbs: {'Above' if daily_totals['carbs'] > suggested_macros['carbs'] else 'Below'} target")
    print(f"Protein: {'Above' if daily_totals['protein'] > suggested_macros['protein'] else 'Below'} target")
    print(f"Fats: {'Above' if daily_totals['fats'] > suggested_macros['fats'] else 'Below'} target")

if __name__ == "__main__":
    main()
