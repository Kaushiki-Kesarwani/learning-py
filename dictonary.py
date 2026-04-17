dict = {
    "name": "palak",
    "age": 19
    }

print(dict)
# info["name"] = "hey"
# print(info)


#nested dict

student ={
    "name":"kaushiki",

    "colors" : {
        "color1": "red",
        "color2":"blue",
        "color3":"black"

    }
}

print(student["colors"]["color2"])
# print(student.items())
# print(student.get("name"))
# print(student.keys())
# print(student.values())
student.update({"name":"palak"})
print(student.values())

