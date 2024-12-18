This program beings with the Animal class that is the parent class for all the animal subclasses. Attributes included in the parent class are name and species along with methods like make_sound and get_info. Make_sound returns a generic sound while get_info provides formatted details about the animal. The four subclasses are Bear, Elephant, Penguin, and Cheetah. These four subclasses use inheritance from the Animal class while also added new attributes like fur_color, weight, height, and speed and also override both make_sound (which provides animal specific sounds) and get_info (which includes animal specific additional details). The Main class starts with a zoo attribute which stores all the animals add to that zoo. The Main class menu also has an interactive menu offering options to add aniamls, display all animals, or filter animals by type. Methods that are in the Main class are add_animals, which adds aniamls to the zoo along with specific user input information, while print_all and print_specific display animal details. The add_animals and print_specific methods both have additional interactive menu’s that help in selecting a specific animal to either add or retrieve animal specific information. The print_all method prints all animals and their corresponding information. The program initializes the Main class and runs the interactive menu when executed as the main module, allowing users to manage their zoo until they exit.
