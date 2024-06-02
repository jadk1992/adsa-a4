
# Convert letters into their respective numbers
def letter_to_number(letter):
    if letter.isupper():
        return ord(letter) - ord("A")
    else:
        return ord(letter) - ord("a") + 26


totalcost = 0


# Taking in inputs
input = input()

country_str, build_str, destroy_str = input.split()

# Splitting inputs into the 3 matrices
country = [[int(x) for x in str(part)] for part in country_str.split(",")]
build = [[letter_to_number(x) for x in part] for part in build_str.split(",")]
destroy = [[letter_to_number(x) for x in part] for part in destroy_str.split(",")]


print(totalcost)

# 111,111,111 ABC,ABC,ABC abc,abc,abc