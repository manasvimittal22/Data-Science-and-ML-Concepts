install.packages("RMySQL")
library(RMySQL)
#
mydb <- dbConnect(MySQL(), user = 'studentuser', password = 'DBMS*spring2022',
                  dbname = 'world', host = '129.10.79.239')
#
dbListTables(mydb)
#
dbListFields(mydb, 'city')
#
rs <- dbSendQuery(mydb, "select c1.Name 
                  from country c1, countrylanguage c2 where c1.code = c2.countrycode
                 and c2.language = 'english'")
#
mydata <- dbFetch(rs)
#
mydata
#
dbClearResult(rs)
#
dbDisconnect(mydb)
#