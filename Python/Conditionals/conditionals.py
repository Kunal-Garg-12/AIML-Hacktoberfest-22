# Initialise variable marks 
marks = 75

# CONDITIONS
if(marks >= 34 and marks <= 50):    # Check if marks lie between 34 and 50 (both included)
    print("Grade C!")               # If condition true then print

elif(marks > 50 and marks <= 75):   # Else if marks lie between 50 and 75 (75 included)
    print("Grade B!")               # If condition true then print

elif(marks > 75 and marks <= 100):  # Else if marks lie between 75 and 100 (100 included)
    print("Grade A!")               # If condition true then print

elif(marks >= 0 and marks < 34):    # Else if marks lie between 0 and 34 (0 included)
    print("FAIL!")                  # If condition true then print

else:                               # If none of the above condition is true 
    print("Something is wrong!")    # Then print