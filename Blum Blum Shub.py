algorithm=str(input("Please enter your preferred algorithm between BBS, TRN, or File: "))

#BBS Code
if algorithm=="BBS":
    def seedbbs(initialvalue):
     global random
     random = initialvalue
    def BBS():
     P = 76667
     Q = 55547
     M = P*Q
     global random
     random = (random**2) % M
     return random
    seedbbs(int(input("Please enter initial value: ")))
    for i in range(12):
     print(int(BBS()))
    
 #TRN Code    
elif algorithm=="TRN":
    import time
    seconds = time.time()
    def seedbbs(initialvalue):
     global random
     random = initialvalue
    def BBS():
     P = 76667
     Q = 55547
     M = P*Q
     global random
     random = (random**2) % M
     return random
    seedbbs(seconds)
    for i in range(12):
     print(int(BBS()))
    
#File Code
elif algorithm=="File":
    file_name = str(input("Please specify your file name followed by the file extension: "))
    seed=0
    def file_window():
     global file_name
     file_name=seed.askopenfilename() 
    def seedbbs(initialvalue):
     global random
     random = initialvalue
    def BBS():
     P = 76667
     Q = 55547
     M = P*Q
     global random
     random = (random**2) % M
     return random
    with open(file_name,"r")as file:
     seedbbs(int(file.readline())) 
    for i in range(12):
     print(int(BBS()))
    
else:
    print("Please try again :) ")
