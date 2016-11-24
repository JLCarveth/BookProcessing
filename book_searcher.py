# Course: IT1 1120
# Assignment #2
# Carveth, John
# 8645004
################################################################################
import sys

with open('NYT-bestsellers.txt') as file:
    lines = file.readlines()

books = []
for x in range(len(lines)):
    book = list(lines[x].split('\t'))
    for y in range(len(book)):
        book[y] = book[y].strip()
    books.append(book)

def wait_to_continue():
    '''
    None->None
    This function is used after any of the primary functions are used. It simply
    waits for the user to hit enter, then calls main() when they do.
    '''
    print('\n'*2)
    a = input('Press Enter to continue...')
    print('\n'*2)
    main()

def year_range(year1, year2):
    '''
    (Int, Int)
    Takes as input two integers of length 4, and searches the book matrix for
    matching entries between the years.
    Ex. year_range(1970,1973) would return all books from 1970, 1971, 1972, and
    1973.
    '''
    years = []
    temp_list = []
    for year in range(year1, year2+1):
        years.append(str(year))
    
    for y in years:
        for x in range(len(books)):
            if y in books[x][3]:
                temp_list.append(books[x][0]+' by '+books[x][1]+', ('+books[x][3]+')')
    if(len(temp_list) == 0):
        print('No books were found for this criteria.')
    else:
        for z in temp_list:
            print(z)
    wait_to_continue()

def month_year(month, year):
    '''
    (int, int)
    Takes as input a month integer of length 2, where 1 <= month <= 12, and a
    year integer of 4 digits in length. Returns any books from the list with a
    date within the parameters. if no books are found, that is relayed to the
    user.
    '''
    temp_list = []
    for x in range(len(books)):
        slash_index = books[x][3].index('/')
        if((str(year) in books[x][3]) and \
           (books[x][3][0:slash_index] == str(month))):
            temp_list.append(books[x])
    print('\n')
    
    if(len(temp_list) < 1):
        print('Sorry, no books were found at this date.')
    else:
        for y in range(len(temp_list)):
            print(temp_list[y][0],'by',temp_list[y][1]+', ('+temp_list[y][3]+')')
    wait_to_continue()

def search_author(author):
    '''
    (Str)
    Prompt the user for a string, then display all books whose author’s
    name contains that string (regardless of case).
    '''
    author = author.lower()
    temp_list = []
    
    for x in range(len(books)):
        if(author in books[x][1].lower()):
            temp_list.append(books[x])
    if(len(temp_list) == 0):
        print('Sorry, no books by the author '+author+' were found.')
    else:
        for y in range(len(temp_list)):
            print(temp_list[y][0],'by',temp_list[y][1]+', ('+temp_list[y][3]+')')
    wait_to_continue()

def search_title(title):
    '''
    (Str)
    Prompt the user for a string, then display all books whose title’s
    contain that string (regardless of case).
    '''
    title = title.lower()
    temp_list = []
    
    for x in range(len(books)):
        if(title in books[x][0].lower()):
            temp_list.append(books[x])
    if(len(temp_list) == 0):
        print('Sorry, no books with the title '+title+' were found.')
    else:
        for y in range(len(temp_list)):
            print(temp_list[y][0],'by',temp_list[y][1]+', ('+temp_list[y][3]+')')
    wait_to_continue()

def min_bestsellers(x):
    '''
    (Int)
    Find all authors with at least x bestsellers.
    '''
    temp_list = []
    for a in range(len(books)):
        count = sum(b.count(books[a][1]) for b in books)
        if(count > x):
            temp_list.append(books[a][1]+':'+str(count))
    
    temp_list = set(temp_list)
    temp_list = list(temp_list)
    for c in range(1,len(temp_list)):
        index = temp_list[c].index(':')
        print(str(c)+'. '+str(temp_list[c][0:index])+'\t'+str(temp_list[c][index+1:]))
    wait_to_continue()

