


class Practice():
  def __init__(self, name, age, location):
    self.name = name 
    self.age = age 
    self.location = location

  def __str__(self):
    return f"{self.name}, {self.age}, from {self.location}"

  def PrintData(self):
    print()
    return f"The age of {self.name} is {self.age} and they are from {self.location}"
    

dicts = {
'p1' : Practice("Brad", 21, "England"),
'p2' : Practice("Stefan", 75, "Georgia"),
'p3' : Practice("Julian", 20, "Romania"),
'p4' : Practice("diogenes", 61, "Germany"),
'p5' : Practice("Asmodeus", 81, "Latvia"),
'p6' : Practice("Santa", 29, "France")
}


for Keys, vals in dicts.items():
  print(f"{Keys} === {vals.PrintData()}")

# p1.PrintData()



