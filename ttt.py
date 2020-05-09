from textblob import TextBlob


text = 'Excel is everywhere. It’s basically the default application for data analysis in the workplace, for better or for worse. There are many boring tasks that you may need to take on in your day to day, that leave you thinking, “there must be a better way”. Python is that way!'

print(text)

analysis = TextBlob(text)
print(analysis.sentiment)
print('\n')
