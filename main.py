
def arquivo():
  file = open('exemplo.txt', 'w+')
  file.write('Oi \n')
  file.write('Hola \n')
  file.write('Hello \n')
  file.seek(0,0)
  print(file.read())
  file.seek(0,0)
  file.close()
arquivo()