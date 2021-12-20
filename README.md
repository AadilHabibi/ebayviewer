# EbayViewer

Utilizes REQUESTS library of Python in order to send views to ebay listing (Which in turns makes the listing go up on the search criteria). In order to not get "caught", the bot needs proxies in the proxies.txt file in the format: proxy:port:user:password

Note: You NEED to have proxies in order for script to run. Additionally, you need to have more number of proxies than views you want.

Process:
1. Ask user for link 
2. Ask user for views 
3. Use requests library to send x views over to link

