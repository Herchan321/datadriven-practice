def caesar_shift_check(a: str, b: str):
  
    
  if len(a)!=len(b):
    return False 
  shifts = set()
  for char_a, char_b in zip(a.lower(), b.lower()):
    if char_a.isalpha() and char_b.isalpha():
      shifts.add((ord(char_b) - ord(char_a)) % 26)
    elif char_a != char_b:
      return False

  return len(shifts) <= 1
  
  
