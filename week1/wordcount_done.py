import sys
def get_dictionary(filename):
    with open(filename, "r") as file:
        content = file.read()
        words =content.split()
        words_dict = dict.fromkeys(words, 0)
        for word in words: words_dict[word]+=1
        return words_dict
def print_words(filename):
    dict=get_dictionary(filename)
    sorted_keys_list= sorted(dict.keys())
    for key in sorted_keys_list: print(key +":"+str(dict[key]))
def print_top(filename):
    dict=get_dictionary(filename)
    sorted_keys_list= sorted(dict.keys())
    tuple_to_add=()
    list_to_sort=[]
    for key in sorted_keys_list:
      tuple_to_add=(key,dict[key])
      list_to_sort.append(tuple_to_add)
    sorted_by_second = sorted(list_to_sort, key=lambda tup: tup[1], reverse=True)
    top10=sorted_by_second[:10]
    for tentry in top10: print(tentry[0] + ":" + str(tentry[1]))
def main():
  #path="c://temp//text.txt" #test only
  #d=get_dictionary(path) #test only
  #print_words(d) #test only



  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()