import PyPDF2 as pdf
import io
import re

file=open('dbmsyes.pdf','rb')

pdf_reader= pdf.PdfFileReader(file)

#print(pdf_reader.getNumPages() 
x=(pdf_reader.getNumPages())

ans=[]
ques=[]
t=False
for page in range(x):

    page1=pdf_reader.getPage(page)
    
    pages_text =page1.extractText()

    #ans=[]

    for line in io.StringIO(pages_text):

        print(line)

        #for i in line:



           #if i.isalpha() and i.endswith(".")
    
               # ans.append(line)
                
           # else:
               # ques.append(line)
#print(ques)'''
#if line.startswith('Ans:') == True :
            #print(line.pages_text )

        #for i in line:

            #if i.isdigit() == True:

            #ans = re.compile('Ans:')

            #if(ans.search(line))== True:
            #ans.append(line)
                #print(line)#
        
            #elif(i.isalpha() == True: 