def max_bestsellers(x):
    '''
    (Int)
    Finds x authors with the most bestselling books.
    '''
    temp_list = []

    for a in range(len(books)):
        count = sum(b.count(books[a][1]) for b in books)
        if([count, books[a][1]] not in temp_list):
            temp_list.append([count, books[a][1]])
        else:
            pass

    temp_list.sort(reverse=True)
    for c in range(1,x):
        print(str(c)+ '. '+temp_list[c][1]+'\t'+str(temp_list[c][0]))
    wait_to_continue()

def main():
    '''
    None->None
    Main Function.
    '''
    
    print('='*45)
    print('What would you like to do? Enter 1, 2, 3, 4, 5, 6, or Q for answer.')
    print('1. Look up year range')
    print('2. Look up month/year')
    print('3. Search for author')
    print('4. Search for title')
    print('5. Number of Authors with at least x bestsellers')
    print('6. List y authors with the most bestsellers')
    print('Q: Quit')
    print('='*45)

    running = True
    
    while running:
        user_input = input('Answer (1,2,3,4,5,6,Q or q):')
        user_input = user_input.lower()
        if(user_input == 'q'):
            print('Quitting...')
            print('Goodbye!')
            sys.exit(0)
        elif(user_input == '1'):
            print('Look up year range:')
            valid1 = False
            valid2 = False
            while valid1 is False:
                try:
                    y1 = int(input('Enter the beginning year:\n'))
                    valid1 = True
                except ValueError:
                    print('Must be a four digit number.')
            if((y1 // 1000) < 1):
                valid1 = False
                print('Must be four digits long. Ex. 2010, 1967, etc.')
            else:
                valid1 = True
                pass
            
            while valid2 is False:
                try:
                    y2 = int(input('Enter the ending year:\n'))
                    valid2 = True
                except ValueError:
                    print('Must be a four digit number.')
            if((y2 // 1000) < 1):
                valid2 = False
                print('Must be four digits long. Ex. 2010, 1967, etc.')
            else:
                valid2 = True
                pass
            running = False
            year_range(y1,y2)      
        elif(user_input == '2'):
            print('Look up month/year')
            valid1 = False
            valid2 = False
            while valid1 is False:
                try:
                    mm = int(input('Enter month (as an integer 1-12): '))
                    if(mm < 1) or (mm > 12):
                        print('Month must be between 1 and 12.')
                        valid1 = False
                    else:
                        valid1 = True
                except ValueError:
                    print('Month must be integer between 1-12.')
            
            while valid2 is False:
                try:
                    year = int(input('Enter year: '))
                    if((year // 1000) < 1):
                        print('Year must be integer with 4 digits.')
                        valid2 = False
                    else:
                        valid2 = True
                except ValueError:
                    print('Year must be integer with 4 digits.')
            
            running = False
            month_year(mm, year)
            wait_to_continue()
        elif(user_input == '3'):
            author = input('Enter an author\'s name (or part of a name): ')
            search_author(author)
        elif(user_input == '4'):
            title = input('Enter a book title (or part of a title): ')
            search_title(title)
        elif(user_input == '5'):
            valid = False
            while valid is False:
                try:
                    x = int(input('Enter an integer larger than zero: '))
                    if(x < 1):
                        valid = False
                        print('Number must be at least 1.')
                    else:
                        valid = True
                except ValueError:
                    print('Number must be an integer.')
            running = False
            min_bestsellers(x)
        elif(user_input == '6'):
            valid = False
            while valid is False:
                try:
                    x = int(input('Enter an integer larger than zero: '))
                    if(x < 1):
                        valid = False
                        print('Number must be at least 1.')
                    else:
                        valid = True
                except ValueError:
                    print('Number must be an integer.')
            running = False
            max_bestsellers(x)
        else:
            print('That is an invalid command!')
if __name__ == '__main__':
    main()
