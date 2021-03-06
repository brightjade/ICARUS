# Final Report

## Quality Arguments

Our interface is designed to support Human-AI interaction on multiple levels.

The first level is direct interaction with the model. On this level, there is our killer feature “Refined Search”. Here, we allow to users to fine-tune the search results by recommending papers related to the papers the user has “added” to their list of citations, by using the average of the added papers as the search query. This proved to improve the relevance of search results with input vector, compared to the initial search results. The feature was _“useful and novel”_ according to P4.

On the second level, we give the user multiple ways to interact with the resulting data to improve their experience. One major part of our interface in this level is the 2D scatter plot, and another is the list view. While the list view provides data and interactions in a familiar but inefficient layout, the graph complements this by putting the data points into context, so that closer dots represent similar papers. Specifically, the 2D scatter plot has two roles:
1) Provides additional data for each recommendation that user can leverage when selecting the papers to add.

With the graph, users can intuitively see how close a paper is to the input vector, to added papers, and to papers the user has marked irrelevant. Users can see whether the papers they have added are skewed and explore papers on the other end or refine their search to get more related papers. 

2) Visual aid for explaining the effect of each interaction that our UI supports.

Every interaction (add, irrelevant, clear results, refined search, even next/previous page) results in some kind of change in the graph as well. This lets the user explore our interface and understand each of these features interactively. .

**Before**
![before](refinedSearchBefore.png)
**After**
![after](refinedSearchAfter.png)
For instance, for the "Refined Search” feature, the user can immediately see that the light blue point shifts closer to the green points and know that the feature gives them papers related to added papers intuitively without further guidance.
We found users actively using the scatter plot, and P2 complimented how it interacts with the list and paper views.


The third and last level is more nuanced support, in which we support interaction with AI by making our system more intuitive and easy to understand. Since our system mediates users’ interaction with AI, there are two cognitive layers and it is important for us to minimize the cognitive load of our interface.
For this, the interface is carefully designed to be as intuitive as possible. Each feature is carefully placed in the best location in the UI, so that each button is close to the elements they directly affect.

**Tooltip**
![tooltip](tooltip.png)
We have also included explanations for the UI and our supported interactions. For instance, the "Start Over" "Clear Results" "Add" "Irrelevant" "Refined Search" buttons all have tooltips when you hover on them, that explain what happens when each button is clicked.

Overall, ICARUS was praised for its intuitive design.

## Evaluation

We evaluated ICARUS by running a user study with five graduate students in a lab (4 Master’s and 1 Ph.D candidate) who have experience of writing research paper for at least one year. After giving a short instruction of how ICARUS works, we asked them to explore ICARUS freely and give feedback and general impressions about it. For the post survey, we asked three questions: Q1) Illustrate general impression, pros/cons, feed backs, further improvements of ICARUS, Q2) What kind of recommendation did you feel helpful?, and Q3) If ICARUS is plugged in overleaf or any writing tool you are using, would you use it? It took an average of thirty minutes for running a user study.

For evaluation, we first conducted NASA-TLX which finds the overall demand when using an interface. Although there were five participants, we tried to find out if ICARUS imposes high mental demand or frustration level. It turned out that the average scores of mental demand and the frustration level were under 2, indicating that ICARUS is fairly easy and straightforward to use. 

We report the pros and cons that participants pointed out in the post survey as the qualitative analysis. For the pros, all participants replied that ICARUS is easy to use and has a straightforward design. One participant replied that he liked how ICARUS integrated the 2D visualization view (P2). Also, P4 noted that refined search was useful and novel. On the other side of the coin, two participants (P1, P5) pointed out the failure cases of recommendations were somehow disappointing. “At least, I expect that the titles include the query” (P1). Additionally, three participants (P2, P3, P4) stressed that the recommendation view should have included the metadata such as conference, title, and year. Lastly, four participants replied that they will use ICARUS if it is plugged in the text editor they are using such as Overleaf. 

