text = input("Ievadiet tekstu: ")
def delete(text):
  if text.count('e')>0:
    text = text.replace('e', ' ')
    text = print(text.upper())
  else: 
    text = print('')
  return text

delete(text)