Module 11.1 
    All setup and installation 
Module 11.2 
    To perform web scraping, we need to tell splinter and beautiful soup what data to extract and where to find it. 
    HTML - Hypertext Markup language - the foundation of all web pages. 
    HTML elements - the basic building blocks of a webpage. 
    Hypertext - Text that links one section of a webpage to another section or another document. 
    The backbone of the internet beause it enables interactivity. 
    Markup - the act of making annotations on a document. 
    HTML is used to annotate and structure a webpage. 
    HTML doesn't create a visuall compelling page.  
    CSS allows you to add style, formatting, layouts and colors. 

    CSS is a declarative language - it declares or describes the effect that you want on your site. 

    Sample code: 
    <html>
<Head>
    <title> Document</title>
</Head>
<body>
    <p>Hello, world!</p>
</body>
</html>

    HTLM tags are instructions that tell a browser how to display elements on a webpage. 
    Opening tags <TAG> the name inclosed in angle brackets
    Closing tags </TAG> the name included in brackets with a slash at the beginning 

<HEAD>
 always contained in an HTML document 
 Contains information about the document itself (metadata) 
 Can also contain information that does not display on the site. 

 <Body>
 Contains all elements that display on the site. 

 Declarations and metatags
 VS Code has some base 'templates' to use - 
 Open a .html file - place a ! on the first line and press enter 

 Will populate with the code below: 
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

<!DOCTYPE HTML> - This is a declaration and not a tag.  It informs web browsers of the version of HTML that the document uses and should always be the first line in a document.
The default version is HTML 5 - curently the most widely used. 

<html lang = 'en'> - this specifies that English is the language that HTML uses.  This is a language attribute.  Tells screen readers which pronunciation engine to use. 

<head> - opens the head section - serves as a container for the setup elements. 

<meta> - metadata tags are placed in the head section - give basic information - lke page width to the web browser. 
More info on metadata tags can be found here: 
https://www.w3schools.com/tags/tag_meta.asp
<meta> tags are singleton tags - they don't need a closing tag. 

<meta> and <title> tags are indented - this makes the code easier to read. 

Headers and Lists 
<ul></ul> - nonnumbered (unordered) lists 

self-closing tag - <body /> - this is a concise way of referring to a set of opening and closing tags along with any content that appears between them. 

<h1> - Header - displays larger and bolder than other text on the page. 
    H1 - H6 
<p> - Paragraph tag
<ul> unordered list (bulleted items)
<li> list item 


 <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    This line should be below. 
 </p>

 The code above all displays on the same line.  HTML ignores white space (including return characters and extra spaces) 
To create a new line, you need to add a new <P> tag. 

 <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. </p>
 <p>This line should be below. 
    </p>

Links 
HTML links include 3 parts 
    Anchor tag
    href attribute
    text that the browser will display for the link 
    ex: <a href="https://pandas.pydata.org/">Pandas Website</a>

    This creates a link to the pandas library website. 
    <a> - this is the anchor tag - letting the browser know the link is coming. 
    href - sets the attribute to the URL of the pandas website 
    Pandas Website - The text that displays to the user. 

Divisions 
<div> doesn't add an element to the webpage but helps organized HTML elements 
Establishes divisions or sections within the body 
<div> tags don't change the appearance of the HTML code. 
It adds to code readability - which is more important in longer more complex pages. 

11.2.6 - Web Scraping with Beautiful Soup 
(Link to Jupyter Notebook - HTML_Case_study)

BeautifulSoup is the library that will be used to parse an HTML document. 

html_soup = soup(html, 'html.parser'_

this will return all code that is assigned to the HTML variable.  

html_soup.title
    This will grab the title element. <title>Document</title>

html_soup.title.text - will pull only the text of the title element 
You can enclose a string that spans multiple lines within triple quotation marks ex. """<code>"""

html_soup.find("div")
while the document contains two <div> tags, the code only returns one. The find method will only return the first instance of the element that its searching for. 


11.3 - Understanding CSS 
CSS - cascading style sheets 
Allows you to tailor the appearance of HTML in the browser. 

<style />
<style>
    p {
        color: blue;
    }
</style>
This sets the text of all paragraphs to blue 

Typically place CSS stylings in separate files that are imported into the HTML document. 
Better organization and separation of code. 

you can set IDs and drive styling for specific elements using CSS.  (see below)
    #first_div {
        color: red; 
    }
    #second {
        color: blue;
    }

can select mulitiple elements at one time by creating and setting classes.  (see index5.html)

<style>
    .even {
        color: blue;
    }
</style>

#second {
    color: blue;
}

only a single element can use a particular ID attribute, multiple elements can share a class.  Gives you more flexibility for customizing (or scraping) sites. 


11.4 - Gaining a deeper understanding of a Website structure 

Using Chrome DevTools will make it easier to identify an element and CSS selector - which are then used to scrape data from the element.  

<body /> - a tag container of every element that appears on a webpage. 
All other containers exist within these elements - 
Multiple levels of nesting can exist - depending on how elaborate the site is. 

When hovering over any part of the code, the connected visual will get highlighted on the website.  (helps by showing where the code is tied in. )

You can search within Dev Tools (Ctrl F) 

11.4.2 - Using HTML Class and ID Attributes 
It's important that attributes are unique or organized into groups. 

<li /> - List element 
<ul /> - Unordered list

drilling down - manuvering through nested elements. 


11.5.1- Performing an automated web scrape 
Make sure you are reviewing Terms of Service and Terms of Use to see what the rules are on using data. 
Many sites don't allow automated browsing and scraping
    Traffic can overload a server and cripple a website. 

Need office hours - i can't get splinter to work - it's installed (also uninstalled/reinstalled) and it does not seem to be recognized. 