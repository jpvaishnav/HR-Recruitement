import os
import pickle
import sys
import selection_committee

l2=[]
G = []

class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

def test_selection_committee():
    #read data from standered.dat file which consists standerd database file
    #and compare with selection committe class attributes
    names=[]
    emails=[]
    f1 = open("database/standerd.dat", "rb")
    try:
        while True:
            s = pickle.load(f1)
            k = s.address
            o = s.name.upper()
            names.append(o)
            emails.append(k)
            continue

    except EOFError:
        pass
    f1.close()
    assert len(names)==len(l2) and len(emails)==len(G), "\nUNEQUAL DATA INSERTED\n"
    print("**************\t\t\t\t\t//UNIT TESTING//\t\t\t\t\t**************\n")
    for i in range(0,len(names)):
        x1=names[i]
        x2=l2[i]
        y1=emails[i]
        y2=G[i]
        assert x1==x2 and y1==y2, "\nMEMBER DATA INVALID\n"
        print("\t\t\t\t\tMEMBER "+str(i+1)+" DATA VERIFIED")
    print("**************\t\t\t//CONGRATULATIONS, UNIT TESTING COMPLETED, 12 TESTCASES EXECUTED //\t\t\t**************\n")
if __name__ == '__main__':
    print("\n\n\nUNIT TESTING OF SELECTION COMMITTEE DATA\n\n\n")
    f2 = open("database/selection.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            k = s.address
            o = s.name.upper()
            l2.append(o)

            G.append(k)
            continue

    except EOFError:
        pass
    f2.close()
    temp=test_selection_committee()