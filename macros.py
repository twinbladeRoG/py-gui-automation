import pyautogui
import time
import pyperclip

def click(x, y):
  pyautogui.click(x, y)

def db_click(x, y):
  pyautogui.doubleClick(x, y)

def move_to(x, y):
  pyautogui.moveTo(x, y)

def move_to_relative(x, y):
  pyautogui.moveRel(x, y)

def controlKey(key):
  pyautogui.hotkey('ctrl', key)

def copy():
  pyautogui.hotkey('ctrl', 'c')

def select_all():
  pyautogui.hotkey('ctrl', 'a')

def paste():
  pyautogui.hotkey('ctrl', 'p')

def create_file(filename, extension, data):
  f = open('./output/'+filename+'.'+extension, 'w')
  if data == 'fromClipboard':
    data=pyperclip.paste().replace('\n', '')
  f.write(data)
  f.close()
  return filename+'.'+extension

def scroll(scroll_amount, x, y):
  pyautogui.scroll(scroll_amount, x, y)

def pause(sec):
  time.sleep(sec)

def type(data):
  pyautogui.typewrite(data)

def screenshot():
  pyautogui.screenshot()
