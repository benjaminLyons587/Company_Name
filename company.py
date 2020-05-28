import requests
import json

    
#Function to try/except if request was successful and if it was than it parses the json to print the company name if not it returns an error
def htmlRequest():
    
    #Input Address
    address = input("Type the MAC address of the company you want the name of:")

    #HTML request in json format searching for input MAC address
    response = requests.get("https://api.macaddress.io/v1?apiKey=at_qIclgvOYlrY5zfslzzYYurorGl7ha&output=json&search={}".format(address))

 
    #First Security and flow consideration is to make sure the REST API status code is OK instead of something else so this try/except does that
    try:
        response.raise_for_status()
        
    except requests.exceptions.HTTPError as e:
        print("Exception: " + str(e))
        return "Exception: " + str(e)
        
    content = response.content
    
    return content

#This takes the raw json data that the htmlRequest function got and parses our the company name string.
def companyParse(content):
    try:
        parsed = json.loads(content)

        vendorDetails = parsed["vendorDetails"]

        companyName = vendorDetails["companyName"]

        if companyName== "":
            print("This MAC address returned no vaild company")
        else:
            print(companyName)
        
        return companyName
    
    except:
        print("This is not vaild json data to find the company name")
    
def main():
    content = htmlRequest()
    company = companyParse(content)

if __name__ == "__main__":
    main()
    

