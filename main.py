import mechanize
import urllib
import sys
from bs4 import BeautifulSoup
br = ""
############################################################################
def setEncoding():
    reload(sys)
    sys.setdefaultencoding('utf8')
############################################################################
############################################################################
def startSurfing():
    url = "http://quotes.toscrape.com/search.aspx"
    br = mechanize.Browser()
    br.open(url)
    br.select_form('filterform')
    br.form.set_all_readonly(False)
    for form in br.form.controls:
        print form
        if form.name == "__VIEWSTATE":
            __VIEWSTATE1 = form.value
            print '__VIEWSTATE1 Value {}'.format(__VIEWSTATE1)

    #Select author; for this Albert Einstein
    author = "Albert Einstein"
    tag = "----------"
    __VIEWSTATE = __VIEWSTATE1
    ##############################################################################
    #Sending post request After selecting Author...
    data = urllib.urlencode({'author':author,'tag':tag, '__VIEWSTATE':__VIEWSTATE1})
    resp = br.open('http://quotes.toscrape.com/filter.aspx', data)
    ###After sending first POST request select the TAG from the Drop Down list
    print "getting values after send first POST"
    br.select_form('filterform')
    for form in br.form.controls:
        print  form
        if form.name == "__VIEWSTATE":
            __VIEWSTATE2 = form.value

    print "__VIEWSTATE2 value is {}".format(__VIEWSTATE2)
    print  "============================================================================================="
    tag = "inspirational"


    #data = urllib.urlencode({'author':author,'tag':tag, '__VIEWSTATE':view2})
    #resp = br.open('http://quotes.toscrape.com/filter.aspx', data)
    br.select_form('filterform')
    for form in br.form.controls:
        print form
    #br.select_form('filterform')
    ###Set the TAG value from the drop down list. In this case we chose 'inspirational'.
    br.form.set_value([tag],"tag")
    ##################################################################################

    print "Final Form status before sending latest POST request..."
    print ""
    print "========================================================================================"
    submit_button = "Search"
    data = urllib.urlencode({'author':author,'tag':tag,'submit_button':submit_button, '__VIEWSTATE':__VIEWSTATE2})
    resp = br.open('http://quotes.toscrape.com/filter.aspx', data)
    return resp
########################################################################################################

###Main#########
resp = ""
setEncoding()
resp = startSurfing()

soup = BeautifulSoup(resp.read(),"html5lib")
print "Title:{}".format(soup.title.text.rstrip().lstrip())
print "Author:{}".format(soup.find("span",{"class":"author"}).text.rstrip().lstrip())
print "Results:{}".format(soup.find("span",{"class":"content"}).text.rstrip().lstrip())
#a=soup.find("span",{"class":"author"}).text
#print a
#print(soup.prettify())






