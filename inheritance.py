class movies:
    def film1(genre):
        print("Action")
    def film2(genre):
        print("Comedy")

class new_movie(movies):
    def film3(genre):
        print("Thriller")

allfilms = new_movie()
allfilms.film1()
allfilms.film2()
allfilms.film3()
