
# Nutritional Tracker
# main.py
# Sainey Take (B00861683) Anne Taha (B00866148)

import csv

# this class is just for storing the person's info and calculating stuff like TDEE
class UserInfo:
    def __init__(self, weight, height, age, gender, activity_level, goal):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.lower()
        self.activity_level = activity_level.lower()
        self.goal = goal.lower()

    # tdee = how much energy you burn in a day
    def get_tdee(self):
        if self.gender == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

        # multiplier depends on how active you are
        activity = {
            "sedentary": 1.2,
            "lightly active": 1.375,
            "moderately active": 1.55,
            "very active": 1.725,
            "extra active": 1.9
        }

        # just use sedentary if something wrong
        multiplier = activity.get(self.activity_level, 1.2)
        return bmr * multiplier

    def get_macro_goals(self):
        tdee = self.get_tdee()

        # bump up/down depending on goal
        if self.goal == "gain":
            tdee += 500
        elif self.goal == "lose":
            tdee -= 500

        # 40/30/30 split from google
        carbs = (tdee * 0.4) / 4
        protein = (tdee * 0.3) / 4
        fats = (tdee * 0.3) / 9

        return {
            "calories": round(tdee, 2),
            "carbs": round(carbs, 2),
            "protein": round(protein, 2),
            "fats": round(fats, 2)
        }

# used this to keep track of what user ate in a day
class MacroLog:
    def __init__(self):
        self.my_totals = {
            "calories": 0,
            "carbs": 0,
            "protein": 0,
            "fats": 0
        }

    def add_food(self, name, cal, carb, prot, fat):
        self.my_totals["calories"] += cal
        self.my_totals["carbs"] += carb
        self.my_totals["protein"] += prot
        self.my_totals["fats"] += fat

    def save_csv(self, filename="log.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Calories", "Carbs", "Protein", "Fats"])
            writer.writerow([
                self.my_totals["calories"],
                self.my_totals["carbs"],
                self.my_totals["protein"],
                self.my_totals["fats"]
            ])

    def compare(self, targets):
        print("\nCompare to Target:")
        # not looping fancy here
        if self.my_totals["calories"] > targets["calories"]:
            print("Calories: Above")
        else:
            print("Calories: Below")

        if self.my_totals["carbs"] > targets["carbs"]:
            print("Carbs: Above")
        else:
            print("Carbs: Below")

        if self.my_totals["protein"] > targets["protein"]:
            print("Protein: Above")
        else:
            print("Protein: Below")

        if self.my_totals["fats"] > targets["fats"]:
            print("Fats: Above")
        else:
            print("Fats: Below")

# runs the whole program
def run_tracker():
    print("Welcome to the ENGM4620 Nutritional Tracker")

    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (cm): "))
        age = int(input("Age: "))
        gender = input("Gender (male/female): ")
        activity = input("Activity level (sedentary/light/moderate/very/extra): ")
        goal = input("Goal (maintain/gain/lose): ")
    except:
        print("Something went wrong. Try again.")
        return

    user = UserInfo(weight, height, age, gender, activity, goal)
    goals = user.get_macro_goals()

    print("\nYour Daily Goals:")
    print("Calories:", goals["calories"])
    print("Carbs:", goals["carbs"], "g")
    print("Protein:", goals["protein"], "g")
    print("Fats:", goals["fats"], "g")

    log = MacroLog()

    print("\nType foods you ate today. 'done' when finished.")
    while True:
        food = input("Food: ")
        if food.lower() == "done":
            break
        try:
            cal = float(input("Calories: "))
            carb = float(input("Carbs (g): "))
            prot = float(input("Protein (g): "))
            fat = float(input("Fats (g): "))
            log.add_food(food, cal, carb, prot, fat)
        except:
            print("bad input. skipping that one.")

    print("\nToday's Total:")
    print("Calories:", log.my_totals["calories"])
    print("Carbs:", log.my_totals["carbs"])
    print("Protein:", log.my_totals["protein"])
    print("Fats:", log.my_totals["fats"])

    log.compare(goals)
    log.save_csv()
    print("(Saved your log to file too)")

if __name__ == "__main__":
    run_tracker()
