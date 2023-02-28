print("Enter the numbers in the set to finish typing write '!':")

number = str(input())
number_set = set()
number_massive = []
binary_massive = []
minus = ""

while number != "!":
    try:
        if int(number) not in number_set:
            number_massive.append(number)
            number_set.add(int(number))
    except ValueError:
        print("You should only use numbers!")
        exit(1)

    number = str(input())

def binary(number_from_massive):
    if number_from_massive < 2:
        return number_from_massive
    return (number_from_massive % 2) + binary(number_from_massive // 2) * 10

print("Look, this is beatifull:")
for i in range(len(number_massive)):

    if (int(number_massive[i])) < 0 :
        number_massive[i] = str(abs(int(number_massive[i])))
        minus = "-"

    binary_massive.append(str(binary(int(number_massive[i]))))
    print(minus+number_massive[i]+" --> "+minus+binary_massive[i])
    minus = ""
