# Machine Learning in Production



72.10.32.23

Welcome, to another episode of IPAs and APIs ...the support group for people who are too awesome for other Tech meetups.

Formalities...

- Recruiter pitches
- Job announcements



## Quick Explaination of APIs and IPAs

For those of you who are new to the group, APIs and IPAs has only a little to do with either IPAs or APIs.

...The original idea was stolen from the classical greek symposium... symposium was an all day drinking event where greek men and hetaera (extreme educated prostitutes), would get together and talk about technology, and philolsophy.

We added a few things to the format, such as this spring we did a charity hackathon, and this fall I'd like to put together a project surrounding the election. But generally our meetup is Technology and Drinking.

### So Let's talk about Machine Learning in Production?

Quick show of hands?

How many of you hate it when a speaker polls you at the beginning of a speech?

Yea... me too. Lol

So I was a sales guy and as a sales guy they professionally trained and taught me how to give a proper speech... so now you know why this is going to suck so bad

### Three goals:

1. Machine learning is hotter than doughnut grease right now... we'd like to make it more approachable, and give you a "Developers intro"
2. Help y'all understand what you should be getting paid
3. Entertain and Delight.

### Sacha and I will be Tag teaming this one...

She's going to cover the data science portion and like all good husband I'm going to do all the hard work. Just kidding.

Actually though I'll tell a quick story... we went on a mini-honeymoon mid-august and when we stopped for lunch, the guide was like... okay everyone lunch is ready, now just to prove that chivalry is not dead we are going to let the only woman on this trip go ahead of everyone else so she can make her husband a sandwich.

Lol. Sacha is the brains of the operation.

But before we get into the meat and potatoes, let me tell you a little bit about me, and then Sacha can tell you a little bit about herself :slightly_smiling_face:

### About Me

Twitter handle/ Github handle

Because I'm already conceited enough I actually prefer to lead an "anti resume" when talking about myself. This was popularized by princeton professor Johannes Haushofer. 

* I almost failed out of high school because I used to like to skip class and hang out and read in library. I'd go surfing when the waves were nice too. 
* The direct result of my hard work in high school was that I was only let into Universities that liked my SAT scores. Thank god for the University of Kansas #Rock Chalk. The admissions have gotten harder. 
* When I made my way into the professional world, I didn't find a "real" job for about 18 months.
* Eventually I did however, and after 4.5 years of 70 hour weeks I made my way to the peak of my career when I promoted to run NYC for verizon's largest retailer... only to be demoted for sending funny corporate emails a couple months later. 
* Along the way I've almost died a bunch of times, included in that list are things like almost being drowned by a pod of dolphins, jumping off of a cliff into 2 ft of water in a rock quarry, almost being hit by a subway to impress a girl, and other funnier stories that I won't say in public. 

I mention all of this primarily to point out that if a guy like me, an American that was almost deported to Canada, can learn machine learning you can too. 



### Machine Learning Overview

What is it...

![Machine Learning](/Users/Pope/Desktop/Screen Shot 2018-09-08 at 8.25.08 AM.png)



#### My perspective...

> Machine learning is using statistics and data to replace the need for explicit programming. 

or put another way... 

>  "Using math to do the hard parts of your job."

### Why does it matter? 

This may be a little bit of an exaduration... if you don't learn this stuff you are probably going to be out of a job.

#### Machine learning has a lot of subtopics:

* Supervised Learning (I know what I want)
* Unsupervised Learning (Here's data, tell me something I didn't know)

