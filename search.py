#!/usr/bin/python

import pywikibot
import csv

wikidata = pywikibot.Site('wikidata', 'wikidata')

with open('/home/sidhant-gupta-004/CD.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)




sdat = {}
for info in data:
    wd_search = pywikibot.data.api.Request(
        site=wikidata,
        parameters={"action": "wbsearchentities",
                    "format": "json",
                    "type": "item",
                    "language": "en",
                    "search": info[0]})

    sdat=wd_search.submit()
    if(sdat["search"]):
        for results in sdat["search"]:
            title = results["title"]
            #print(title)
            itempage = pywikibot.ItemPage(wikidata, title)
            # you need to query and see if this page has
            # country thing. If it is there, you need to break it
            # and use that QueryTitle to insert your new values.

            itemdat = itempage.get()
            if ('P17' or 'P131' or 'P2044' or 'P625') in itemdat['claims'].keys():
                #print(title)               //Used for Checking
                #print(info[0], info[1])

                #with open('/home/sidhant-gupta-004/TEST.csv', 'wa') as fi:
                #    writer = csv.writer(fi)
                #    writer.writerows(info)

                if 'P1082' not in itemdat['claims'].keys():
                    claim = pywikibot.Claim(wikidata, 'P1082')
                    wbquant = pywikibot.WbQuantity(info[1])
                    claim.setTarget(wbquant)
                    itempage.addClaim(claim, bot=False, summary='Adding population')
                    break

            else:
                break


    #print(sdat[j])
    # print('\n')
    # if 'title' in sdat[j]['search']:
    #     print(sdat[j]['search'].get('title'), '\n')
    # j = j+1
