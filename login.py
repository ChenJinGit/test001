class Anilam(object):
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def drink(self):
      print('----喝------')
  def say(self):
      print('-----看-----')
def main():
  dog = Anilam('黄狗', '11')
  dog.drink()
  dog.say()

if __main__ == '__name__':
    main()
    
