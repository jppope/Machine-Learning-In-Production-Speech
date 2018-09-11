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

### 1. Get Data

* Stack Overflow 2017 ???? [link!]
* All the Variables

```R
  [1] "Respondent"                       "Professional"                    
  [3] "ProgramHobby"                     "Country"                         
  [5] "University"                       "EmploymentStatus"                
  [7] "FormalEducation"                  "MajorUndergrad"                  
  [9] "HomeRemote"                       "CompanySize"                     
 [11] "CompanyType"                      "YearsProgram"                    
 [13] "YearsCodedJob"                    "YearsCodedJobPast"               
 [15] "DeveloperType"                    "WebDeveloperType"                
 [17] "MobileDeveloperType"              "NonDeveloperType"                
 [19] "CareerSatisfaction"               "JobSatisfaction"                 
 [21] "ExCoderReturn"                    "ExCoderNotForMe"                 
 [23] "ExCoderBalance"                   "ExCoder10Years"                  
 [25] "ExCoderBelonged"                  "ExCoderSkills"                   
 [27] "ExCoderWillNotCode"               "ExCoderActive"                   
 [29] "PronounceGIF"                     "ProblemSolving"                  
 [31] "BuildingThings"                   "LearningNewTech"                 
 [33] "BoringDetails"                    "JobSecurity"                     
 [35] "DiversityImportant"               "AnnoyingUI"                      
 [37] "FriendsDevelopers"                "RightWrongWay"                   
 [39] "UnderstandComputers"              "SeriousWork"                     
 [41] "InvestTimeTools"                  "WorkPayCare"                     
 [43] "KinshipDevelopers"                "ChallengeMyself"                 
 [45] "CompetePeers"                     "ChangeWorld"                     
 [47] "JobSeekingStatus"                 "HoursPerWeek"                    
 [49] "LastNewJob"                       "AssessJobIndustry"               
 [51] "AssessJobRole"                    "AssessJobExp"                    
 [53] "AssessJobDept"                    "AssessJobTech"                   
 [55] "AssessJobProjects"                "AssessJobCompensation"           
 [57] "AssessJobOffice"                  "AssessJobCommute"                
 [59] "AssessJobRemote"                  "AssessJobLeaders"                
 [61] "AssessJobProfDevel"               "AssessJobDiversity"              
 [63] "AssessJobProduct"                 "AssessJobFinances"               
 [65] "ImportantBenefits"                "ClickyKeys"                      
 [67] "JobProfile"                       "ResumePrompted"                  
 [69] "LearnedHiring"                    "ImportantHiringAlgorithms"       
 [71] "ImportantHiringTechExp"           "ImportantHiringCommunication"    
 [73] "ImportantHiringOpenSource"        "ImportantHiringPMExp"            
 [75] "ImportantHiringCompanies"         "ImportantHiringTitles"           
 [77] "ImportantHiringEducation"         "ImportantHiringRep"              
 [79] "ImportantHiringGettingThingsDone" "Currency"                        
 [81] "Overpaid"                         "TabsSpaces"                      
 [83] "EducationImportant"               "EducationTypes"                  
 [85] "SelfTaughtTypes"                  "TimeAfterBootcamp"               
 [87] "CousinEducation"                  "WorkStart"                       
 [89] "HaveWorkedLanguage"               "WantWorkLanguage"                
 [91] "HaveWorkedFramework"              "WantWorkFramework"               
 [93] "HaveWorkedDatabase"               "WantWorkDatabase"                
 [95] "HaveWorkedPlatform"               "WantWorkPlatform"                
 [97] "IDE"                              "AuditoryEnvironment"             
 [99] "Methodology"                      "VersionControl"                  
[101] "CheckInCode"                      "ShipIt"                          
[103] "OtherPeoplesCode"                 "ProjectManagement"               
[105] "EnjoyDebugging"                   "InTheZone"                       
[107] "DifficultCommunication"           "CollaborateRemote"               
[109] "MetricAssess"                     "EquipmentSatisfiedMonitors"      
[111] "EquipmentSatisfiedCPU"            "EquipmentSatisfiedRAM"           
[113] "EquipmentSatisfiedStorage"        "EquipmentSatisfiedRW"            
[115] "InfluenceInternet"                "InfluenceWorkstation"            
[117] "InfluenceHardware"                "InfluenceServers"                
[119] "InfluenceTechStack"               "InfluenceDeptTech"               
[121] "InfluenceVizTools"                "InfluenceDatabase"               
[123] "InfluenceCloud"                   "InfluenceConsultants"            
[125] "InfluenceRecruitment"             "InfluenceCommunication"          
[127] "StackOverflowDescribes"           "StackOverflowSatisfaction"       
[129] "StackOverflowDevices"             "StackOverflowFoundAnswer"        
[131] "StackOverflowCopiedCode"          "StackOverflowJobListing"         
[133] "StackOverflowCompanyPage"         "StackOverflowJobSearch"          
[135] "StackOverflowNewQuestion"         "StackOverflowAnswer"             
[137] "StackOverflowMetaChat"            "StackOverflowAdsRelevant"        
[139] "StackOverflowAdsDistracting"      "StackOverflowModeration"         
[141] "StackOverflowCommunity"           "StackOverflowHelpful"            
[143] "StackOverflowBetter"              "StackOverflowWhatDo"             
[145] "StackOverflowMakeMoney"           "Gender"                          
[147] "HighestEducationParents"          "Race"                            
[149] "SurveyLong"                       "QuestionsInteresting"            
[151] "QuestionsConfusing"               "InterestedAnswers"               
[153] "Salary"                           "ExpectedSalary"  
```

This survey covered **many** different types of questions. Depending on your goal, you don't need to use information from **every** variable you obtain.


* How we created our subset. What difficult choices we needed to make (for 'pedagogical reasons' of course). 
* EDA to support our choices and make naive speculations. 

### Clean up Data / Organize

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