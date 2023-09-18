def check_rhythm(stanza):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

    syllables_count = sum(1 for char in stanza[0] if char in vowels)

    for phrase in stanza[1:]:
        if sum(1 for char in phrase if char in vowels) != syllables_count:
            return "Пам парам"

    return "Парам пам-пам"

# Считываем стихотворение с клавиатуры
input_text = input("Введите стихотворение: ").split()
output_text = check_rhythm(input_text)
print(output_text)
