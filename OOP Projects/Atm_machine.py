class Atm:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    # print(f"Pin is {self.pin} and balance is {self.balance}")
    self.menu()
    
  def menu(self):
    user_input = input("""
          Hi 
          How can i help you?
          1.press 1 to create pin
          2.press 2 to change pin
          3.press 3 to check balance
          4.press 4 to withdraw balance
          5.press 5 to exit
          """
          )
    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      #check balance
      pass
    elif user_input == '4':
      #withdraw balance
      pass
    else:
      exit()    
    
  def create_pin(self):
    user_pin = input("Enter your pin:")
    self.pin = user_pin
    
    user_balance = int(input("Enter your balance:"))
    self.balance = user_balance
    print("Pin changed successfully")
    self.menu()
    
  def change_pin(self):
    old_pin =input("Enter old pin:")
    if old_pin == self.pin:
      new_pin = input("Enter new pin:")
      self.pin = new_pin
      print("New pin intered successfully")
      self.menu()
    else:
      print("Existing pin didn't match")
      self.menu()    
  
obj = Atm()
