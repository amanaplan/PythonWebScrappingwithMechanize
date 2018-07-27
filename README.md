# Mechanize
Dealing with ASP.Net Pages

Websites built using ASP.Net technologies are typically a nightmare for web scraping developers, mostly due to the way they handle forms.
These types of websites usually send state data in requests and responses in order to keep track of the client's UI state. 

An ASP.Net website would typically store the data that you filled out in the previous pages in a hidden field called "__VIEWSTATE" which contains a huge string like the one shown below:


This is a Base64 encoded string representing the client UI state and contains the values from the form. This setup is particularly common for web applications where user actions in forms trigger POST requests back to the server to fetch data for other fields.

The __VIEWSTATE field is passed around with each POST request that the browser makes to the server. The server then decodes and loads the client's UI state from this data, performs some processing, computes the value for the new view state based on the new values and renders the resulting page with the new view state as a hidden field.

If the __VIEWSTATE is not sent back to the server, you are probably going to see a blank form as a result because the server completely lost the client’s UI state. So, in order to crawl pages resulting from forms like this, you have to make sure that your crawler is sending this state data with its requests, otherwise the page will not load what it's expected to load.

REFERENCE:https://blog.scrapinghub.com/2016/04/20/scrapy-tips-from-the-pros-april-2016-edition
