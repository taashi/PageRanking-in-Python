names=[]

openfile = open("/Users/rohitchawla/Desktop/Taashi_Khurana_HW1/test/hmtl2/\linksScrapped.txt")

for line in openfile:
   names.append(line.strip())

anothernames = []
for i in names:
   ij, onlyname = i.split("wikipedia.org")
   anothernames.append(onlyname)

g1file = open('/Users/rohitchawla/Desktop/Taashi_Khurana_HW1/test/hmtl2/ce1.txt','w')
URL_DIRECTORY = '/Users/rohitchawla/Desktop/Taashi_Khurana_HW1/test/hmtl2/test1/'

for eachentry in anothernames:
   ij, only = eachentry.split("wiki/")
   g1file.write(only + " ")
   for each in names:
       ij, onlyname = each.split("wikipedia.org/wiki/")
       newpath = URL_DIRECTORY + '\\' + onlyname + '.txt'
       sourcereader = open(newpath, 'r', encoding="utf8").read()
       newname = "/wiki/" + onlyname
       if eachentry in sourcereader and onlyname != only:
           g1file.write(onlyname + " ")
   g1file.write("\n")

g1file.close()