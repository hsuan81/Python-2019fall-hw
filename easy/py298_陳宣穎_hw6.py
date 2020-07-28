file = open('stores_old.csv', 'r', encoding='big5')
file1 = open('stores_new.csv', 'w', encoding='big5')
      
for line in file.readlines():
    i = line.split(',')
    j = [i.pop(0),i.pop(2),i.pop(3),i.pop(3)]
    k =','.join(j)+'\n'
    file1.write(k)
file.close()
file1.close()
