movies = []


def movies_app():
    instructions = "\nWelcome to your movie's app.\n" \
                   "\n enter 'a' to add a movies\n enter 'l' to list all movies" \
                   "\n enter 'f to find a movie\n enter 'q' quit app"
    print(instructions)
    user_selection = input('\nPlease enter your choice: ').lower()

    while user_selection != 'q':
        if user_selection == 'a':
            add_movie()
        elif user_selection == 'l':
            list_movies()
        elif user_selection == 'f':
            find_movie()
        else:
            print('invalid selection,try again...')
        print(instructions)
        user_selection = input('\nPlease enter your choice: ').lower()


def add_movie():
    name = input('Enter name of movie: ').lower()
    year_of_release = int(input('Enter movie release year: '))
    genre = input('Enter genre of movie: ').lower()

    movie = {
        'name': name,
        'year_of_release': year_of_release,
        'genre': genre
    }
    movies.append(movie)


def list_movies():
    print("List of all movies")
    for movie in movies:
        show_movie_detail(movie)


def show_movie_detail(movie):
    print(f"Name: {movie['name'].lower()}")
    print(f"Year:{movie['year_of_release']}")
    print(f"Genre:{movie['genre'].lower()}")


def find_movie():
    category = input("Find a movie by either:\nMovie Name\nGenre: ").lower()
    exact_match = input(f"What category in {category}").lower()
    found_movie = []
    for movie in movies:
        if movie[category] == exact_match:
            found_movie.append(movie)
    print('here is the list....')
    for movie in found_movie:
        show_movie_detail(movie)


movies_app()





