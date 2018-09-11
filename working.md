# Machine Learning in Production

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

[We're going to do the drinking feedback version of hands...]

### Goal of this Speech

> Expose you to a basic Machine Learning Production process, and then show a "deployed" version of the data model

### Sacha and I will be Tag teaming this one...

She's going to cover the data science portion and like all good husband I'm going to do all the hard work. Just kidding.

### About Me

Find me: @jppope and jonpauluritis.com



### Machine Learning Overview
![Machine Learning](/Users/jonpauluritis/prototype/Machine-Learing-In-Production-Speech/slides/images/AI.png)




#### My perspective...

> Machine learning is using statistics and data to replace the need for explicit programming. 

or put another way... 

>  "Using math to do the hard parts of your job."

### Why does it matter? 

This may be a little bit of an exaduration... if you don't learn this stuff you are probably going to be out of a job.



##Machine learning has a lot of subtopics:

#### Supervised Learning versus Unsupervised Learning 

![Supervised](/Users/jonpauluritis/prototype/Machine-Learing-In-Production-Speech/slides/images/supervisedUnsupervised.jpg)



### Linear Regression 



Examples:

*  Salary & Years Experience
* Amount spent on gas & distance travelled on a road Trip

### Lojistic Regression

![example](/Users/jonpauluritis/prototype/Machine-Learing-In-Production-Speech/slides/images/LogisticRegression.png)

Example:

* Think of Shaquille Oneil, He's going to make all of his shots within 2-3 feet of the basket, He's going to miss pretty much every 3 pointer
* If you recieve an email about viagra discounts... its probably spam.



### Classification



* Clustering algorithms (there's a bunch of groups find the groups)
* Reinforcement learning (Rewards good behavior)
* Artificial Neural Networks (Making ML harder by explaining with graphs)
* Convolutional Neural Networks (In case explaining ANNs weren't hard enough)




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

1. As a developer seeking employment, how do I increase my salary? What factors negatively/positively impact my salary? 
2. To create a prediction model that will calculate an 'appropriate' salary given a new set of specific covariate values (information), which is expected to come from an employer or job-seeking developer.

### 2. Get Data

* [Stack Overflow 2018](https://insights.stackoverflow.com/survey/2018/)
* Insert all the Variables.

This survey covered **many** different types of questions. Depending on your goal, you don't need to use information from **every** variable you obtain.


* How we created our subset. For 'pedagogical reasons,' we concentrated our analysis on US full-time developers. 
* EDA to support our choices and make naive speculations. 

  * For example, I initially kept gender and race because I wanted to see if they attributed to salary. I was happy to find that there were no significant differences in the average salary when considering various genders and races.
  * **I want to make something clear:** This data can answer questions about employee salary differences, but we cannot answer questions about the likelihood of obtaining a developer job based on gender, race, or any other variables. 

### Clean up Data / Organize

#### Challenges

1. **Some questions allowed you to pick more than one category that you fall under.**

   Example: What kind of developer do you identify as? (*DeveloperType*)

   Here are all the categories that respondent #2 thought described him best.

```R
> StackOverFlow_Data$DeveloperType[2]
[1] "Web developer; Mobile developer; Embedded applications/devices developer; Machine learning specialist; Data scientist; Graphic designer; Desktop applications developer"
```

	You can deal with this many ways, but what I did was create dummy variables for each category. So, there was one column per selection and if the user classified themselves as a web developer, then the value would be 1 and if not the value would be 0. There was about 20 unique categories. But, for this presentation I only created the top 11 categories.

2. **Some questions had many levels (even though you were only able to choose one) + different forms of 'NAs'.**

   Example: How many employees does the company you work for have? (*CompanySize*)

   You can also deal with this many ways, but what I did was eliminate the 'NAs' and narrow down the categories. Particularly for *CompanySize* I created *Nano, Small, Medium, and Large.*

3. **The Uninformed Statistician.**

   * Some column names did not match the questions and some questions did not have columns related to it in the dataset. WTF?
4. **User Error?**
   * In the survey it asks users what their salary is and if they inputted their answer in pay per hour, week, month, or year. However, there was no column for the unit of measure specification. This would have been fine if they already converted the values to be uniform. But, they didn't. The majority of values in *Salary* were values like ```75000``` which obviously meant $75,000 per year. But then you'd run into ```5```. 5? 5 what? If that meant \$5000, then surely it could mean per month. That would make sense when I looked at the rest of that person's data. Well then what do you do with ```30000``` since 30K seems too low and 360K seems too high. 
   * So, I consulted Google and Google told me that the Average Computer Programmer Hourly Wage in the United States can range from **$15.84** and go up to **$54.74**. \$15 per hour is salary of \$27K, so I snipped the salaries that were less than that. 

> If you were doing this professionally, more research would be appropriate.

#### Cleaning Summary

* Missing Data
* Dumb shit
* Null Values ('NA', 'I don't know', 'I prefer not to answer')
* Making weird choices
* Making Assumptions (x probably isn't related to y)


### Data Mining/ Play with it

- 

### Make a Model 

Model selection and assessment procedure.

- What method we used to create a prediction model.

How do we calculate the coefficients AND what do they mean? 

- synonyms for coefficients
- synonyms for covariates=regressors=predictors=variables=independent variables = X
- Start with the basic y=mx+b two points scenario (what was taught in school)
- Then go over OLS (ordinary least squares) or SLR (simple linear regression)
- Then end with MLR (multiple linear regression) 
- Allude to how things can get even crazier (transformations, splines, higher-order terms, etc.)

### Test / Confirm


Note About:  Train / Test Split
Note About: Dummy Variable Trap



---







###So The title of this speech was "Machine Learning in Production"

Right now we have a Machine Learning Model... So how does one "put a model in production"? 

A year ago I went looking for this answer... and I got really confused though... because the answer is not a straight forward thing.



### Here's an example of a guy trying to figure this out:

What are the best libraries / frameworks out there for productionizing ML?

Link

![Reddit Image](/Users/Pope/stormcloud/github/mlSpeech/slides/images/redditQuestions.png)

Answers: 

- Caffe2 (Deep learning framework)
- Tensor Flow (ML framework)
- ONNX (Open Neural Network Exchange ... Format)
- NVIDIA TensorRT if you are using GPU (Hardware Manufacturers interface?)
- "Docker Flask Redis Tensorflow" (Containers, micro framework, key-value store, ML framework)
- Scikit-learn (Framework for doing simple ML)



Or sometimes you get diagrams like this: 

![complex](/Users/Pope/stormcloud/github/mlSpeech/slides/images/dataLake.png)

### If you stop and think about why there isn't a REALLY simple answer... 

With a web app... you are a deploying a piece of software or the product. 

Take this thing here and put it over there so people can use it



That is not the case for machine learning though... 



What are people primarily using Machine Learning for Today

- Search (Google, Bing)
- Recommendation Alogrithms (Netflix, Amazon) 
- Identifying Credit Card fraud (PayPal, Major Banks)
- Financial Trading. (Renaissance Capital)
- Reinforcement Learning... Multiarmed bandit problem for ads (Advertising Companies)
- Political Manipulation (Cambridge Analytica)

Where is it going?

- Driverless cars (Tesla, Waymo, Uber, Cruise, Drive.ai, etc)
- Robotics (Boston dynamics)
- Healthcare (IBM Watson)
- Celebrity Porn (Deep Fakes)



### Top Level view. 

Andrew Ng Talks talked about this in his "state of artificial intelligence" speech

- Strategic data acquisition 
- Create a interface/product from data
- Users use interface/ product and generate data

This creates a cycle

![data cycle](/Users/Pope/stormcloud/github/mlSpeech/slides/images/dataCycle.png)



### Takeaway: This whole cycle is machine learning in production...

(key difference between a software application and an AI / Machine Learning)





## Lets get practical 

### What does a basic web application deployment look like:

1) Data Model

2) Some sort of an interface

3) A User. 

![Basic](/Users/Pope/stormcloud/github/mlSpeech/slides/images/basic.png)