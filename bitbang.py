text = 'bitband.org'
duplicates = []
for char in text:
   if text.count(char) > 1:
     if char not in duplicates:
         duplicates.append(char)
         
print(duplicates)