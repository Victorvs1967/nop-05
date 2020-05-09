from textblob import TextBlob


text = 'Для начала, мы выведем самые последние твиты, связанные с нашим ключевым словом. После мы используем textblob, чтобы определить тональность каждого отдельного твита и выведем её тоже. Посмотрим, что сказал глава Apple Тим Кук.'

print(text)

analysis = TextBlob(text)
print(analysis.sentiment)
print('\n')
