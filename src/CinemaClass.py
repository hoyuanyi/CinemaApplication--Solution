
class CinemaClass():
    def __init__(self):
        self.movies_dict = {'Morbius': {'price': 8, 'max_slots': 10, 'total_bought': 0}}
    
    def add_movie(self):
        print("Existing movies:")
        for movie in self.movies_dict:
            print(movie)
        print("----- Add Movies -----")
        self.get_movie_name()
    
    def get_movie_name(self):
        while True:
            movie_name = input("Enter Movie Name: ")
            if movie_name.strip() == "":
                print("Please input movie name")
                continue
            else:
                movie_price = self.set_movie_price()
                movie_max_slot = self.set_movie_max_slot()
                if movie_name.strip() not in self.movies_dict:
                    self.movies_dict[movie_name.strip()] = {'price': int(movie_price), 'max_slots': int(movie_max_slot), 'total_bought': 0}
                    print("----- Movie Details -----")
                    print(f"Movie Name: {movie_name.strip()}")
                    print(f"Movie Max Price: {movie_price}")
                    print(f"Movie Max Slot: {movie_max_slot}")
                    print("----- Movie Added -----")
                else:
                    print("The movie you tried to add exist..")
                    continue
                return movie_name
    
    def set_movie_price(self):
        while True:
            movie_price = input("Enter Movie Price: ")
            if movie_price.isnumeric():
                if int(movie_price) != 0:
                    return movie_price
                else:
                    print("Please set it greater than 1")
            else:
                print("Enter a valid price")
  
    def set_movie_max_slot(self):
        while True:
            movie_max_slot = input("Enter Movie Max Slot: ")
            if movie_max_slot.isnumeric():
                if int(movie_max_slot) != 0:
                    return movie_max_slot
                else:
                    print("Please set it greater than 1")
            else:
                print("Enter a valid movie max slot")

    def remove_movie(self):
        for movie in self.movies_dict:
            print(movie)
        while True:
            movie_name = input("Enter Movie Name to remove: ")
            if movie_name.strip() in self.movies_dict:
                del self.movies_dict[movie_name.strip()]
                print(f"Movie: {movie_name.strip()} has been deleted.")
                break
            else:
                print("Enter a valid movie name to remove")
    
    def buy_movie(self):
        for movie in self.movies_dict:
            print(movie)
        while True:
            movie_name = input("Enter Movie Name to buy: ")
            if movie_name.strip() in self.movies_dict:
                self.buy_movie_amount(movie_name.strip())
                return
            else:
                print("Enter a valid movie name to buy")

    def buy_movie_amount(self, movie_name):
        maxBought = self.movies_dict[movie_name]['total_bought']
        maxSlot = self.movies_dict[movie_name]['max_slots']
        remainingAmt = self.movies_dict[movie_name]['max_slots'] - self.movies_dict[movie_name]['total_bought']
        print("Remaining tickets: " + str(remainingAmt))
        if remainingAmt == 0:
            print("Movie sold out")
            return
        while True:
            amount = input("Enter amount to buy: ")
            if amount.isnumeric():
                if int(amount) <= remainingAmt:
                    maxBought += int(amount)
                    self.movies_dict[movie_name].update({'total_bought': maxBought})
                    print("Movie Ticket Purchased")
                    remainingAmt = self.movies_dict[movie_name]['max_slots'] - self.movies_dict[movie_name]['total_bought']
                    print("Remaining ticket amount: " + str(remainingAmt))
                    break
                else:
                    print("exceeded amount to buy")
            else:
                print("Enter a valid amount to buy")
 
    def show_movies(self):
        for movie in self.movies_dict:
            print(f"{movie} - ${str(self.movies_dict[movie]['price'])}")
        
    def movie_menu(self):
        while True:
            print("----- Movie Interface -----")
            print("1 - Add Movie")
            print("2 - Remove Movie")
            print("3 - Buy Movie")
            print("4 - Show all Movies")
            print("0 - Exit Interface")
            option = input("Choose option: ")
            if option.strip() == "1":
                print("You have selected Option 1: Add - Movie")
                self.get_movie_name()
            elif option.strip() == "2":
                print("You have selected Option 2: Remove - Movie")
                self.remove_movie()
            elif option.strip() == "3":
                print("You have selected Option 3: Buy - Movie")
                self.buy_movie()
            elif option.strip() == "4":
                print("You have selected Option 4: Show all Movies")
                self.show_movies()
            elif option.strip() == "0":
                print("You have selected Option 0: Exit Interface")
                break
            else:
                print("Invalid Option")