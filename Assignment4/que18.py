#Given a list of strings, display each string reversed.
#List = [“cat”, “dog”, “bird”]
#Expected output: [‘tac’, ‘god’, ‘drib’]
words = ['cat', 'dog', 'bird']
reversed_list = [word[::-1] for word in words]

print(reversed_list)
