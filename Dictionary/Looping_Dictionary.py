# Looping trough all key-value pairs
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

# Create two variables to store the key and the value
for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)

# Another example
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

# Looping Through All the Keys in a Dictionary
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Is the same as
for name in favorite_languages:
    print(name.title())

# Another example
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

# Check if one key is not in the dictionary
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Dictionary sorted
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