We also received further suggestions to improve ICARUS. P1 noted that the connectivity between papers is important when finding the paper. “Citation information between papers should be considered to express the connectivity between the papers.” Another fruitful suggestion from P1 was that weighting the attention of words could improve the recommendation quality. “Giving more weights to the query keywords (e.g. interactive segmentation) is needed to find more relevant papers.” This is a reasonable feedback since most of the state-of-the-art language models utilize attention mechanisms in their model. We believe including such feature would enhance the recommendation quality of ICARUS. 

What we learned from evaluating ICARUS is that users actively used 2D projection view when exploring papers. Also, users considered the metadata such as conference or year important when choosing the recommendation. Additionally, we were delighted that users said that the refining feature actually improved the quality of the recommendation. Refining the query via human interaction is the collaboration of the language model and the user’s taste. The fact that users liked this feature demonstrates that we built a system which actively utilizes the collaboration of human and AI. 

## Discussion

We designed ICARUS such that it supports a number of human-AI interactions in an effective and intuitive manner; however, we believe that it can be much improved to make the user experience better. First, ICARUS is an AI-advised decision-making system where the user has a flexible control over AI. The user can refine the results by adding and blacklisting recommended papers, as well as performing the “Refined Search” feature. Nevertheless, we realize that grasping the mental model of our system is difficult because random papers are very often recommended. As for the interpretability of the model, we had thought that displaying the cosine similarity score could explain the model decisions, but it lacked demonstrating the process of the model making decisions. To enhance the interpretability, we could perhaps highlight specific parts of the paper abstract that contributed the most on the similarity score. Alternatively, we could create a more complex yet interpretable scoring function than cosine similarity. A cosine similarity score ranks papers based on semantic similarity, but this might not be what the user actually wants. We could utilize additional data, such as the number of connected citations, user preferences, or even a past session history of the user, to build a more comprehensive and explainable recommendation engine.

In terms of metrics, we had no methods of evaluating the model performance quantitatively. Paper recommendation does not really have a clear answer, as the standards for “good” recommendation differ subjectively. We could have done an A/B testing over users to build an optimized recommendation algorithm, but the amount of time and resources would be beyond the scope of a class project. In such a case, automatic evaluation metrics such as Mean Average Precision at K (MAP@K), one of the metrics for evaluating recommendation systems, could be considered.

As for the fairness, ethics, and privacy issues, we believe that ICARUS does not cause any serious problem. It is perfectly fair in that the papers are recommended solely based on abstracts and not biased in any way, since author names, university/corporate names, or any other metadata that could hint at the identities of the papers were not given at all. However, we cannot be sure of this, as we had not run any test to check this. Moreover, such a perfectly unbiased decision-making system might not be wanted by the users because according to one of the comments from the user study, users might actually want to see popular papers or papers from well-known authors/companies first. We could perhaps add a filtering feature in which the users could select.

Lastly, we believe that the 2-D scatterplot was simple yet clear enough to visualize well of the embedding space of the papers. But as opposed to our initial belief, the cartesian distance did not reflect the actual similarity score. Therefore, instead of visualizing the distance in the cartesian plane, we could increase the size of scatter dots by their similarity score and create an interactive graph with the dots.


## Individual Reflection

### Seokhun Jeong

I intentionally did the project with people I didn't know, because as an AI novice, I wanted to interact with people who had expertise in AI and learn more about AI. Initially, I felt that we had very different thought processes - for instance, while we were preparing for the pitch Jungsoo and Minseok mainly focused on the model and performance while I valued the problem statement, storyline and interaction. This was actually very natural, considering how research in each field is conducted, but I had to be the one to keep giving ideas about improving the storyline and interactions. However, during the course of the project our goals started to align a lot better. Towards the final presentation, I found Jungsoo and Minseok caring a lot more about interaction and the overall storyline, and prepare the final presentation quite thoroughly while I worked on the final touches of the interface. While I can’t say I’m the one to thank, I feel we all learned something through interacting with people from other areas.

