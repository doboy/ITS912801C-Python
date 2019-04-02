f = open('general_3_output.csv', 'w')

for line in open('general_3_input.csv'):
  f.write(line.upper())
