def basic_rental(num_days: int):
    amount = num_days * 1000
    if num_days >= 7:
        return amount - 1500
    elif num_days >= 3 and num_days <= 6:
        return amount - 500
    return amount

def calculate_extras(insurance, gps, num_days):
    extra_amount = 0
    if insurance:
        extra_amount += 200 * num_days
    if gps:
        extra_amount += 50 * num_days
    return extra_amount

def generate_invoice(num_days, wants_insurance, wants_gps):
    rental_amount = basic_rental(num_days)
    extra_amount = calculate_extras(wants_insurance, wants_gps, num_days)
    return rental_amount + extra_amount

print("Welcome to the Car Rental System!")

rental_days = int(input("How many days will you rent the car for? "))

insurance_response = input("Would you like insurance? (yes/no): ").lower()
if insurance_response == "yes":
    has_insurance = True
else:
    has_insurance = False

gps_response = input("Would you like GPS? (yes/no): ").lower()
if gps_response == "yes":
    has_gps = True
else:
    has_gps = False

total_cost = generate_invoice(rental_days, has_insurance, has_gps)

print(f"Transaction complete! Total amount due: {total_cost} TL")
