import requests

'''
    Process:
1. Ask user for link -- Done
2. Ask user for views -- Done
3. Get proxies to work -- Done
4. Grab the link and send x views over -- Done
'''
proxyDict = {}

def getViews(ebayLink, numViews, proxyDict):
    for proxy, viewNum in zip(proxyDict, range(numViews)):
        print(f"Adding view #{viewNum} with proxy: {proxyDict[proxy]}")

        with requests.Session() as s:
            r = s.get(ebayLink, proxies = {"http": proxyDict[proxy], "https": proxyDict[proxy]})
            #print(r.status_code)

itemLink = input("What is the link you would like to add views to?\n")
amtOfViews = input("How many views would you like to add? \n")

amtOfViews = int(amtOfViews)

# Reading the proxies and re-arranging them into proper order
with open('proxies.txt') as f:
    #Gets rid of the newline character
    lines = f.read().splitlines()

    '''
    Try turning this into List Comprehension
    '''
    for proxy in lines:
        #proxyDict[proxy] = []
        proxyDict[proxy] = proxy.split(':')
        fullProxyStr = 'http://' + proxyDict[proxy][2] + ':' + proxyDict[proxy][3] + '@' + proxyDict[proxy][0] + ':' + proxyDict[proxy][1]
        proxyDict[proxy] = fullProxyStr
        #print(proxyDict[proxy] + '\n')


print("Sending views now... \n")
getViews(itemLink, amtOfViews, proxyDict)
