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
* If you recieve an email about viagra discounts... it's probably spam.



### Classification

Example: 

* Naive Bayes:



| Beer   | Dark | IBUs > 100 | ABV > 5.2 | Total Beers |
| ------ | ---- | ---------- | --------- | ----------- |
| IPA    | 0    | 400        | 250       | 500         |
| Stout  | 400  | 0          | 150       | 300         |
| Other  | 100  | 100        | 100       | 200         |
| Totals | 500  | 500        | 500       | 1000        |

So from the table what do we already know?

- 50% of the Beers are IPAs
- 30% are Stouts
- 20% are other Beers

Based on our training set we can also say the following:

Beer #1 => Light, Hoppy, 5.4% (1, 0.8, 0.5, 0.5) =  



### Clustering algorithms

Example:

* The Research Triangle in North Carolina. Given a lat/ long of a student address guess which University they go to. 



### Reinforcement learning (Rewards good behavior)



### ANNs and CNNs (Going deep)








## Data Science

### Hello Everyone.

This is me. My twitter handle and website if you're interested.

Has anyone ever been asked...

### What is a data scientist? 

* I have. plenty. Ever since I started my Masters program. I'm first gen in my family and to them statistician = actuary. 
* But, it's a whole new thing! The "sexiest job of the 21st century" they call it. 
* I found this on Google and sent this to my whole family.  It makes me look cool. 
* So now my standard reply at a cocktail party is : "Imagine if you took the three hardest subjects in the world: Math, Computer Science, and Statistics." That's what I do.

