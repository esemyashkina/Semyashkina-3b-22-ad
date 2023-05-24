letters = {'vowels': ['у', 'е', 'ё', 'а', 'о', 'э', 'я', 'и', 'ю', 'ы'],
           'consonants': ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х',
                          'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б']}

string = str(input())
vowels_sum, consonants_sum = 0, 0
for letter in string:
  if letter in letters['vowels']:
    vowels_sum += 1
  elif letter in letters['consonants']:
    consonants_sum += 1

print(f'Количество гласных - {vowels_sum}, количество согласных - {consonants_sum}')