* Regression (how this thing relates to this other thing), 
* Classification (how these things are alike and different)
* Clustering algorithms (there's a bunch of groups find the groups)
* Reinforcement learning (Rewards good behavior)
* Artificial Neural Networks (Making ML harder by explaining with graphs)
* Convolutional Neural Networks (In case explaining ANNs weren't hard enough)

* Deep learning (Another reason to buy Google, Amazon, and Microsoft Stock)



 Twitter handle/ Github handle



## Data Science

### What is a data scientist? 

* I found this image and emailed it to my whole family because they kept asking me what the heck I was doing with my time.

* Jon's definition of a data scientist is : a statistician that works with data that is too big to fit on one computer. 
* I, personally, have a tough time explaining what a data scientist is. But it is the career I'm trying to pursue right now. And, my family is always asking. What are you studying? What can you do with that degree? I quickly grew tired of trying to explain this new and wonderful Data Science career, so I turned to Google for help. And I was satisfied with pictures and diagrams I found. Who doesn't like pictures? 
* I chose this image to email my whole family so they'd stop asking me...They have a male figure, but I like this one for obvious reasons.
* And since Halloween is coming up...I also wanted to share this one!
* So now, my standard reply is : Imagine if Computer Science, Mathematics, and Statistics had a baby. Scientific, right? But, I feel like it works. 

(Source: https://en.wikibooks.org/wiki/Data_Science)

### About Sacha

- My math and stats interest began in high school. I graduated Corona High as valedictorian. 
- Although I was accepted to Berkeley, UCLA, and UC San Diego, I decided to go to UCI. 
- After changing my major 6 times or so, I then pursued and completed a Pure Math degree with a minor in statistcs. 
- After graduation, I ran a few tutoring centers for Mathnasium Corporation for about 2 years. 
- Then, I wanted to go back to school for Statistics. So, I left Mathnasium, tutored on the side for extra cash, studied for the GRE, and researched schools. Fate brought me back to UCI. 
- And that's where I am now. 
- Some irrelevant, but fun facts about me...I love teaching, I can sing, and my recent obsessions are gardening, horticulture, & insects.
- Anyhow, we've been doing IPAs and APIs since August 2015. We love it, and we're really glad you're here after our small hiatus since April. So, thank you.  

### The Project

* So, let's talk about the project. 
* I was surprised to find that the majority of a Machine Learning included a lot of what I have been studying this past year. It's a lot of Statistics, actually. 
* BUT, I don't want to scare you. You don't need a degree in Stats to do this. However, later, I will go over a few stats concepts you **should** know. 

### General Steps 

0. Define Your Question(s)

1. Get Data
2. Clean Up/Organize
3. Data Mining / Play with it!
4. Build a Model
5. Test and Confirm
6. If you want...Do something with it! 

*I will go over Steps 1-5 and Jon will talk about Step 6.* 

(Source: https://blog.dataiku.com/2016/07/06/fundamental-steps-data-project-success)

### 1. Our Questions

### 2. Get Data

* [Stack Overflow 2018](https://insights.stackoverflow.com/survey/2018/)
* Insert all the Variables.

This survey covered **many** different types of questions. Depending on your goal, you don't need to use information from **every** variable you obtain.


* How we created our subset. For 'pedagogical reasons,' we concentrated our analysis on US full-time developers. 
* EDA to support our choices and make naive speculations. 

### Clean up Data / Organize

#### Challenges

1. **Some questions allowed you to pick more than one category that you fall under.**

   Example: What kind of developer do you identify as? (*DeveloperType*)

   Here are all the categories that respondent #2 thought described him best.

```R
> StackOverFlow_Data$DeveloperType[2]
[1] "Web developer; Mobile developer; Embedded applications/devices developer; Machine learning specialist; Data scientist; Graphic designer; Desktop applications developer"
```

​	You can deal with this many ways, but what I did was create dummy variables for each category. So, there was one column per selection and if the user classified themselves as a web developer, then the value would be 1 and if not the value would be 0. There was about 20 unique categories. But, for this presentation I only created the top 11 categories.

2. **Some questions had many levels (even though you were only able to choose one) + different forms of 'NAs'.**

   Example: How many employees does the company you work for have? (*CompanySize*)

   You can also deal with this many ways, but what I did was eliminate the 'NAs' and narrow down the categories. Particularly for *CompanySize* I created *Nano, Small, Medium, and Large.*

3. **The Uninformed Statistician.**
   * Some column names did not match the questions and some questions did not have columns related to it in the dataset. WTF?
4. **User Error?**
   * In the survey it asks users what their salary is and if they inputted their answer in pay per week, month, or year. However, there was no column for the unit of measure specification. This would have been fine if they already converted the values to be uniform. But, they didn't. The majority of values in *Salary* were values like ```75000``` which obviously meant $75,000 per year. But then you'd run into ```5```. 5? 5 what? If that meant \$5000, then surely it could mean per month. That would make sense when I looked at the rest of that person's data. Well then what do you do with ```30000``` since 30K seems too low and 360K seems too high. 
   * So, I consulted Google and Google told me that the Average Computer Programmer Hourly Wage in the United States can range from **$15.84** and go up to **$54.74**. \$15 per hour is salary of \$27K, so I snipped the salaries that were less than that. 

> If you were doing this professionally, more research would be appropriate.

* What are the limitations of our talk? What we will be going over. What we won't be going over.
* Missing Data
* Dumb shit
* Null Values
* Making weird choices
* Making Assumptions
* Building a User Interface for Truth
* Talk about each factor that we decided on

### Data Mining/ Play with it

How do we calculate the coefficients AND what do they mean? 

- synonyms for coefficients
- synonyms for covariates=regressors=predictors=variables=independent variables = X
- Start with the basic y=mx+b two points scenario (what was taught in school)
- Then go over OLS (ordinary least squares) or SLR (simple linear regression)
- Then end with MLR (multiple linear regression) 
- Allude to how things can get even crazier (transformations, splines, higher-order terms, etc.)

### Make a Model 

Model selection and assessment procedure.

- What method we used to create a prediction model.

### Test / Confirm

Train / Test Split

Purpose => 

Dummy Variable Trap







### Do Something with it 

... and into Production

From what I can tell if you talk to the data science people "Into Production" basically means:

"I turned over my findings so that the other people can do stuff with it"



From a web development background getting something into production is simple. Git pull on your server, then direct your domain name to port 80.

What is production anyway?

## End really really well!!!!