import sys
def get_dictionary(filename):
    file = open(filename, "r")
    content = file.read()
    words = (list(content.split()))
    d = dict.fromkeys(words, 0)
    for word in words:
        if word in d: d[word] +=1
    file.close()
    return d
def print_words(filename):
    d=get_dictionary(filename)
    r = sorted(d.keys())
    for lentry in r: print(lentry +":"+str(d[lentry]))
def print_top(filename):
    d=get_dictionary(filename)
    r = sorted(d.keys())
    t=()
    l=[]
    for lentry in r:
      t=(lentry,d[lentry])
      l.append(t)
    sorted_by_second = sorted(l, key=lambda tup: tup[1], reverse=True)
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