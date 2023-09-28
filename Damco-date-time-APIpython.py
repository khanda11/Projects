import re

#Enter the desired date format (see below) as the first argument for datechangefinal and then
#enter the current date as a string into the second argument. This will work only
#if the current date is in one of the formats below!

#1) MM/DD/YYYY: 07/04/2023
#2) DD/MM/YYYY: 04/07/2023
#3) YYYY/MM/DD: 2023/07/04
#4) Month DD, YYYY: July 4, 2023
#5) DD Month, YYYY: 4 July, 2023
#6) YYYY-MM-DD: 2023-07-04

yeardict = {
  "01": "January",
  "02": "February",
  "03": "March",
  "04": "April",
  "05": "May",
  "06": "June",
  "07": "July",
  "08": "August",
  "09": "September",
  "10": "October",
  "11": "November",
  "12": "December"
  
}

reverseyeardict= {
"January": "01",
"February": "02",
"March": "03",
"April": "04",
"May": "05",
"June": "06",
"July": "07",
"August": "08",
"September": "09",
"October": "10",
"November": "11",
"December": "12"

    }

def datechange12(date):
    date_list = list(date)
    date_list[0:2], date_list[3:5] = date_list[3:5], date_list[0:2]
    new_string = "".join(date_list)
    print(new_string)
    
def datechange13(date):
    date_list = list(date)
    date_list[6:], date_list[0:2] = date_list[0:2], date_list[6:]
    date_list[5:7], date_list[8:] = date_list[8:], date_list[5:7]
    new_string = "".join(date_list)
    print(new_string)

def datechange14(date):
    month1 = date[0:2]
    month = yeardict.get(month1)
    date1 = date[3:5]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[6:]
    print(month + " " + date1 + ", " + year)
    
def datechange15(date):
    month1 = date[0:2]
    month = yeardict.get(month1)
    date1 = date[3:5]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[6:]
    print(date1 + " " + month + ", " + year)

def datechange16(date):
    month = date[0:2]
    date1 = date[3:5]
    year = date[6:]
    print(year + "-" + month + "-" + date1)
    
def datechange21(date):
    date_list = list(date)
    date_list[0:2], date_list[3:5] = date_list[3:5], date_list[0:2]
    new_string = "".join(date_list)
    print(new_string)

def datechange23(date):
    date_list = list(date)
    date_list[6:], date_list[0:2] = date_list[0:2], date_list[6:]
    new_string = "".join(date_list)
    print(new_string)

def datechange24(date):
    month1 = date[3:5]
    month = yeardict.get(month1)
    date1 = date[0:2]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[6:]
    print(month + " " + date1 + ", " + year)
    
def datechange25(date):
    month1 = date[3:5]
    month = yeardict.get(month1)
    date1 = date[0:2]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[6:]
    print(date1 + " " + month + ", " + year)
    
def datechange26(date):
    month = date[3:5]
    date1 = date[0:2]
    year = date[6:]
    print(year + "-" + month + "-" + date1)
    
def datechange31(date):
    year = date[0:4]
    date_list = list(date)
    i=0
    while i < 5:
        del date_list[0]
        i+=1
    date_list.append("/" + year)
    new_string = "".join(date_list)
    print(new_string)

def datechange32(date):
    year = date[0:4]
    date_list = list(date)
    date_list[5:7], date_list[8:] = date_list[8:], date_list[5:7]
    i=0
    while i < 5:
        del date_list[0]
        i+=1
    date_list.append("/" + year)
    new_string = "".join(date_list)
    print(new_string)
    
def datechange34(date):
    month1 = date[5:7]
    month = yeardict.get(month1)
    date1 = date[8:]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[0:4]
    print(month + " " + date1 + ", " + year)

def datechange35(date):
    month1 = date[5:7]
    month = yeardict.get(month1)
    date1 = date[8:]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[0:4]
    print(date1 + " " + month + ", " + year)
    
def datechange36(date):
    month1 = date[5:7]
    date1 = date[8:]
    year = date[0:4]
    print(year + "-" + month1 + "-" + date1)


def datechange41(date):
    blank= date.find(" ")
    month1= date[0:blank]
    month= reverseyeardict.get(month1)
    comma= date.find(",")
    date1= date[blank+1:comma]
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(month + "/" + date1 + "/" + year)

def datechange42(date):
    blank= date.find(" ")
    month1= date[0:blank]
    month= reverseyeardict.get(month1)
    comma= date.find(",")
    date1= date[blank+1:comma]
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(date1 + "/" + month + "/" + year)
    
def datechange43(date):
    blank= date.find(" ")
    month1= date[0:blank]
    month= reverseyeardict.get(month1)
    comma= date.find(",")
    date1= date[blank+1:comma]
    year = date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(year + "/" + month + "/" + date1)
    
def datechange45(date):
    blank= date.find(" ")
    comma= date.find(",")
    date_list = list(date)
    date_list[blank+1:comma], date_list[0:blank] = date_list[0:blank], date_list[blank+1:comma]
    new_string = "".join(date_list)
    print(new_string)

def datechange46(date):
    blank= date.find(" ")
    month1= date[0:blank]
    month= reverseyeardict.get(month1)
    comma= date.find(",")
    date1= date[blank+1:comma]
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(year + "-" + month + "-" + date1)

def datechange51(date):
    blank= date.find(" ")
    date1= date[0:blank]
    comma= date.find(",")
    month1 = date[blank+1:comma]
    month= reverseyeardict.get(month1)
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(month + "/" + date1 + "/" + year)

