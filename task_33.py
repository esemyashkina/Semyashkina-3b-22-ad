string = str(input())
letters = set(list(string))
for letter in letters:
  print(f'Символ {letter} встречается в строке {string} {string.count(letter)} раз')