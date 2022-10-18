import tkinter as tk  #for creating tk interface
import nltk 
from textblob import TextBlob  #for sentiment analysis
from newspaper import Article

def summarize():

    #nltk.download('punkt')

    url = utext.get('1.0', 'end').strip()

    #passing url in article object
    article = Article(url)
    #downloading the data
    article.download()
    #parsing the data: to divide a sentence into grammatical parts and identify the parts and their relations to each other
    article.parse() 
    #calling nlp method
    article.nlp()
    
    title.config(state='normal')
    #print(f'Title: {article.title}')
    author.config(state='normal')
    #print(f'Authors: {article.authors}')
    publication.config(state='normal')
    #print(f'Date of Pub: {article.publish_date}')
    summary.config(state='normal')
    #print(f'Summary: {article.summary}')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    #Sentiment Analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    

#Making tk-GUI 
root = tk.Tk()
root.title('News Summarizer Project: Aviraj')
root.geometry('1200x600')

#Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=2, width=150)
title.config(state='disabled', bg='white')
title.pack()
#Author
alabel = tk.Label(root, text='Authors')
alabel.pack()

author = tk.Text(root, height=2, width=150)
author.config(state='disabled', bg='white')
author.pack()
#Publisher
plabel = tk.Label(root, text='Publishing Date')
plabel.pack()

publication = tk.Text(root, height=2, width=150)
publication.config(state='disabled', bg='white')
publication.pack()
#Summary
slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=150)
summary.config(state='disabled', bg='white')
summary.pack()
#Sentiment
salabel = tk.Label(root, text='Sentiment Analysis')
salabel.pack()

sentiment = tk.Text(root, height=2, width=150)
sentiment.config(state='disabled', bg='white')
sentiment.pack()
#URL
ulabel = tk.Label(root, text='Sentiment Analysis')
ulabel.pack()

utext = tk.Text(root, height=2, width=150)
#utext.config not required
utext.pack()

#Button
btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

root.mainloop()
