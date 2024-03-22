class Njofredev():
  def __init__(self, name, surname, email, phone):
    self.name = name
    self.surname = surname
    self.email = email
    self.phone = phone

  def get_data(self):
    return f'My name is: {self.name}, my surname: {self.surname}, my email: {self.email} and my phone is: {self.phone}'
# 🙋‍♂️
njofre = Njofredev("Nicolás", "Jofré Andrade", "n.jofreandrade@gmail.com", "+569 5755 89 66")
print(njofre.get_data())  

# My name is: Nicolás, my surname: Jofré Andrade, my email: n.jofreandrade@gmail.com and my phone is: +569 5755 89 66