(Source: https://en.wikibooks.org/wiki/Data_Science)

### About Sacha

- Here's me in three simple bulletpoints. My math and stats career started just after high school.
- I could have gone to Berkeley, UCLA, or UC San Diego, but I chose UCI for reasons that made sense at the time. 
- After changing my major 6 times or so, I then pursued and completed a Pure Math degree with a minor in statistcs. 
- After graduation, I ran a few tutoring centers for Mathnasium Corporation for about 2 years. 
- Fate dragged me back to UCI. Where I am now to complete my Masters degree this coming Spring in Stats. 
- Some irrelevant, but fun facts about me...I love teaching, I can sing, and my recent obsessions are gardening, horticulture, & insects.
- Anyhow, we've been doing IPAs and APIs since August 2015. We love it, and we're really glad you're here after our small hiatus since April. So, thank you. 

### Linear Regression Explanation

* I don't want to scare you, but there are some stats concepts that I'll be going over in my part of the talk. These are things you **should** **understand** or at least be **aware** of.
* To me, ML is Statistics on steriods. 
* Don't tell us we didn't warn you. 

#### Terminology

* In math and stats there are always synonyms for the same thing. Not sure why. It's a pain. But, I want you to be aware of the synonyms for the X variables. BC I might use any of these during this talk. 
* Predictors
* Regressors
* Covariates
* Explanatory vars
* Independent vars
* X vars 

#### Line

* Let's start easy. Y=mx + b.  
* You can do this by hand no problem.
* Just a rise over run situation.

#### SLR

* But, that's unrealistic. What happens when you have more than 2 observations? What happens when you have a sample of size n?
  * Error term is needed! We have noise! We need to make assumptions. We also need to make sure those assumptions are justifiable. (Confession: I totally did not do model diagnostics for error assumptions in this project; Professor Dan would be shaking his head right about now.)
* Our slope still looks like a ratio; not quite Rise over Run. We take the x's and subtract them from their mean. That produces what is called mean-centered terms. We do the same for the y's and then multiply them both and add them up. This is called the covariance between X and Y. Then, we do the same for the denominator but just with the x's. 
* And finding the intercept is very similar to previous slide except with averages instead.

#### MLR

* What happens when you have more than one predictor variable? 
* We need linear algebra! Finding the regression coefficients (the 'b's) is an iterative process otherwise. Linear algebtra makes it easier. 
* This is the model we will be fitting. We will not go over transformations, splines, or Generalized Linear Models (GLMs) like Logistic Regression.
* Beta is now a vector that contains all the regression coefficients. 
* The formula is complex but at least it still involves the X and Y values. 
* Another important thing to note is $X^TX$ must be invertible. Meaning, you can't have any dependent columns in $X$ matrix. Meaning you can have dependent variables. An easy example would be one column that asks for temperature in Fahernheit and then another column with that temperature in Celcius. These are directly dependent. 
* I can go further with dependent predictors but I won't now bc of time.

(3D Plot Source: https://se.mathworks.com/help/stats/regress.html)

### The Project

* So, let's talk about the project. 
* I was surprised to find that the majority of a Machine Learning included a lot of what I have been studying this past year. It's a lot of Statistics, actually.   

### General Steps 

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

- EDA Plots
- End with what subset of Data we used.

#### Salary Histogram

You saw this before in hot pink. I wanted to play with these a little and separate them by Gender. We didn't use Gender in our Prediction Model, but I thought it was interesting to show. Male is in purple (as you know the majority of developers are male), and non-male is in orange (this includes what was labeled as Females, Transgender, non-conforming, or Other).

* The sampling distribution of Salary look fairly similar between the groups. [Note: our min salary is 27K]
* When working with groups that are unbalanced, a histogram can be a little unclear or misleading. Density graphs are much better.

#### Salary Density

* Better! We can see that the range is similar, but the averages may be slightly different. See how non-males have a higher density in the lower ranges of Salary and males have a higher density in the higher ranges of Salary?

* Well this is only a marginal view. I was suspicious. Maybe there were confounding variables that made this the case.
* Can anyone think of a reason for this?

#### Years of Coding! (densities)

* Years of coding is a confounding variable. 
* A larger proportion of non-males are less young in the coding world! 
* A larger proportion of those experienced with coding are males.
* The same is true with Years Coded in general and Years Coded professionally. 
* Give it time. I'm sure that the salary density plot will converge to be similar. 

#### Mean Plots!

* You may be less experienced with mean plots
* They are very popular in time-series analysis, but I liked using it here because if we just had a scatterplot, it would be a little difficult to see the upward trend.
* A mean plot is basically a scatterplot between X and Y with a smooth curve running through the averages of every X level. You're won't always see straight lines.
* What's not surprising is the more you code in general the higher salary you have.
* What is INTERESTING is the orange curve. 
* It looks like on average non-males have higher salaries early in their coding experience  than males! And then the reverse seems true after around 12 years of experience.
* However....
* Sometimes, you need to consider sample size differences across the different X levels. Sample size differences can show things like this.
* Without further investigation, making claims based on this single mean plot can be DANGEROUS. 
* This second plot shows the power of small sample sizes a little better.
* You see more orange dots pre-10 years but post-10 years the sample sizes are small AND most the dots have lower salaries. Our density plots showed us why that was. 

#### Boxplot

* This one is a little obvious, but I at least wanted to give you an example of a boxplot with categorical variables. 
* I also included the sample sizes of each group. 
* I think it's fair to say that average salary and distribution seems the same between those who graduated with a bachelors vs those who had lower formal education. 



### Model Selection & Assessment

#### General Steps

- AIC, BIC, & Cross-Validation are estimates of EPE (expected prediction error). We want to minimize the EPE. So, we want these to be small.
- RSS is not strong for this because it necessarily decreases. The more predictors you have, the better the fit. You would think that's what you want, but you don't ultimately want to decrease prediction error of your sample. You want to minimize prediction error for new observations outside of your sample. 
- More predictors means overfitting. We do not want overfitting.

### Test / Confirm

Note About:  Train / Test Split
Note About: Dummy Variable Trap

### Final Model



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





## Let's get practical 

### What does a basic web application deployment look like:

1) Data Model

2) Some sort of an interface

3) A User. 

![Basic](/Users/Pope/stormcloud/github/mlSpeech/slides/images/basic.png)