# brewtiful
This app began with my adoration for quality craft beer, especially the beautifully packaged kind. 

I began by writing a scraper to scrape all of the information off the [National Brewer's Association Membership roster](https://www.brewersassociation.org/directories/breweries/). You can read more about that [here](https://github.com/nealykehres/brewery-scraper).

I had to parse the data further using Pandas. This was my first time using pandas, but it did what I needed it to pretty quickly so I enjoyed it. 

Next, I used Flask to create an app that would allow uses to choose a state and then view all the logos of the breweries in that state. I used [this code](https://github.com/WebsiteBeaver/interactive-and-responsive-svg-map-of-us-states-capitals) to create a map that was interactive to be displayed at the top of the page. 

I used the [Clearbit Logo API](bit.com/logo) to collect the images of the logos. This API is very imperfect. It yielded a number of broken images, so I handled that by styling the broken images to appear somewhat decent on the page. It didn't accomplish my goal of displaying all of the logos, but it allowed me to use the API for most of the images while maintaining a decent looking web app. 

I used [fip.js](http://nnattawat.github.io/flip/) to create the flipping animation that allows users to view more information about the breweries behind the logos. Sometimes it allows users to see the front of the card even after the flip. Based on my research, this in unavoidable on Google Chrome. 
