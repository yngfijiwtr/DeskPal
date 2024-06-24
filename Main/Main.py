import time
import digitalio
from Menu import *
from Apps import *

# Initialise Button IO
button_left = digitalio.DigitalInOut(board.D2)
button_left.direction = digitalio.Direction.INPUT
button_left.pull = digitalio.Pull.UP

button_middle = digitalio.DigitalInOut(board.D3)
button_middle.direction = digitalio.Direction.INPUT
button_middle.pull = digitalio.Pull.UP

button_right = digitalio.DigitalInOut(board.D4)
button_right.direction = digitalio.Direction.INPUT
button_right.pull = digitalio.Pull.UP

# Clock variables
last_minute = None
last_hour = None

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
# You can sign up for a free API key on the OpenWeatherMap website.
api_key = 'YOUR_API_KEY'

def loop(last_minute, last_hour, api_key):
  state_menu = 0
  state_machine = 0
  run_once = 0
  while True:
    if (button_left.value == False):
      state_menu -= 1
      run_once = 0
      print("button left pressed")
      time.sleep(0.5)
    if (button_right.value == False):
      state_menu += 1
      run_once = 0
      print("button right pressed")
      time.sleep(0.5)
    if (button_middle.value == False) and (state_machine == 0):
      state_machine = state_menu
      run_once = 0
      print("button middle pressed: select")
      display_loading()
    if (button_middle.value == False) and (state_machine != 0):
      state_menu = 0
      state_machine = 0
      run_once = 0
      print("button middle pressed: main menu")
      display_loading()

    if (state_menu == 4):
      state_menu = 0
    if (state_menu == -1):
      state_menu = 3

    if(state_menu == 0) and (state_machine == 0) and (run_once == 0):
      display_menu()
      run_once = 1
    if (state_menu == 1) and (state_machine == 0) and (run_once == 0):
      display_option_stonks()
      run_once = 1
    if (state_menu == 2) and (state_machine == 0) and (run_once == 0):
      display_option_clock()
      run_once = 1
    if (state_menu == 3) and (state_machine == 0) and (run_once == 0):
      display_option_weather()
      run_once = 1
    if (state_machine == 1):
      # Stonks App
      display_indices()
      display_crypto()
    if (state_machine == 2):
      # Clock App
      (last_minute, last_hour) = clock_program(last_minute, last_hour)
    if (state_machine == 3):
      # Weather app
      # Enter the city name that you would like to see
      display_weather("Spokane", api_key)
loop(last_minute, last_hour, api_key)
