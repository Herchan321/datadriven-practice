def sum_list(counts: list) -> int:
  if not counts:
    return 0
  s=0
  for i in range (len(counts)):
    s+=counts[i]
   

  return s
