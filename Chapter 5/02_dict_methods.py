marks = {
    "Rishi": 100,
    "Aarav": 92,
    "Rahul": 67,
    0 : "Priya"
}


# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Priya": 98, "Renuka": 101})
print(marks)

print(marks.get("Aarav9")) # Return None
print(marks.get["Aarav9"]) # Return an error