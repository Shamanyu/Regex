import re

class Regex():

  def __init__(self):
    print ("Init function of Regex")

  def match(self, string, pattern):
    p = re.compile('ab*')
    print (p)

if __name__ == '__main__':
  regex = Regex()
  regex.match('', '')