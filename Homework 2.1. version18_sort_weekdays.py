from datetime import datetime, timedelta
from collections import defaultdict

# Список користувачів
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 2, 14)},
    {"name": "Taras Shevchenko", "birthday": datetime(1814, 3, 9)},
    {"name": "Vladimir Zelensky", "birthday": datetime(1978, 1, 25)},
    {"name": "Mila Kunis", "birthday": datetime(1983, 8, 14)},
    {"name": "Vitali Klitschko", "birthday": datetime(1971, 7, 19)},
    {"name": "Sergei Bubka", "birthday": datetime(1963, 12, 4)},
    {"name": "Igor Sikorsky", "birthday": datetime(1889, 5, 25)},
    {"name": "Katheryn Winnick", "birthday": datetime(1977, 12, 17)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Albert Einstein", "birthday": datetime(1879, 3, 14)},
    {"name": "Nelson Mandela", "birthday": datetime(1918, 7, 18)},
    {"name": "Marie Curie", "birthday": datetime(1867, 11, 7)},
    {"name": "Leonardo da Vinci", "birthday": datetime(1452, 4, 15)},
    {"name": "Winston Churchill", "birthday": datetime(1874, 11, 30)},
    {"name": "J.K. Rowling", "birthday": datetime(1965, 7, 31)},
    {"name": "Adele", "birthday": datetime(1988, 5, 5)},
    {"name": "George Clooney", "birthday": datetime(1961, 5, 6)},
    {"name": "Meryl Streep", "birthday": datetime(1949, 6, 22)},
    {"name": "Tom Hanks", "birthday": datetime(1956, 7, 9)},
    {"name": "Brad Pitt", "birthday": datetime(1963, 12, 18)},
    {"name": "Angelina Jolie", "birthday": datetime(1975, 6, 4)},
    {"name": "Robert Downey Jr.", "birthday": datetime(1965, 4, 4)},
    {"name": "Natalie Portman", "birthday": datetime(1981, 6, 9)},
    {"name": "Johnny Depp", "birthday": datetime(1963, 6, 9)},
    {"name": "Cate Blanchett", "birthday": datetime(1969, 5, 14)},
    {"name": "Denzel Washington", "birthday": datetime(1954, 12, 28)},
    {"name": "Emma Watson", "birthday": datetime(1990, 4, 15)},
    {"name": "Keanu Reeves", "birthday": datetime(1964, 9, 2)},
    {"name": "Scarlett Johansson", "birthday": datetime(1984, 11, 22)},
    {"name": "Daniel Radcliffe", "birthday": datetime(1989, 7, 23)},
    {"name": "Gwen Stefani", "birthday": datetime(1969, 10, 3)},
    {"name": "Simon Cowell", "birthday": datetime(1959, 10, 7)},
    {"name": "Sacha Baron Cohen", "birthday": datetime(1971, 10, 13)},
    {"name": "Zac Efron", "birthday": datetime(1987, 10, 18)},
    {"name": "Alicia Silverstone", "birthday": datetime(1976, 10, 4)},
    {"name": "Jeremy Renner", "birthday": datetime(1971, 10, 7)},
    {"name": "Snoop Dogg", "birthday": datetime(1971, 10, 20)},
    {"name": "Zach Galifianakis", "birthday": datetime(1969, 10, 1)},
    {"name": "Thandie Newton", "birthday": datetime(1972, 10, 6)},
    {"name": "Usher", "birthday": datetime(1978, 10, 14)},
    {"name": "John Lennon", "birthday": datetime(1940, 10, 9)},
    {"name": "Eminem", "birthday": datetime(1972, 10, 17)},
    {"name": "Ryan Reynolds", "birthday": datetime(1976, 10, 23)},
    {"name": "Seth MacFarlane", "birthday": datetime(1973, 10, 26)},
    {"name": "Hilary Duff", "birthday": datetime(1987, 10, 28)},
    {"name": "Ioan Gruffudd", "birthday": datetime(1973, 10, 6)},
    {"name": "Bruno Mars", "birthday": datetime(1985, 10, 8)},
    {"name": "Matthew Morrison", "birthday": datetime(1978, 10, 30)},
    {"name": "Test Arest", "birthday": datetime(1978, 10, 15)},
]

