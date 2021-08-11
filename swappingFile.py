def swapFiles():
    fileName_1=input("Enter the first file name:- ")
    fileName_2=input("Enter the second file name:- ")

    fileA_R=open(fileName_1,'r')
    fileB_R=open(fileName_2,'r')
    
    fileA_data=fileA_R.read()
    fileB_data=fileB_R.read()

    fileA_W=open(fileName_1,'w')
    fileB_W=open(fileName_2,'w')

    fileA_W.write(fileB_data)
    fileB_W.write(fileA_data)

swapFiles()