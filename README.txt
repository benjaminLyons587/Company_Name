
Enter this into command line first:

docker build --tag company-name .

After that finishes running you can enter in:

docker run -it company-name

This should run the docker container.

A test company is 44:38:39:ff:ef:57 you can enter that into the command line and it should return Cumulus Networks, Inc
My program has two functions one that handles the HTML request and this simply takes the 
MAC address given to it and if it is valid it returns the content from the macaddress.io
website. This is a reusable way of coding it because you can use that function to find any
other information about the MAC address aside from company name. the companyParse function
takes the content from the returned json information and parses out the company name. The separation of concerns for these two functions makes the code more modular and reusable. 


A few security considerations that I did not have time to implement would be to instead of linking the api key inside the GET request you could use a third party authentication method to mask that so that someone looking at the web traffic could not see the api key.
Another consideration is to use a log timestamps in our own internal server so that replay
attacks could not reuse the same return packet as the one you requested to try and gain
access to our system the python requests library has a request.header file so you could
pull the 'Date' from that and make sure it is a valid time and not a reused time. A combination of these two considerations would make the security of this program better 
and reduce the risk of man in the middle attacks or reply attacks.
