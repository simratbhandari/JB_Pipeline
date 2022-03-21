**What are the risks involved in building such a pipeline?**
- Since the dataframe was converted into sql, there is a relatively high chance of sql injection attacks. Additionally since we have transfer from the api to relational storage, there is a need to constantly monitor the pipeline for speed and efficiency, particularly as the size of data grows larger. When you try to input a large number of tweets, it takes a long time to process the data because the message comes in from the compiler saying that the program runs beyond the normal time limit. We should also be wary of hitting the API limits which is purely dependent on Twitter. When that rate limit is reached, running the code would send a message of 'Maximum rate limit reached. Program will sleep now.' So we would need to have a restart option everytime this rate limit is reached so the code automatically restarts. Also, try to determine all possible edgecases: for example, in order to remove duplicate tweets, we have to remove retweets as well, but if someone writes 'RT' in the beginning without actually retweeting, it could give a false positive duplicate tweet, so we need to make sure that all edge cases are resolved.
  
**How would you roll out the pipeline going from proof-of-concept to a production-ready solution?**
- Firstly, figure out the problem statement, the requirements and the deliverables of the project. 
- Secondly, do research on all the viable API and third party libraries that can be used (Data Collection and Preparation).
- Next, check to see if the workflow for the pipeline is properly set up and anticipate the possible problems and edge cases that can come up.
- Write a design document to make sure all the above are noted as well as an outline of the libraries that could be used.
- Start writing the code and clean up the code wherever possible
- Next thoroughly test the code, by writing test cases and test it on a larger sample of data to see more edge cases.
- Check to see if the code is scalable on different samples of data.
- Collaborate with the appropriate teams and customers to cover all your bases.
- Finally deploy the code to prod whenever comfortable to make it a production- ready solution.

**What would a production-ready solution entail that a POC wouldn't?**
- A proof of concept is work that is focused on determining whether an idea can be turned into a reality. A proof of concept is meant to determine and verify whether an idea can turn into a project that can make it through to deployment in production. A production ready solution, on the other hand is one that is capable of meeting the demands of the user. A POC wouldn't entail scalability and the extensive testing that a production- ready solution would entail. Scalability entails dertermining if the idea works on different sample sets and testign includes having sample test cases that thoroughly check each aspect of the code and check to see if the idea is error- free and works for any type of case that the programmer and customer can think off. Another aspect is error handling which a production- ready solution would entail that a POC wouldn't. We need to check for different edge cases after the code is written to thoroughly validate the code.

**What is the level of effort required to deliver each phase of the solution?**
- From proof of concept to production- ready, there are a couple of steps that need to be followed:
   1. Initial preparation for the project: which includes extensive research and preparation into third party libraries and different API's: this would be proportional to the scale of the project: for this particular project, it would take some research effort for 1-2 hours to see which third party library I would use and how to connect to which particular database.
   2. Design document to highlight all the guidelines: this would be proportional to the guidelines of the project (scale of the project: this would involve all the guardrails of the project, the initial limitations, edgecases etc), so for this particular project, would take 1-2 hours.
   3. Starting the coding process: writing the initial outline of the code, along with the classes and functions to be used to get a brief idea. This would also be proportional to the size of the project, so for this particular project, it took me around 2-3 hours to brainstorm and write out the outline along with all the imports of the appropriate library functions.
   4. Testing: testing is a major and important phase to reach a production- ready solution. One should check for additional edge cases to make the code more robust and efficient, as well as scalability of the program with different sizes of sample data. Testing extensively is a skill which requires a considerable level of effort and time depending on the size of your project as well as how much initial testing was done (initial print statements). For this particular project, it took me around 4-5 hours to test out the code, to print out certain lines, to test out the code with different sample sizes of tweets, to determine edge cases that could be used and tested for. It also took some time to filter out the tweets related to music and what keywords could be used potentially to distinguish the tweets related to music.
   5. Collaboration: this last phase goes hand in hand with testing. After the code is tested for and complete, you can collaborate with other teams to validate your code and the process further. This would be a phase more appropriate in a business setting and would be the last phase before deploying into production. This shouldn't take more than 1-2 hours of effort depending on which team you're going to, the size of the project.
    
**What is your estimated timeline for delivery for a production-ready solution?**
- It depends on the scale of the project, but if it's a project on a bigger scale, it would take a couple of months (1-2 months) to go from PoC to a production ready solution because of going through all the phases, with the longest phase being the testing process which would take the most amount of time and effort. It also depends on the scalability of the project with the amount of data that is being inputted in. For this particular project, if I wanted to make more enhancements, like making my classifier for the tweets better, by analyzing the data we receive from each tweet and see how to classify the tweets to filter our music better. This would involve filtering out based on more keywords as well as matching the keyword ('Justin Bieber' with different cases and spaces) with music keywords and make the filtering process better and more robust. With more holistic testing and validation, this project could also take about a month from the initial stages of the project to a production- ready solution. 

 
