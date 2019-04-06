import json

data = {}

command_list = []

while True:
  macro = input('\nEnter macro: ')
  command = {}

  if macro == 'moveTo':
    command['command'] = 'moveTo'
    command['x'] = int(input('Enter X coordinate: '))
    command['y'] = int(input('Enter Y coordinate: '))

  elif macro == 'click':
    command['command'] = 'click'
    command['x'] = int(input('Enter X coordinate: '))
    command['y'] = int(input('Enter Y coordinate: '))

  elif macro == 'dclick':
    command['command'] = 'dclick'
    command['x'] = int(input('Enter X coordinate: '))
    command['y'] = int(input('Enter Y coordinate: '))

  elif macro == 'selectAll':
    command['command'] = 'selectAll'

  elif macro == 'copy':
    command['command'] = 'copy'

  elif macro == 'createFile':
    command['command'] = 'createFile'
    command['filename'] = input('Enter filename: ')
    command['extension'] = input('Enter file extension: ')
    command['data'] = input('Enter data: ')

  elif macro == 'pause':
    command['command'] = 'pause'
    command['time'] = int(input('Enter pause time: '))

  elif macro == 'type':
    command['command'] = 'type'
    command['data'] = input('Enter data: ')

  elif macro == 'exit':
    break

  else:
    print('Invalid macro.')

  command_list.append(command)


# command = {}
# command['command'] = 'moveTo'
# command['x'] = 586
# command['y'] = 156

# command_list.append(command)

# command = {}
# command['command'] = 'click'
# command['x'] = 586
# command['y'] = 156

# command_list.append(command)

data['commands'] = command_list
data['iteration'] = 3

f = open('./config/macros.json', 'w')
f.write(json.dumps(data))
f.close()

