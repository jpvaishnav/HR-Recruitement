import os
import pickle
import sys
from subprocess import call
import applicant

#import pytest

def test_applicant_name(x):
    a=x.isdigit()
    if len(x)!=0 and a!= True:
        return True
    else:
        return False

def test_applicant_mobile(x):
    if x.isdigit() and len(x)!=0 and len(x)==10:
        return True
    else:
        return False

def test_applicant_email(x):
    if len(x)==0:
        return False
    a=x.isdigit()
    if a==True:
        return False
    if x[0].isdigit():
        return False
    if '@' in x==False:
        return False
    return True

def test_applicant_marks(x):
    if str(x).isdigit() and len(str(x))!=0 and x>0 and x<=100:
        return True
    else:
        return False

print("**************\t\t\t\t\t//UNIT TESTING//\t\t\t\t\t**************\n")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 1 : \n")
#user enters all valid entries
apl1=applicant.save("JAY PRAKASH",
                         "prakash.3@iitj.ac.in",
                         "7898458963",
                         87)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 1 EXECUTED SUCCESSFULLY")

print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 2 : \n")
#USER ENTERS VALID EMAIL ID WITH DIFFERENT DOMAIN
apl1=applicant.save("JAY PRAKASH",
                         "prakash.3@gmail.com",
                         "7898458963",
                         87)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 2 EXECUTED SUCCESSFULLY")

#testcase 3 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 3 : \n")
#DIFFERENT ENTRY
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "7898458783",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 3 EXECUTED SUCCESSFULLY")

#testcase 4 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 4 : \n")
#user forgets entering the name
apl1=applicant.save("",
                         "adarshkumar@gmail.com",
                         "7898458783",
                         61)
if test_applicant_name(apl1.name):
    print("\t\t\t\t\tVALID NAME ENTERED")
else:
    print("\t\t\t\t\tNAME NOT ENTERED, PLEASE PROVIDE THE APPLICANT'S NAME!")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 4 EXECUTED SUCCESSFULLY")

#testcase 5
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 5 : \n")
#USER TYPES wrong email id type
apl1=applicant.save("ADARSH",
                         "adarshkumargmail.com",
                         "7898458783",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
if test_applicant_email(apl1.address):
    print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
else:
    print("\t\t\t\t\tTHE PROVIDE EMAIL-ID IS MISSING '@' SYMBOL, PLEASE RE-ENTER AGAIN!")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 5 EXECUTED SUCCESSFULLY")

#testcase 3 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 6 : \n")
#user enters Mobile number with missing one digit accidentally
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "789845878",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
if test_applicant_mobile(apl1.mobile_no):
    print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
else:
    print("\t\t\t\t\tPROVIDED MOBILE NUMBER IS MISSING ONE DIGIT, PLEASE ENTER ONE MORE DIGIT!")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 6 EXECUTED SUCCESSFULLY")

#testcase 7
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 7 : \n")
#USER forgets evaluation
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "7898458783",
                         -2)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
if test_applicant_marks(apl1.price):
    print("\t\t\t\t\tRESPECTED AUTHORITY, YOU HAVE MISSED EVALUATION PART, PLEASE FILL IT !")
else:
    print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 7 EXECUTED SUCCESSFULLY")

#testcase 3 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 8 : \n")
#USER ENTERS ONE DIGIT EXTRA IN MOBILE NUMBER
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "78984587838",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
if test_applicant_mobile(apl1.mobile_no):
    print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
else:
    print("\t\t\t\t\tPROVIDED MOBILE NUMBER ENJOYING ONE EXTRA DIGIT, PLEASE UPDATE IT!")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 8 EXECUTED SUCCESSFULLY")

#testcase 9 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 9 : \n")
#USER ABRUPTLY EXCEEDES MARKS
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "7898458783",
                         161)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
if test_applicant_marks(apl1.price):
    print("\t\t\t\t\tVALID MARKS AWARDED")
else:
    print("\t\t\t\t\tRESPECTED AUTHORITY, YOU HAVE ASSIGNED MARKS MORE THAN 100, PLEASE CORRECT IT!")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 9 EXECUTED SUCCESSFULLY")

#testcase 10
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 10 : \n")
#USER FORGEST ENETERING EMAIL-ID
apl1=applicant.save("ADARSH",
                         "",
                         "7898458783",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
if test_applicant_email(apl1.address):
    print("\t\t\t\t\tEMAIL ID NOT ENTERED, PLEASE FILL THE MISSING ROW!")
else:
    print("\t\t\t\t\tINVALID EMAIL ID")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 10 EXECUTED SUCCESSFULLY")

#testcase 11
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 11 : \n")
#USER FORGETS ENTERING MOBILE NUMBER
apl1=applicant.save("ADARSH",
                         "adarshkumar@gmail.com",
                         "",
                         61)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
if test_applicant_mobile(apl1.mobile_no):
    print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
else:
    print("\t\t\t\t\tMOBILE NUMBER NOT ENTERED, PLEASE FILL THE MISSING ROW!")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 11 EXECUTED SUCCESSFULLY")

#testcase 12 
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 12 : \n")
#CHECKING UPPER LIMIT CONDITION OF EVALUATION 
apl1=applicant.save("RAJ KUMAR SHARMA",
                         "rsharma@gmail.com",
                         "7898458783",
                         100)
assert test_applicant_name(apl1.name), "\t\t\t\t\tINVALID NAME"
print("\t\t\t\t\tVALID NAME ENTERED")
assert test_applicant_mobile(apl1.mobile_no), "\t\t\t\t\tINVALID MOBILE NUMBER"
print("\t\t\t\t\tVALID MOBILE NUMBER REGISTERD")
assert test_applicant_email(apl1.address), "\t\t\t\t\tINVALID EMAIL ID"
print("\t\t\t\t\tVALID EMAIL ID REGISTERED")
assert test_applicant_marks(apl1.price), "\t\t\t\t\tINVALID MARKS AWARDED"
print("\t\t\t\t\tVALID MARKS AWARDED")
print("\n\t\t\t\t\tAPPLICANT INFORMATION TESTCASE 12 EXECUTED SUCCESSFULLY")

print("**************\t\t\t\t\t//CONGRATULATIONS, UNIT TESTING COMPLETED, 12 TESTCASES EXECUTED //\t\t\t\t\t**************\n")