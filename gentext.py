f = open("gentext.txt", "w")
for x in range(1, 100):
  f.write(f"<p>{x}</p>\n")