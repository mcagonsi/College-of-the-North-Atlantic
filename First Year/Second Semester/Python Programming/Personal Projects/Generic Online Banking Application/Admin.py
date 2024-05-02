from objs import actors as a
import mysql.connector as db
import random
from datetime import datetime,date,timedelta

accountsID = random.randint(1000,9999)
accountNumber = "{}{}".format(str(accountsID),str(random.randint(1000,9999)))
fname = 'michael'
lname = 'Agonsi'
sex = 'male'
dob = '2000-01-01'
relationship ='single'
phone = '+15555555555'
stateOfOrigin ='imo'
countryofOrigin ='Nigeria'
streetAddress ='30 Diana Road'
town ='St. Johns'
country ='Canada'
postalcode = 'A1B1H8'
id = 0
onlinebankingid = 0
C = a.Customer(fname,lname,sex,dob,relationship,phone,stateOfOrigin,countryofOrigin,streetAddress,town,country,postalcode,id,onlinebankingid)

parameters = (C.FirstName,C.LastName, C.Gender, C.DateOfBirth,C.Relationship, C.PhoneNumber, C.StateOfOrigin, C.CountryOfOrigin,C.StreetAddress, C.City, C.Country,C.PostalCode)

query = 'insert into customer values (default,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,NULL);'


con = db.connect(host='localhost',user='root',passwd='root',port=3306,database='bankdb')
c = con.cursor()
c.execute(query,parameters)
con.commit()

# query ='select * from accounttype;'
# c.execute(query)
# for row in c.fetchall():
#     print(row)
print('successfully inserted')