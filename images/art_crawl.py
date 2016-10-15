import urllib
import csv
import os  


def main():
    i=0
    with open('catalog.csv', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
         for row in spamreader:
             if i>0 and (not os.path.isfile('./'+str(i)+ " - "+ row[2])) and row[7]=="painting" and row[4].split(",")[0] in ["Oil on canvas","Oil on panel","Fresco","Oil on wood","Tempera on panel"]:

                try:
                    urllib.urlretrieve (row[6].replace(".html", ".jpg").replace("html", "art"), str(i)+ " - "+ row[2])
                except:
                    pass

                print str(i)+ " - "+ row[2] + row[4].split(",")[0]
             i=i+1


main()

