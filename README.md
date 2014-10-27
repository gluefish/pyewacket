#Pyewacket

Pyewacket was the name of a cat in the novel Bell, Book and Candle.  It was also the name of a familiar spirit in Salem during the witch-hunt days.  Here, it is the name of a test automation framework under development.

Py, of course, refers to Python, the scripting language / programming language (depending on your point of view).  Wa refers to Web Application.  T is for Testing.  Cke is still up for grabs.  You choose.

![logo](http://www.gluefish.com/Documents/pyewacket/pyewacket.png "")

##Description

Web applications are in short, web pages being made available to various browsers such as Google Chrome, Firefox, Internet Explorer, Safari, and phantomJS.  Whenever you type an address into the address bar of the browser and hit enter, assuming you have an internet connection, the result is that you see a web page appear on the screen.  

Under the covers of that web page is some code that instructs the browser how to display the contents.  In order to start test automation against that page, we need to have our programming language be able to see and interact with the objects described in that code.

Using Python, we can do several things that make that possible:
- A python add-in called webdriver makes python able to see and interact with web page options
- Another python add-in called gspread allows python to interact with cells in a Google Docs spreadsheet, which can then be used to maintain the manual and automated steps to edit the test.
