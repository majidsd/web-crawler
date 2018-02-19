# Simple Web Crawler

<h4>
  Large search engines use thousands of continually running web crawlers to discover web content
</h4>

<h4>
  Web crawlers fetch a page, place all the page’s links in a queue, fetch the next link from the queue, and repeat
</h4>

<h5>
Here we will cover two codes, one is just simple program that crawl all links, and other do the same as the first and adding save URL as MD5, also the scond has limit to url to be covered, use 10 as default if the user does not enter the value, but first let us setup the environment and then explain the code 
</h5>

<h4>Setup Environment</h4>
<p> To do that we have to install three stuff: <p>
<ol>
  <li> Install Python </li>
  <p> We can install Python by going to thier <a href='https://www.python.org/downloads/'> offical site </a> and then setup the python in your platform (Windows or Linux), you will find help in thier if you have a problem </p>
  
  <li> Install BeautifulSoup </li>
  <p> After installing Python, open cmd on Windows or terminal on Linux, then install BeautifulSoup using this command
  <br />
  <code> pip install beautifulsoup4 </code>
  </p>
</ol> 

<h4> The Code </h4>
<h6>We have two codes here, the first just simple application that crawl all the sites of the given lists of site, and the second do same as the first plus limit of sites and filter for the site<h6>
<ul style="list-style-type:circle">
  <li> <h4> simple_web_crawler </h4> </li>
  <li> <h4> simple_web_crawler_with_hashed_urls </h4> </li>
</ul> 
