import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import datetime
import cryptocompare
import yfinance as yf

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

# Initialise Button IOError
button_left = digitalio.DigitalInOut(board.D2)
button_left.direction = digitalio.Direction.INPUT
button_left.pull = digitalio.Pull.UP

button_middle = digitalio.DigitalInOut(board.D3)
button_middle.direction = digitalio.Direction.INPUT
button_middle.pull = digitalio.Pull.UP

button_right = digitalio.DigitalInOut(board.D4)
button_right.direction = digitalio.Direction.INPUT
button_right.pull = digitalio.Pull.UP

#state of machine
state_machine = 0
state_menu = 0

def get_sp500_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      sp500_ticker = "^GSPC"  # Ticker symbol for S&P 500 index
      sp500_data = yf.Ticker(sp500_ticker)
      sp500_price = sp500_data.history(period='1d')['Close'].iloc[0]
      return sp500_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching S&P500 Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch S&P500 price.")
  return 0

def get_dow_jones_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      dow_jones_ticker = "^DJI"  # Ticker symbol for Dow Jones Industrial Average
      dow_jones_data = yf.Ticker(dow_jones_ticker)
      dow_jones_price = dow_jones_data.history(period='1d')['Close'].iloc[0]
      return dow_jones_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching DOW JONES Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch DOW JONES price.")
  return 0

def get_nasdaq_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      nasdaq_ticker = "^IXIC"  # Ticker symbol for NASDAQ Composite index
      nasdaq_data = yf.Ticker(nasdaq_ticker)
      nasdaq_price = nasdaq_data.history(period='1d')['Close'].iloc[0]
      return nasdaq_price
    except IndexError:
      print("Error: no data available for the specified period.")
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
    except Exception as e:
      print("Error fetching NASDAQ Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch NASDAQ price.")
  return 0

def get_bitcoin_price():
  max_retries = 3
  retries = 0
  while retries < max_retries:
    try:
      bitcoin_price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
      return bitcoin_price
    except Exception as e:
      print("Error fetching Bitcoin Price: ", e)
      print("Retrying in 5 seconds...")
      retries += 1
      time.sleep(5)
  print("Max retries exceeded. Unable to fetch Bitcoin price.")
  return 0

def display_time():
  lcd.clear()
  i = 1
  while i < 4:
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%I:%M:%S %p")

    lcd.cursor_position(0, 0)
    lcd.message = "Hi, the time is:"
    lcd.cursor_position(0, 1)
    lcd.message = formatted_time
    time.sleep(1)
    i += 1
  print("Current time: ", formatted_time)
def display_indices():
  sp500_price = get_sp500_price()
  print("S&P 500 price: ", sp500_price)

  dow_jones_price = get_dow_jones_price()
  print("Current Dow Jones price:", dow_jones_price)

  nasdaq_price = get_nasdaq_price()
  print("Current NASDAQ price:", nasdaq_price)

  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "S&P 500 Price:"
  lcd.cursor_position(0, 1)
  lcd.message = str(sp500_price)
  time.sleep(3)
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "DOW JONES Price:"
  lcd.cursor_position(0, 1)
  lcd.message = str(dow_jones_price)
  time.sleep(3)
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "NASDAQ Price:"
  lcd.cursor_position(0, 1)
  lcd.message = str(nasdaq_price)
  time.sleep(3)
def display_crypto():
  bitcoin_price = get_bitcoin_price()
  print("Bitcoin Price: ", bitcoin_price)

  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Bitcoin Price:"
  lcd.cursor_position(0, 1)
  lcd.message = str(bitcoin_price)
  time.sleep(3)
def clock_program():
  current_time = datetime.datetime.now()
  current_minute = current_time.minute
  current_hour = current_time.hour
  #print("Current time: ", current_time)
  formatted_time = current_time.strftime("%I:%M:%S %p")
  print("Current time: ", formatted_time, "      ")

#  lcd.clear()
  lcd.cursor_position(0, 0)# coloumn,row
  lcd.message = "Hi,"
  lcd.cursor_position(3, 0)# coloumn,row
  lcd.message = "The time is:"
  lcd.cursor_position(0, 1)
  lcd.message = formatted_time
  time.sleep(1)
def display_menu():
  print("Main Menu")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Welcome: DeskPal"
  lcd.cursor_position(0, 1)
  lcd.message = "<-Choose Mode->"
  time.sleep(0.2)
def display_option_stonks():
  print("Display Stonks Option")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Stonks Ticker!"
  lcd.cursor_position(0, 1)
  lcd.message = "-Hold Enter-"
  time.sleep(0.2)
def display_option_clock():
  print("display clock option")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Motivation Clock"
  lcd.cursor_position(0, 1)
  lcd.message = "-Hold Enter-"
  time.sleep(0.2)
def display_loading():
  print("display loading screen")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Loading....."
  lcd.cursor_position(0, 1)
  lcd.message = "Please Wait"
  time.sleep(2)
def setup():
  print("setup mode")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Connecting to"
  lcd.cursor_position(0, 1)
  lcd.message = "the internet"
  time.sleep(1)
def loop():
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

    if (state_menu == 2):
      state_menu = -1
    if (state_menu == -2):
      state_menu = 1

    if(state_menu == 0) and (state_machine == 0) and (run_once == 0):
      display_menu()
      run_once = 1
    if (state_menu == -1) and (state_machine == 0) and (run_once == 0):
      display_option_stonks()
      run_once = 1
    if (state_menu == 1) and (state_machine == 0) and (run_once == 0):
      display_option_clock()
      run_once = 1
    if (state_machine == -1):
      #display_time()
      display_indices()
      display_crypto()
    if (state_machine == 1):
      clock_program()
setup()
loop()
