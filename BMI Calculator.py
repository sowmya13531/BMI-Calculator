def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "UnderWeighted"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweighted"
    else:
        category = "Obese"
    return bmi, category

def main():
    try:
        weight = float(input("Enter your weight in Kilograms: "))
        height = float(input("Enter your hieight in meters: "))
        if weight <= 0 or height <= 0:
            print("Enter valid Data")
            return
        bmi, category = calculate_bmi(weight, height)
        print(f"\n Your BMI is: {bmi:.2f}")
        print(f"\n Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values")
if __name__ == "__main__":
    main()
