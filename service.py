import macros
import json

command_list = json.load(open('./config/macros.json'))

commands = command_list['commands']
iteration = command_list['iteration']

for i in range(1, iteration+1):
  for command in commands:
    c = command['command']
    if c == 'moveTo':
      x = command['x']
      y = command['y']
      macros.move_to(x, y)

    if c == 'click':
      x = command['x']
      y = command['y']
      macros.click(x, y)

    if c == 'dclick':
      x = command['x']
      y = command['y']
      macros.db_click(x, y)

    if c == 'selectAll':
      macros.select_all()

    if c == 'copy':
      macros.copy()

    if c == 'createFile':
      filename = command['filename'] + '_' + str(i)
      extension = command['extension']
      data = command['data']
      macros.create_file(filename, extension, data)

    if c == 'pause':
      seconds = command['time']
      macros.pause(seconds)

    if c == 'type':
      data = command['data']
      macros.type(data)