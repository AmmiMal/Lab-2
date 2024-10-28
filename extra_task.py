from csv import reader


def task():
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        all_tags = set()
        books = dict()
        for row in table:
            if row[8] != 'Кол-во выдач':
                books[row[1].lstrip('#')] = int(row[8])
            tags = row[-1].split('#')
            for tag in tags[1:]:
                all_tags.add(tag.lstrip(' '))
        print(', '.join(all_tags))
        print()
        books = sorted(books.items(), key=lambda item:item[1], reverse=True)
        popular_books = books[:20]
        for number, book in enumerate(popular_books):
            print(f"{number+1}. {book[0]}")


if __name__ == "__main__":
    task()


