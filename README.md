# MWTL Hackathon
This Python script is a small program written during the the Wikimedia Hackathon at Amrita University, Amritapuri on the 1st and 2nd October 2016. It adds population data to towns/villages within a district where the location names and population figures have been manually derived from the Indian Census 2011.

## Disclaimer
This is a script which allows you to make edits directly in Wikidata which show up there instantaneously. So be careful. And (of course) I take no responsibilty for how this code may be reproduced, modified and/or used.

## Prerequisites
* Register an account at Mediawiki.
* Refer to the notebooks at: https://gist.github.com/AbdealiJK/05b8d2e6ded9bcb58e10deb16c7bacd5 . Clone the contents of this repository and then signup in PAWS at: https://paws.wmflabs.org . This allows you to use the notebooks provided. Read up till `03 - Wikidata.ipynb`
* Install the pywikibot python module locally by following the instructions provided at the end of `02 - Intro to pywikibot.ipynb` . This is an optional step but I personally believe that once you start doing the related coding and understanding yourself, you will learn much more, much more efficiently (and that can be done better locally).
* You will need to refer to the following link in order to write some required functions: https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Quantities_and_Units

## Deployment
Python, as we know, is an easy language. So there is not much on HOW to write the code. Just note that you should completely understand `03 - Wikidata.ipynb` and `05 - Getting census data.ipynb` because you need to know these properly to write this program.

The other part is WHAT to write there. This is only simple logic.  
You first search Wikidata for the particular town/village by name. This will show a few search results and you will need to decide which result is actually a place (and not a band name). For this, you have to go to the key (as the JSON data is converted to a dictionary by pywikibot) 'claims' within `itempage.get()` (the command to 'get' the object from wikidata), given the variable name you choose is 'itempage'. Here, you will check if the claims within the page are like 'Country' or 'Coordinate Location', etc. Here, the condition should also include that 'population' is NOT a part of the claims already, because the function we are using adds a claim, hence, then, we will have 2 population values (not good).

After determining which item within Wikidata to edit, you have to follow the code as shown in the link referred above (refer the given code as well), add the value to the population claim, and run the program.

## Further Development
* So we have a poulation attribute. But WHEN did the area have these many residents? We need to provide a 'Reference' to show that this data belongs to 2011. That is an essential piece in the code which needs to be patched, without it the population data can be regarded useless.
* The database is also missing validation, WHO says that this is the value of population at this place? We need to add a 'Source' claim and give it the value 'Indian Census 2011'.
* Another fact is that the code only checks some parameters of a location and not all. As a result, some places without the population value but within the chosen district were left out. The code neither checks if the present value of population is correct or not.
* Also, in some remote cases, the towns/villages do not exist on Wikidata, for this, no provision is provided to create an item.

This script, hence, can be inferred as the most basic form (maybe less) of a potentially interesting program to work on.

## Authors
* Sidhant Gupta - sidhant-gupta-004 (GitHub)  
                - guptasidhant004@gmail.com (Email)
                
## Acknowledgements
* FOSS@Amrita  
The organisers of the Hackathon have done a wonderful job in providing an excellent platform to students who have just been introduced to Open Source concepts - and this event was very important and informative towards our goal of Open Source Development.
* Abdeali JK  
I would thank him for his guidance (and resources) which form everything that is there in this code.
* Help  
I would also like to thank my seniors at the club (Tony etta and Srijan bhaiya), who helped me with the code - in checking the title of an attribute and reading the CSV file for the data of towns/villages.
