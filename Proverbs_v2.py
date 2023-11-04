import random

# Create a dictionary with key-value pairs
my_dict = {
    "A wise son makes a glad father, but a foolish son is the grief of his mother.": 1,
    "Treasures of wickedness profit no one, but righteousness delivers from death.": 2,
    "He becomes poor who deals with an idle hand, but the hand of the diligent makes rich.": 3,
    "He who gathers in summer is a wise son, but he who sleeps at harvest is a shameful one.": 4,
    "He who walks uprightly walks securely, but he who perverts his ways shall come to grief.": 5,
    "": 6,
}

# Get a random key from the dictionary
random_key = random.choice(list(my_dict.keys()))

# Access the corresponding value
random_value = my_dict[random_key]

print("Proverb: ", random_key)

