sentence  = "Hey your name is {1} and you are from {0}."
country = "Indonesia"
name = "Jerry"

print(sentence.format(country, name))

# F strings
print(f"Hey your name is {name} and Your are from {country}")
txt = "For only {price:.2f} Euro!"
print(txt.format(price = 37.0999))

price = 21.7999
txt = f"For only {price:.2f} Euro!"
print(txt)

print(f"{3 * 32}")
print(type(f"{7 * 12}"))

