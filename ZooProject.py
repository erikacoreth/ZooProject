class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print('generic animal sound')

    def get_info(self):
        return f"{self.name} is a {self.species}."

class Bear(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
    def make_sound(self):
        print('roar')
    def get_info(self):
        return f"{self.name} is a {self.species} with {self.fur_color} fur color."

class Elephant(Animal):
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = float(weight)
    def make_sound(self):
        print('trumpet')
    def get_info(self):
        return f"{self.name} is a {self.species} with {self.weight} kg weight."

class Penguin(Animal):
    def __init__(self, name, species, height):
        super().__init__(name, species)
        self.height = float(height)
    def make_sound(self):
        print('squawk')
    def get_info(self):
        return f"{self.name} is a {self.species} with {self.height} ft height."

class Cheetah(Animal):
    def __init__(self, name, species, speed):
        super().__init__(name, species)
        self.speed = float(speed)
    def make_sound(self):
        print('purr')
    def get_info(self):
        return f"{self.name} is a {self.species} with {self.speed} mph speed."

class Main:
    def __init__(self):
        self.zoo = [] #list to store all animals in the zoo
    def start(self):
        while True:
            print('==Zoo Menu==')
            print('1) add animals')
            print('2) print all')
            print('3) sprint specific animals')
            print('4) exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                self.add_animal()
            elif choice == '2':
                self.print_all()
            elif choice == '3':
                self.print_specific()
            elif choice == '4':
                print('Exiting the program. Bye!')
                break
            else:
                print('Invalid choice. Please try again.')


    def add_animal(self):
        print('==Add Menu==')
        print('1) add bear')
        print('2) add elephant')
        print('3) add penguin')
        print('4) add cheetah')
        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Input Name: ')
            species = input('Input Species: ')
            fur_color = input('Input Fur Color: ')
            bear = Bear(name, species, fur_color)
            self.zoo.append(bear)
            print(f"Bear {name} added to zoo.")

        elif choice == '2':
            name = input('Input Name: ')
            species = input('Input Species: ')
            weight = input('Input Weight (kg): ')
            elephant = Elephant(name, species, weight)
            self.zoo.append(elephant)
            print(f"Elephant {name} added to zoo.")

        elif choice == '3':
            name = input('Input Name: ')
            species = input('Input Species: ')
            height = input('Input Height (ft): ')
            penguin = Penguin(name, species, height)
            self.zoo.append(penguin)
            print(f"Penguin {name} added to zoo.")

        elif choice == '4':
            name = input('Input Name: ')
            species = input('Input Species: ')
            speed = input('Input Speed (mph): ')
            cheetah = Cheetah(name, species, speed)
            self.zoo.append(cheetah)
            print(f"Cheetah {name} added to zoo.")
        else:
            print('Invalid choice. Please try again.')

    def print_all(self):
        if not self.zoo:
            print("The zoo is empty.")
        else:
            print("\n==All Animals in the Zoo==")
            for animal in self.zoo:
                print(animal.get_info())

    def print_specific(self):
        class_map = {
            '1': Bear,
            '2': Elephant,
            '3': Penguin,
            '4': Cheetah
        }
        print("\n=== Print Menu ===")
        print("1) Print Bears")
        print("2) Print Elephants")
        print("3) Print Penguins")
        print("4) Print Cheetahs")
        choice = input("Enter your choice: ")

        animal_class = class_map.get(choice)
        if animal_class:
            selected_animals = [animal for animal in self.zoo if isinstance(animal, animal_class)]
            if not selected_animals:
                print(f"No {animal_class.__name__}s in the zoo.")
            else:
                print("\n=== Printing Specific Animals ===")
                for animal in selected_animals:
                    print(animal.get_info())
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu = Main()
    main_menu.start()















