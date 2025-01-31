def reverse(args):
  inp = args.get("input", "")
  out = "Try to reverse! This is a reverse provider!"
  if inp != "" :
    out = inp[::-1]
  return { "output": out }