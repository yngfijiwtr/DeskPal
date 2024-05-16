import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
import board
import time
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
def display_option_weather():
  print("display clock option")
  lcd.clear()
  lcd.cursor_position(0, 0)
  lcd.message = "Spokane Weather"
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