**What are the risks involved in building such a pipeline?**
- Since the dataframe was converted into sql, there is a relatively high level of sql injection. Additionally, since we have transfer from the api to relational storage, 
  there is need to constantly monitor the pipeline for speed and efficiency, particularly as the size of data grows larger. When you try to input a large number of 
  tweets, it takes a long time to process the data because the message comes in from the compiler saying that the program runs beyond the normal time limit.
  
**
 How would you roll out the pipeline going from proof-of-concept to a production-ready solution?**
**- Firstly, figure out the problem statement, the requirements and the deliverable of the project.
    Secondly, do research on all the viable API and third party libraries that can be used.
    Once we have the tools, we can start**