Regarding implementation, I thought the teamwork was near perfect. We all had different experience and expertise in implementation, and we built our interface by doing rapid iterations to quickly build a basic interface and continue improving it. Jungsoo quickly developed the base model so that we could start designing the interactions. I bootstrapped the front-end and Minseok connected the model to an API and to the front-end chart component. With this connection in place, our rapid iteration processes were extremely efficient: I mainly improved interactions and explanations, fixed issues and improved the overall user experience, and Jungsoo improved the model. Minseok acted as the glue: he was skilled in both front-end and AI implementation so he could work with me in the front-end and also implement the ‘refined search’ feature that required work in both the model and the front-end. Overall, I really enjoyed working with Minseok and Jungsoo and was extremely satisfied with the final outcome.

The only downside in our teamwork during implementation was that since work was divided so naturally and efficiently, and we all had our hands full with our work, we didn’t have the time to learn or thoroughly understand each other’s work. I can’t really say I succeeded to meet my initial goal of learning more about AI implementation during the project. 

However, through our project I learned that there are problems that interaction alone cannot solve and requires other types of models or higher performance. While I think the interactions that we designed were quite useful and could make up for parts where the model wasn’t performant enough, our user study showed that there were still too many recommendations that felt irrelevant. 

### Jungsoo Lee

I was lucky to work with my wonderful teammates who had strong coding/communication skills. Minseok was at the core of our work who integrated the front-end and back-end of ICARUS. Seokhun had strong coding skills at building the front-end of ICARUS and gave various suggestions for the views in ICARUS. I deployed the pretrained language models in order to extract the features from abstracts and used them for 2D visualization. I really liked how my teammates compensated the parts that I could think while we had discussions. For example, I tend to think about the model implementation part when conceiving a new feature. However, Seokhun and Minseok point out the impacts on the front-end side which I could never think of. Also, we all had different abilities, so we compensated each other in the coding part too. One thing that could have been better is that we only discussed online which somehow limited our discussion. Though, it was a great experience to work with the two members.

Through the course, I learned that human interaction is more complicated than I thought. Since I have a strong background at AI, I normally think about the test accuracy or any kind of performance that we can measure for a model. However, during the course, I had to think how humans react to a certain feature which was far more complicated than I expected and it opened my perspectives. I will take this as the cornerstone and think about various aspects when building a model including the human’s perspective.

### Minseok Choi

Personally, I had one of the best team experiences with our team because everyone was good at different things yet shared the same picture of the final product. Seokhun was an expert at handling the frontend with React, bootstrapping with Nextjs and managing component states with MobX (which I completely had no idea and learned another level of React programming). Jungsoo had an experience with building a platform in the HCI field, so he knew well of the user needs for the backend AI model and understood how the user studies and interviews proceed. Finally, I had an experience with deploying a React-Flask application from scratch, so it was very comfortable combining the best of the two teammates. One thing we could have done better, however, is planning the AI design process more effectively. Although the project put a heavy emphasis on the human-AI interactions, we failed to think through how much time and effort would be required for implementing the interactions. Therefore, most of the workload was focused on the frontend before each deadline, so I, who knew React, communicated with Seokhun consistently and helped implementing React components. Moreover, Jungsoo finished building our AI model early, so he helped making slides and report, as well as conducting the user studies. Due to everyone’s efforts, we were able to pull through, but for the next time, we would need a much more careful planning before designing our human-AI interactive application.

Through designing a human-AI application as a team, I learned to think in a user-centered perspective. Before implementing each component or interaction, I would think twice whether the user would find it convenient or unintuitive. Furthermore, I did not consider the explainability or interpretability of the AI model as important, but putting myself in their shoes, I realized that the individual AI performance is not everything and that demonstrating the reason for the AI decisions is crucial. It would not only help building the mental model of AI, but it would also assist in the human-AI team collaboration performance. Lastly, by developing a web-based platform, I felt firsthand that the fast inference speed is really important for good user experience. I learned to appreciate lightweight models, especially in class projects, and would think more about the computation speed and resources in my future research and beyond.

## YouTube URL

- <https://youtu.be/oPSjkUIt2ww>
