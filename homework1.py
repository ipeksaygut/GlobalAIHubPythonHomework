list=list()
for i in range(5):
    value=input("Enter a value:")
    list.append(value)

for value in list:
    try:
        value=int(value)
        value = float(value)
        value = str(value)
    except ValueError:
        print(f"value:{value}   type:{type(value)}")
    if value==int(value):
        value = int(value)
    elif value==int(value) and value==float(value):
        value = float(value)
    elif value==str(value):
        value = str(value)

print(f"value:{value}   type:{type(value)}")


