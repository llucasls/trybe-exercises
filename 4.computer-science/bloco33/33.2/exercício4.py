import json, csv


with open("books.json") as books_file:
    books = json.load(books_file)

total_categories = []
categories_frequency = {}
categories_percent = {}
total_books = len(books)

for book in books:
    for book_category in book["categories"]:
        total_categories.append(book_category)

total_categories = sorted(total_categories)

for category in total_categories:
    categories_frequency[category] = 0

for category in total_categories:
    categories_frequency[category] += 1

for category in categories_frequency:
    categories_percent[category] = categories_frequency[category] / total_books

with open("book_categories.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file, delimiter = ",", quotechar = '"')
    header = ("categoria","porcentagem")
    writer.writerow(header)
    for category in categories_percent:
        result = (category, categories_percent[category])
        writer.writerow(result)
