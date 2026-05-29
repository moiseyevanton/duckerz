with open("loginator.txt", "r", encoding="utf-8") as file:
      for line in file:
          if "/flag.php/" in line:
              part = line.split("/flag.php/")[1]
              symbol = part[0]
              print(symbol, end="")

print()