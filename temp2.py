def calculate_total_cost(credits, in_state_resident, on_campus_resident, housing_type, books_cost, miscellaneous_cost):
  """
  Calculates the total cost of attending Central Maine Community College for one year.

  Args:
    credits: The number of credits the student is taking.
    in_state_resident: True if the student is a resident of Maine, False otherwise.
    on_campus_resident: True if the student is living on campus, False otherwise.
    housing_type: The type of on-campus housing (Rancourt Hall, Fortin Hall, or Apartment).
    books_cost: The estimated cost of books and supplies.
    miscellaneous_cost: The estimated cost of miscellaneous expenses.

  Returns:
    The total cost of attending Central Maine Community College for one year.
  """

  # Tuition and fees
  tuition = 94 * credits
  if in_state_resident:
    mandatory_fees = 984
  else:
    mandatory_fees = 984

  # On-campus housing costs
  if on_campus_resident:
    if housing_type == "Rancourt Hall":
      housing_cost = 10000
    elif housing_type == "Fortin Hall":
      housing_cost = 9570
    elif housing_type == "Apartment":
      housing_cost = 11500
    else:
      raise ValueError("Invalid housing type: {}".format(housing_type))
  else:
    housing_cost = 0

  # Total cost
  total_cost = tuition + mandatory_fees + housing_cost + books_cost + miscellaneous_cost

  return total_cost

# Get user input
credits = int(input("Enter the number of credits you are taking: "))
in_state_resident = input("Are you a resident of Maine? (y/n): ") == "y"
on_campus_resident = input("Are you living on campus? (y/n): ") == "y"
if on_campus_resident:
  housing_type = input("What type of on-campus housing will you be living in? (Rancourt Hall, Fortin Hall, or Apartment): ")
else:
  housing_type = None
books_cost = float(input("Enter the estimated cost of books and supplies: "))
miscellaneous_cost = float(input("Enter the estimated cost of miscellaneous expenses: "))

# Calculate and print the total cost
total_cost = calculate_total_cost(credits, in_state_resident, on_campus_resident, housing_type, books_cost, miscellaneous_cost)
print("The total cost of attending Central Maine Community College for one year is: ${:.2f}".format(total_cost))