def get_birthdays_for_week(users):
    today = datetime.today().date()
    # Finding the start of the week (i.e., Saturday)
    start_of_week = today - timedelta(days=(today.weekday() - 5) % 7)  # Shift to Saturday

    birthdays_by_day = defaultdict(list)

    for user in users:
        # Get birthday for the current year
        birthday_this_year = user["birthday"].replace(year=today.year).date()

        # Check if the birthday is on Saturday or Sunday, shift it to Monday
        if birthday_this_year == start_of_week or birthday_this_year == start_of_week + timedelta(days=1):
            birthdays_by_day["Monday"].append(user["name"])

        # Check if the birthday is from Monday to Friday of the current week
        elif start_of_week + timedelta(days=2) <= birthday_this_year <= start_of_week + timedelta(days=6):
            day_name = (birthday_this_year - start_of_week).days - 2  # Shift by 2 days to align with start being Saturday
            day_string = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][day_name]
            birthdays_by_day[day_string].append(user["name"])

    # Outputting the result
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day in days_order:
        if day in birthdays_by_day:
            print(f"{day}: {', '.join(birthdays_by_day[day])}")


# Тестування in console

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 2, 14)},
    {"name": "Taras Shevchenko", "birthday": datetime(1814, 3, 9)},
    {"name": "Vladimir Zelensky", "birthday": datetime(1978, 1, 25)},
    {"name": "Mila Kunis", "birthday": datetime(1983, 8, 14)},
    {"name": "Vitali Klitschko", "birthday": datetime(1971, 7, 19)},
    {"name": "Sergei Bubka", "birthday": datetime(1963, 12, 4)},
    {"name": "Igor Sikorsky", "birthday": datetime(1889, 5, 25)},
    {"name": "Katheryn Winnick", "birthday": datetime(1977, 12, 17)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Albert Einstein", "birthday": datetime(1879, 3, 14)},
    {"name": "Nelson Mandela", "birthday": datetime(1918, 7, 18)},
    {"name": "Marie Curie", "birthday": datetime(1867, 11, 7)},
    {"name": "Leonardo da Vinci", "birthday": datetime(1452, 4, 15)},
    {"name": "Winston Churchill", "birthday": datetime(1874, 11, 30)},
    {"name": "J.K. Rowling", "birthday": datetime(1965, 7, 31)},
    {"name": "Adele", "birthday": datetime(1988, 5, 5)},
    {"name": "George Clooney", "birthday": datetime(1961, 5, 6)},
    {"name": "Meryl Streep", "birthday": datetime(1949, 6, 22)},
    {"name": "Tom Hanks", "birthday": datetime(1956, 7, 9)},
    {"name": "Brad Pitt", "birthday": datetime(1963, 12, 18)},
    {"name": "Angelina Jolie", "birthday": datetime(1975, 6, 4)},
    {"name": "Robert Downey Jr.", "birthday": datetime(1965, 4, 4)},
    {"name": "Natalie Portman", "birthday": datetime(1981, 6, 9)},
    {"name": "Johnny Depp", "birthday": datetime(1963, 6, 9)},
    {"name": "Cate Blanchett", "birthday": datetime(1969, 5, 14)},
    {"name": "Denzel Washington", "birthday": datetime(1954, 12, 28)},
    {"name": "Emma Watson", "birthday": datetime(1990, 4, 15)},
    {"name": "Keanu Reeves", "birthday": datetime(1964, 9, 2)},
    {"name": "Scarlett Johansson", "birthday": datetime(1984, 11, 22)},
    {"name": "Daniel Radcliffe", "birthday": datetime(1989, 7, 23)},
    {"name": "Gwen Stefani", "birthday": datetime(1969, 10, 3)},
    {"name": "Simon Cowell", "birthday": datetime(1959, 10, 7)},
    {"name": "Sacha Baron Cohen", "birthday": datetime(1971, 10, 13)},
    {"name": "Zac Efron", "birthday": datetime(1987, 10, 18)},
    {"name": "Alicia Silverstone", "birthday": datetime(1976, 10, 4)},
    {"name": "Jeremy Renner", "birthday": datetime(1971, 10, 7)},
    {"name": "Snoop Dogg", "birthday": datetime(1971, 10, 20)},
    {"name": "Zach Galifianakis", "birthday": datetime(1969, 10, 1)},
    {"name": "Thandie Newton", "birthday": datetime(1972, 10, 6)},
    {"name": "Usher", "birthday": datetime(1978, 10, 14)},
    {"name": "John Lennon", "birthday": datetime(1940, 10, 9)},
    {"name": "Eminem", "birthday": datetime(1972, 10, 17)},
    {"name": "Ryan Reynolds", "birthday": datetime(1976, 10, 23)},
    {"name": "Seth MacFarlane", "birthday": datetime(1973, 10, 26)},
    {"name": "Hilary Duff", "birthday": datetime(1987, 10, 28)},
    {"name": "Ioan Gruffudd", "birthday": datetime(1973, 10, 6)},
    {"name": "Bruno Mars", "birthday": datetime(1985, 10, 8)},
    {"name": "Matthew Morrison", "birthday": datetime(1978, 10, 30)},
    {"name": "Test Arest", "birthday": datetime(1978, 10, 15)},
]

get_birthdays_for_week(users)
