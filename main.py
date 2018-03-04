import re

class Regex():

  def __init__(self):
    print ("Init function of Regex")

  def match(self, string, pattern):

    p = re.compile('ab*')
    print (p.match("dabc"))
    print (p.search("dabc"))
    print (p.match("abc").group())
    print (p.match("abc").start())

    p = re.compile(r'\d+')
    m = p.match(' string goes here')
    if m:
      print('Match found: ', m.group())
    else:
      print('No match')

    p = re.compile(r'\d+')
    m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    if m:
      print('Match found: ', m)
    else:
      print('No match')

if __name__ == '__main__':
  regex = Regex()
  regex.match('', '')