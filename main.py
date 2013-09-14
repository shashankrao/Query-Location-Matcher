### IMPORTING ENCHANT LIBRARY FOR WORD CHECKING
# SOURCE: http://pythonhosted.org/pyenchant/
import enchant

# import modules
import sys

#import local modules
from soundex import *
from editdistance import *
from doublemetaphone import *

#global declaration of dictionaries
sdx = {}
sdx4 = {}
sdx3 ={}

#global list of all places
places = []

def getlocations(locpath):
	global sdx 
	global sdx4 	
	global sdx3 
	global places

	fo=open(locpath,"r")
	for line in fo:
    	places.append(line.replace('\n','').upper())
    	sdx[dm(line.replace('\n','').upper())[0]] = line.replace('\n','').upper()
    	sdx3[soundex2((line.replace('\n','').upper()),3)] = line.replace('\n','').upper()
    	sdx4[soundex2((line.replace('\n','').upper()),4)] = line.replace('\n','').upper()            
	fo.close()

def matchlocations(inputfile,outputfile):
	from enchant.checker import SpellChecker
	chkr = SpellChecker("en_US")
	global sdx 
	global sdx4 	
	global sdx3 
	global places

	i=0
	fo = open(inputfile,"r")
	printer = open(outputfile,"w")
	for line in fo:
    	print i
    	i = i+1
    	chkr.set_text(line)
    	for err in chkr:
        	#print "error",err.word
        	toprint = err.word
        	word = err.word.upper()
        	mind = 4
        	replace = []
        	flag = False
        	soundFlag = False
        	noFlag = False
        	if word in places:
            	line = line.replace(toprint,"<loc>"+word.lower()+"</loc>")
        	else:
            	for place in places:
                	dist = minEditDist(word,place)
                	#print place,dist
                	if dist<mind:
                    	replace=[]
                    	replace.append(place)
                    	mind = dist
                    	flag = True
                	elif dist == mind:
                    	replace.append(place)
                    	flag == True
            	if flag == True and len(word) > mind:
                	if mind ==1 and len(replace)==1:
                    	line = line.replace(toprint,"<loc>"+replace[0].lower()+"</loc>")    
                	else:
                    	if(soundex2(word,4) in sdx4 and len(word)>3):
                        	line = line.replace(toprint,"<loc>"+sdx4[soundex2(word,4)].lower()+"</loc>")
                    	elif(soundex2(word,3) in sdx3 and len(word)>3):
                        	line = line.replace(toprint,"<loc>"+sdx3[soundex2(word,3)].lower()+"</loc>")
                    	elif(dm(word)[0] in sdx and len(word)>3):
                        	line = line.replace(toprint,"<loc>"+sdx[dm(word)[0]].lower()+"</loc>")  
                    	else:
                        	if len(replace) == 1:
                            	line = line.replace(toprint,"<loc>"+replace[0].lower()+"</loc>")
                        	else:
                            	#print replace
                            	for ele in replace:
                                	if(dm(ele)[0] == dm(toprint)[0]):
                                    	line = line.replace(toprint,"<loc>"+ele.lower()+"</loc>")
                                    	soundFlag = True
                                    	break
                            	if soundFlag == False:
                                	line = line.replace(toprint,"<loc>"+replace[0].lower()+"</loc>")
            	elif(dm(word)[0] in sdx and len(word)>3):
                	        line = line.replace(toprint,"<loc>"+sdx[dm(word)[0]].lower()+"</loc>")
    	printer.write(line)

	printer.close()
	fo.close()


if __name__ == "__main__":
	if(len(sys.argv) <4):
		print "python main.py locationfile.txt source.txt dest.txt"
		sys.exit()
	getlocations(sys.argv[1])
	matchlocations(sys.argv[2],sys.argv[3])