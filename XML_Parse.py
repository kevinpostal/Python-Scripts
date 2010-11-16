#### Kevin Postal ###
#  Lets parse this xml like it's chop salad
# 2010
##

import os,sys, glob, time, datetime
from xml.dom import minidom

def check_xml(file):
    try:
        xmldoc = minidom.parse(file)
        ExtendedInfo = xmldoc.getElementsByTagName('ExtendedInfo')[0]
        salesNumber = ExtendedInfo.getAttribute('salesNumber')[:5] #Grab only 5 characters
        if salesNumber == SALES_NUMBER:
            format_xml(xmldoc,file)
    except:
        pass
        
def format_xml(xmldoc,file):
    ##### OLD FUNCTION ######
    # Lamda Function I wrote to remove all but 4 chars and add #'s as placeholders
    #truncate =  lambda x: "#" *  ( len (x) -4 ) + x[-4:] 
    #########################
    
    # New lamda... Which just grabs last 4
    truncate =  lambda x: x[-4:] 
    
    PrincipalCollection = xmldoc.getElementsByTagName('Principal')[0]
    BankInformation = xmldoc.getElementsByTagName('BankInformation')[0]
    BusinessInfo = xmldoc.getElementsByTagName('BusinessInfo')[0]
    
    # Truncate all the values
    socialSecurityNumber = truncate(PrincipalCollection.getAttribute('socialSecurityNumber'))
    transRoutingNumber = truncate(BankInformation.getAttribute('transRoutingNumber'))
    dDA = truncate(BankInformation.getAttribute('dDA'))
    federalTaxID =truncate(BusinessInfo.getAttribute('federalTaxID'))
    
    #Set new values
    BankInformation.setAttribute('transRoutingNumber',transRoutingNumber)
    BankInformation.setAttribute('dDA',dDA)
    PrincipalCollection.setAttribute('socialSecurityNumber',socialSecurityNumber)
    BusinessInfo.setAttribute('federalTaxID',federalTaxID)
    
    write_to_file(xmldoc,file)

def file_list(LOCATION):
    for folder in glob.glob(LOCATION):
        # here .xml files, but could be .txt files or whatever
        for file in glob.glob(folder + '/*.xml'):
            # retrieves the stats for the current file
            # the tuple element at index 8 is the last-modified-date
            stats = os.stat(file)
            # put the two dates into matching format    
            lastmodDate = time.localtime(stats[8])
            expDate = time.strptime(xDate, '%Y-%m-%d')
            file, time.strftime("%m/%d/%y", lastmodDate)
            # check if files-modified-date is outdated
            if expDate < lastmodDate:
                check_xml(file)

def write_to_file(doc, file):
    date = datetime.datetime.today().strftime("%Y%m%d")
    name = "%s/OUTPUT/%s_%s" % ( os.path.dirname(file),date,os.path.basename(file) )
    file_object = open(name, "w")
    doc.writexml(file_object,addindent="    ",newl="\n")
    file_object.close()

def main():
    file_list(LOCATION)
    
if __name__ == "__main__":
    #Directory the python script is being ran from
    LOCATION = os.path.dirname(sys.argv[0]) + "\\"
    
    #Make Sure we have an output folder
    if not os.path.exists(LOCATION + "OUTPUT"):
        os.makedirs(LOCATION + "OUTPUT")
        
    SALES_NUMBER = '02657'
    xDate = '2010-11-15'
    main()
    
