# French-Expression


To learn anything, I use an application nammed Anki. This application is based on two elements which help you to memorize anything : Spaced repetition and Flash Card.

A flash card is a "Card" on which you have a question on one size and the answer on the other size. The concept is pretty basic, but using it push you to revise in a active manner which help you to memorize faster. Moreover, ask question about a topic is one of the best way to achor deeper your knowledge into your mind.

Spaced repetition is the fact of reviewing your knowledge on a regular basis. Once again, this is necessary to memorize on the long run. But more you review something, more you will remind things about it. So you need to review it less and less often. For instance, after learning something for the first time you forget about 50% of what you learn 1 day later. But after you revision, it may take a week to forget as much, and then a month, and then a couple months...

You get the idea. The time needed between each session of revision goes exponentialy. Thus to learn in the most effective manner, you must use this concept. But it is hard to implement... That is why Anki is so useful!

So let's get back to the story of this algorithm.

In class, one of our teacher show us a website (http://www.expressio.fr/) listing lot of expressions, their meaning and their origin. I found it interesting and I wanted to add it on Anki.

But as there is about a thousand expression listed on the site, this will take some time to do manualy. And that is where this algorithm take place.

I found this page : http://www.expressio.fr/toutes_les_expressions.php Which definitively help me a lot.
So I get the html code of this page, parse it to get all the urls of the expressions.

Then parse again each page and put it in a format Anki is supporting. Then we are done! I import it on Anki and I can easily learn it.

There is only one page which I can't parse which is : http://www.expressio.fr/expressions/une-nuit-blanche.php because it has some russian characters (« белые ночи ») that the file was not supporting... 

So I deleted It manualy.

If you also want to learn french expression. Contact me (guillaume1.thomas@protonmail.com), I will explain you how to use it