def datechange52(date):
    blank= date.find(" ")
    date1= date[0:blank]
    comma= date.find(",")
    month1 = date[blank+1:comma]
    month= reverseyeardict.get(month1)
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(date1 + "/" + month + "/" + year)

def datechange53(date):
    blank= date.find(" ")
    date1= date[0:blank]
    comma= date.find(",")
    month1 = date[blank+1:comma]
    month= reverseyeardict.get(month1)
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(year + "/" + month + "/" + date1)

def datechange54(date):
    blank= date.find(" ")
    comma= date.find(",")
    date_list = list(date)
    date_list[blank+1:comma], date_list[0:blank] = date_list[0:blank], date_list[blank+1:comma]
    new_string = "".join(date_list)
    print(new_string)
    
def datechange56(date):
    blank= date.find(" ")
    date1= date[0:blank]
    comma= date.find(",")
    month1 = date[blank+1:comma]
    month= reverseyeardict.get(month1)
    year= date[comma+2:]
    if len(date1) == 1:
        date1 = "0" + date1
    print(year + "-" + month + "-" + date1)

def datechange61(date):
    year = date[0:4]
    date_list = list(date)
    i=0
    while i < 5:
        del date_list[0]
        i+=1
    date_list[2] = "/"
    date_list.append("/" + year)
    new_string = "".join(date_list)
    print(new_string)

def datechange62(date):
    year = date[0:4]
    date_list = list(date)
    date_list[5:7], date_list[8:] = date_list[8:], date_list[5:7]
    i=0
    while i < 5:
        del date_list[0]
        i+=1
    date_list[2] = "/"
    date_list.append("/" + year)
    new_string = "".join(date_list)
    print(new_string)
    
def datechange63(date):
    newdate = date.replace("-", "/")
    print(newdate)

def datechange64(date):
    month1 = date[5:7]
    month = yeardict.get(month1)
    date1 = date[8:]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[0:4]
    print(month + " " + date1 + ", " + year)

def datechange65(date):
    month1 = date[5:7]
    month = yeardict.get(month1)
    date1 = date[8:]
    if int(date1) < 10:
        date1 = date1.replace("0", "")
    year = date[0:4]
    print(date1 + " " + month + ", " + year)
    
    

def datefind1(date):
    if date[2] == '/' and int(date[0:2]) <= 12:
        return 1
        

def datefind2(date):
    if date[2] == '/' and int(date[0:2]) > 12:
        return 1
    
    
def datefind3(date):
    if date[4] == '/':
        return 1
    
def datefind4(date):
    pattern1 = "[A-Za-z]"
    pattern2 = "[A-Za-z0-9]"
    num = re.findall(pattern2, date)
    if(re.search(pattern1, date) and not num[0].isdigit()):
        return 1
    
        
def datefind5(date):
    pattern1 = "[A-Za-z]"
    pattern2 = "[A-Za-z0-9]"
    num = re.findall(pattern2, date)
    if(re.search(pattern1, date) and num[0].isdigit()):
        return 1
    

def datefind6(date):
    pattern = "-"
    if(re.search(pattern, date)):
        return 1
    
#1) MM/DD/YYYY: 07/04/2023
#2) DD/MM/YYYY: 04/07/2023
#3) YYYY/MM/DD: 2023/07/04
#4) Month DD, YYYY: July 4, 2023
#5) DD Month, YYYY: 4 July, 2023
#6) YYYY-MM-DD: 2023-07-04

def datechangefinal(form, date): #whichever number is entered for form, is the date format which it will be converted to
    if datefind1(date) == 1:
        if form == 1:
            print(date)
        if form == 2:
            return datechange12(date)
        if form == 3:
            return datechange13(date)
        if form == 4:
            return datechange14(date)
        if form == 5:
            return datechange15(date)
        if form == 6:
            return datechange16(date)
    elif datefind2(date) == 1:
        if form == 1:
            return datechange21(date)
        if form == 2:
            print(date)
        if form == 3:
            return datechange23(date)
        if form == 4:
            return datechange24(date)
        if form == 5:
            return datechange25(date)
        if form == 6:
            return datechange26(date)
    elif datefind3(date) == 1:
        if form == 1:
            return datechange31(date)
        if form == 2:
            return datechange32(date)
        if form == 3:
            print(date)
        if form == 4:
            return datechange34(date)
        if form == 5:
            return datechange35(date)
        if form == 6:
            return datechange36(date)
    elif datefind4(date) == 1:
        if form == 1:
            return datechange41(date)
        if form == 2:
            return datechange42(date)
        if form == 3:
            return datechange43(date)
        if form == 4:
            print(date)
        if form == 5:
            return datechange45(date)
        if form == 6:
            return datechange46(date)
    elif datefind5(date) == 1:
        if form == 1:
            return datechange51(date)
        if form == 2:
            return datechange52(date)
        if form == 3:
            return datechange53(date)
        if form == 4:
            return datechange54(date)
        if form == 5:
            print(date)
        if form == 6:
            return datechange56(date)
    else:
        if form == 1:
            return datechange61(date)
        if form == 2:
            return datechange62(date)
        if form == 3:
            return datechange63(date)
        if form == 4:
            return datechange64(date)
        if form == 5:
            return datechange65(date)
        if form == 6:
            print(date)
   
    

    
    