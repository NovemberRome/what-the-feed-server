# What The Feed server

What The Feed is a social media aggregration platform that helps you follow related social media accounts at once. Suppose you are interested in some topic, say "Indian Finance", WTF will automatically find the leading social media accounts for that topic, follow their posts and provide you with an aggregrated feed. These topics are called "subscriptions" and you can subscribe to as many topics as you want. Companion Android app is [here](https://github.com/iiitv/hackathon-fullstack-app)


## Hackathon

This was team FullStack's project for IIITV Hackathon 2016. Team members were - 
* Avi Aryan [@aviaryan](https://github.com/aviaryan)
* Pratyush Singh [@singh-pratyush96](https://github.com/singh-pratyush96)
* Raju Koushik [@RajuKoushik](https://github.com/RajuKoushik)
* Vaibhav
* Vikas

Social networks that were integrated at this point are Twitter, Instagram and Tumblr.


## Working

* To get quality social media accounts for a topic (*phrase*), we do a google search and fetch the top results. Example, for top Instagram accounts of "Indian Fashion", we search google for "site:instagram.com Indian Fashion - instagram" and with some regex we fetch links to top instagram accounts. Same goes for other social media.
* To get the recent posts of an account, we are using their respective APIs. 


## Documentation

Some documentation of the API is in [wiki](https://github.com/iiitv/hackathon-fullstack-server/wiki)


## Future Plans

Let's see.