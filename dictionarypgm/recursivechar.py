pattern="ABAACCD"

char_count={ }
rec_char=[]
for char in pattern:
      if char in char_count:
          print(f"first recursive char is {char}")
          rec_char.append(char)
      else:
          char_count[char]=1
print(rec_char)

print(rec_char[1],"secnd rec char")