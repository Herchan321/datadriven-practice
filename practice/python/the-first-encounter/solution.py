def string_to_number_mapping(s: str) -> dict:
  if not s:
    return {}
  
  recorded={}
  for i, char in enumerate(s):
    if char not in recorded:
      recorded[char] = i
  return recorded
