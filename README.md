# WEB-SCRAPING
In this repositiory we will see web scraping, web scraping automatically extracts data and presents in a format in which we can easily make 
sense of,With the help of python library beautiful soup i extracted the news from different websites. Beautiful soup is used for pulling data out
of HTML and XML files. It works with our favourite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
it commonly saves programmers hours or days of work.
I scrapped the BBC NEWS, BLOOMBERG, NEW YORK TIMES,TIMES OF INDIA,CNBC websites.
The input should be any topic on which we want trending news, it is then concatenated with all the URL'S of the new websites. Using for loops,
'headlines','description','link','date' are pulled out of every news from every website.All the four things of every news is stored in a dictionary with keys as 'headlines'
,'link','date' and 'descriptor'. The date is changed to a particular formate "<YYYY-mm-dd> so that it will be easier to sort in a database later. Then finally
inserted in the database. Then with command db.collection_name.find().sort({"date":-1}) all the news are sorted in descending order.
