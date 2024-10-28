from csv import reader
import random

def tasks():
    counter = 0
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            if row[1] != 'Название':
                if len(row[1]) > 30:
                    counter += 1
        print(counter)


    flag = 0
    search = input('Search for: ')
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            author, author_fio, year = row[3], row[4], row[6][6:10]
            if (year == '2015' or year == '2018') and (search == author or search == author_fio):
                print(f"Найдена кника {year} года. Автор: {author_fio}; Название книги: {row[1]}; Формат книги: {row[2]}")
                flag = 1
        if flag == 0:
            print('Nothing found.')


    output = open('result_3_task.txt', 'w')
    with open('books.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        new_table=[]
        for row in table:
            new_table.append(row)
        for i in range(20):
            number = random.randint(1,len(new_table)-1)
            author_fio, year = new_table[number][4], new_table[number][6][6:10]
            output.write(f"{author_fio}. {row[1]} - {year}\n")

    output.close()


if __name__ == "__main__":
    tasks()

