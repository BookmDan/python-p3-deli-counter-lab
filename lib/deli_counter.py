katz_deli = []

def line(katz_deli):
  if not katz_deli:
    return "The line is currently empty."
  
  line_status = "The line is currently:"
  for index, person in enumerate(katz_deli, start=1):
    line_status +=f" {index}, {person}"

  return line_status

def take_a_number(katz_deli, name):
  katz_deli.append(name)
  position = len(katz_deli)
  print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
  if not katz_deli:
    print("There is nobody waiting to be served!")
    return
  
  serving_person = katz_deli.pop(0)
  print("Currently serving {serving_person}.")