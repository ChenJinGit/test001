class Anilam(object):
  def __init__(self, name, age, num):
      self.name = name
      self.age = age
      self.num = num
  def drink(self):
      print('----喝------')
  def say(self):
      print('-----看-----')
      print('----张三增加的-----')
      print('----陈金增加的-----')
      print()
def main():
  dog = Anilam('黄狗', '11', 100)
  dog.drink()
  dog.say()

if __main__ == '__name__':
    main() 
