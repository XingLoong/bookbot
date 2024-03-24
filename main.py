def main():
  book_path = 'books/Franky.txt' #copy book text into file, and link here
  text = book_text(book_path)
  words = num_words(text)
  print("--- Begin the book report ---")
  print(f"{words} words in the document")
  print("")
  rearrange(letter_count(text))
  print("--- End Report ---")

def book_text(path):
  with open(path) as f:
    return f.read()

def num_words(text):
  words = text.split()
  return len(words)

def letter_count(text):
  lowered_string = text.lower()
  dict_count = {}
  
  for t in lowered_string:
    if t.isalpha():
      if t not in dict_count:
        dict_count[t] = 1
      else:
        dict_count[t] += 1
    else:
      continue
  return dict_count

def rearrange(dict_count):
  arranged = sorted(dict_count.items(), key = lambda x:x[1], reverse = True)
  for x in arranged:
    print(f"The '{x[0]}' character was found {x[1]} times")


main()