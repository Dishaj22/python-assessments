word = ["apple", "banana", "cherry", "date", "elderberry"]
longest = max(word, key=lambda word: len(word))
print("longest word:", longest)