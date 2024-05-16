import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
import board
import time
import datetime
import requests
from Stocks import *

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
def clock_program(last_minute, last_hour):
  lcd.cursor_position(0, 0)# coloumn,row
  lcd.message = "Hi,"
  lcd.cursor_position(3, 0)# coloumn,row
  lcd.message = "The time is:"
  current_time = datetime.datetime.now()
  current_minute = current_time.minute
  current_hour = current_time.hour
  #print("Current time: ", current_time)
  formatted_time = current_time.strftime("%I:%M:%S %p")
  print("Current time: ", formatted_time, "      ")
  lcd.cursor_position(0, 1)
  lcd.message = formatted_time
  time.sleep(1)
  if (current_hour != last_hour):
    last_hour = current_hour
    last_minute = current_minute
    lcd.clear()
    lcd.cursor_position(0, 0)
    lcd.message = "NEW HOUR! GET YO"
    lcd.cursor_position(0, 1)
    lcd.message = "ASS TO WORK!!!!"
    time.sleep(5)
    lcd.clear()
    lcd.cursor_position(0, 0)# coloumn,row
    lcd.message = "Hi,"
    lcd.cursor_position(3, 0)# coloumn,row
    lcd.message = "The time is:"
  if (current_minute != last_minute):
    last_minute = current_minute
    lcd.clear()
    lcd.cursor_position(0, 0)
    lcd.message = "Wow! It is now a:"
    lcd.cursor_position(0, 1)
    lcd.message = "BRAND NEW MINUTE"
    time.sleep(5)
    lcd.clear()
    lcd.cursor_position(0, 0)# coloumn,row
    lcd.message = "Hi,"
    lcd.cursor_position(3, 0)# coloumn,row
    lcd.message = "The time is:"
  return last_minute, last_hour
import requests
def display_weather(city_name, api_key):
    # Construct the URL with the city name
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

  # Send HTTP request to the API
  response = requests.get(url)

  # Check if request was successful
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract relevant weather information
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Print the weather information
    print(f"Weather in {city_name}: {weather_description.capitalize()}")
    print(f"Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} mph")

    lcd.cursor_position(0, 0)
    lcd.message = "Spokane Weather:"
    lcd.cursor_position(0, 1)
    lcd.message = f"{temperature} F {humidity}% RH     "
    time.sleep(5)
    lcd.cursor_position(0, 0)
    lcd.message = f"{weather_description}              "
    lcd.cursor_position(0, 1)
    lcd.message = f"Wind: {wind_speed} mph"
    time.sleep(2)
  else:
    print("Failed to fetch weather data.")
    lcd.clear()
    lcd.cursor_position(0, 0)
    lcd.message = "Failed to fetch"
    lcd.cursor_position(0, 1)
    lcd.message = "weather data."
