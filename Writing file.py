#   employees = ["Shahid", "Faizan", "Ismail"]
#   txt_data = ("I like Pizza!")

# IT IS MAINLY USED TO .JSON FILE
# import json
# import csv
# students = { "name": "Shahid khan", "class": "3rd year B.E","College": "GCE"}
# employees = [["Name", "Age", "Job"],["Shahid", "21", "Developer"],["Faizan", "21", "Developer"],["Ismail", "21", "Developer"]]
file_path ="text.csv", "text.json", "text.csv"

try:
    with open(file_path,"w") as file:
       # This is for .csv file: writer = csv.writer(file)  # for row in employees: writer.writerow(row)
# This for .json file: json.dump(students, file, indent=4)
# This is for .txt file: for student in students: # file.write(student + "\n")
        print(f"The file {file_path} was created successfully")
except FileExistsError:
    print("The file already exists")






