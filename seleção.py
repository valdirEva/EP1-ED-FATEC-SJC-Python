def seleção(v1):
  v = v1.copy()
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r



