# Final Python Project: Multi-Functional GUI Application

Video Demo: https://youtu.be/LKpD1FpCPuQ

## Description:

This project is a multi-functional Python application that combines some mini-games, utilities, and interactive features into a single platform. The application is implemented with a graphical user interface (GUI) built using the `tkinter` library and uses additional libraries like `Pillow`, `multiprocessing`, and `turtle` to enhance its functionality. It also uses external resources like Open Trivia Database using APIs.

## Features:

### Main Window:

Main window is made by using `tkinter` library. In order to enhance the performance, `multiprocessing` library is used. In order to add visual appeal, images are used and thus `Pillow` library is mandatory to manage images and their sizes et cetera. It is composed of three buttons namely `Quiz Game`, `World Clock` and `Old Games`.

### Mini-Games:

The `Old Games` contain the following games. They are all made by using the `turtle` library.

- **Pong Game**: A two-player classic Pong game with customizable score limits and interactive gameplay.
- **Snake Game**: The well-known snake game where the player controls a snake to eat multi-colored food and as a result grow in size and speed.
- **Turtle Race**: A betting game where the user bets which turtle wins in a randomized race.
- **Turtle Road Crossing**: An arcade-like game which has 6 stages and the player has to navigate a turtle across a road while avoiding oncoming cars.

### Quiz Application:

The Quiz application performs the following tasks:

- Fetches trivia questions from an API (Open Trivia Database).
- A user-friendly interface to answer True/False questions.
- A feedback mechanism using glowing buttons to denote the correct answer.
- A mechanism to update scores live.

### World Clock:

The World Clock is made using several libraries and is in turn the most complex of all the tasks. It uses following libraries:

- `tkinter`
- `geopy`
- `datetime`
- `pytz`
- `threading`
- `timezonefinder`

#### It works as follows:

1. It uses a `ttk` entry to take the name of a city that the user inputs.
2. `datetime` is used to fetch the current time and convert it to UTC time.
3. The `geopy` library calculates latitudes and longitudes.
4. `timezonefinder` finds the time-zone from latitudes and longitudes.
5. Using `datetime` and `pytz`, the current time is displayed with respect to UTC in a 24-hour clock format.
6. `tkinter` displays the time, time-zone, and city name on a canvas and stores it in a list of dictionaries.

## Code Architecture:

- **`project.py`**: The main entry point, containing the application logic and navigation.
- **Modular files for specific features**:
  - `quiz.py`
  - `world_clock.py`
  - `pong.py`
  - `snake.py`
  - `turtle_race.py`
  - `turtle_road_crossing.py`
- **Testing**: 
  - Separate test file `test_project.py` ensuring correctness of core functionalities.
- **Dependencies**: Includes files like `tokens.env` and a directory `images/` containing the necessary images.

## File Structure:

project.py: Contains the main logic of the application, including the main window that provides navigation to different functionalities. It defines the following three functions for testing:

- start_playing_quiz()
- start_using_world_clock()
- start_playing_old_games()

quiz.py: Handles the quiz game, with fetching questions from an online API, interactive UI with True/False buttons, and scorekeeping.

world_clock.py: Implements the world clock feature where users can add cities, and the application displays real-time clocks with time zone information along with city names.

pong.py, snake.py, turtle_race.py, turtle_road_crossing.py: Define the respective mini-games using the turtle library.

test_project.py: Includes tests using `pytest` for the three core navigation functions to ensure their outputs meet expected results.

requirements.txt: Lists all the dependencies required for the project, including GUI and auxiliary libraries like `tkinter`, `requests`, `pytz`, `geopy`, and `turtle`.


## Libraries and Dependencies:

- GUI Framework: `tkinter`
- Concurrency: `multiprocessing`, `threading`
- Networking: `requests`
- Geolocation: `geopy`, `timezonefinder`
- Date and Time: `datetime`, `pytz`
- Game Development: `turtle`
- Additional: `dotenv`, `Pillow`

## Design Choices:

- Modular design ensures each feature resides in its own module, simplifying maintenance and extensibility.
- Threading for non-blocking tasks (e.g., fetching API data in the world clock).
- Robust exception handling for smoother user experience.
- Dynamic image resizing for consistent GUI appearance across devices.
- Employing `pytest` for automatic testing of core navigation functions.

## How to Run:

1. Clone the repository to your local machine.
2. Ensure Python 3.10+ is installed.
3. Install dependencies from `requirements.txt` using:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python project.py
   ```
5. To execute tests:
   ```bash
   pytest test_project.py
   ```   
