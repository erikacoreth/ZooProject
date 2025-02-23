# Zoo Management System

## Overview
The Zoo Management System is a Python-based application that allows users to manage a collection of various animals in a zoo-like setting. The system supports adding different types of animals, such as bears, elephants, penguins, and cheetahs, each with specific attributes. Users can add animals, view all animals, or print specific types of animals from the collection.

## Features
- **Add Animals**: Add bears, elephants, penguins, and cheetahs to the zoo with specific attributes like fur color, weight, height, and speed.
- **View All Animals**: Display details of all animals currently in the zoo.
- **Filter by Animal Type**: View animals of a specific type (e.g., all bears or all penguins).
- **Interactive Menu**: Navigate through the application using a simple text-based menu.

## How to Run
To run the Zoo Management System, make sure Python is installed on your computer. Follow these steps:

1. **Clone the Repository**:
    ```
    git clone https://github.com/yourusername/zoo-management-system.git
    ```
2. **Navigate to the Project Directory**:
    ```
    cd zoo-management-system
    ```
3. **Run the System**:
    ```
    python zoo_manager.py
    ```

## Usage Instructions
Once the application starts, you will interact with it through a menu-driven interface:
1. **Add Animals**: Choose the type of animal to add and provide the required details.
2. **Print All Animals**: Lists all animals in the zoo with their details.
3. **Print Specific Animals**: Select a specific type of animal to view, such as all bears or all cheetahs.
4. **Exit the Program**: Terminate the application.

### Example Commands
- **Add an Elephant**:
  - Choose to add an elephant.
  - Provide the name, species, and weight of the elephant.
- **View All Animals**:
  - Select the option to print all animals and view details like name, species, and specific attributes.

## Development
This project utilizes basic principles of object-oriented programming in Python, including inheritance, polymorphism, and encapsulation. Each animal type extends a base `Animal` class, which provides shared functionality and interface for all animals.
