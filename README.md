# Recipe_Recommender
A Recipe Recommender to encourage one to put together meals based of off the ingredients at one’s disposal.
<img width="1957" alt="CDSAML" src="https://github.com/UtkarshBagaria/Recipe_Recommender/assets/79400700/70e5a914-20e6-4846-8df3-ab98d2afd0c3">
The system works by asking the user to provide all their available ingredients and preferences as input. Based on these inputs provided by the user, several recipe recommendations are provided.
Several technologies for pre-processing and data collection were used like automation softwares and the pandas library in python. 
Several strategies like tf-idf, weighing parameters were used to determine weights and rankings of recommendations.
The data is converted to a knowledge graph in Neo4j. Output is first filtered based of off the input and then ranked using our novel method.
### An example to show the working of the system:
#### Input
![Screenshot 2023-08-04 202324](https://github.com/UtkarshBagaria/Recipe_Recommender/assets/79400700/6335637b-8024-4ddc-be8b-1cd585759cdd)
#### Output Snippet
![Screenshot 2023-08-04 202440](https://github.com/UtkarshBagaria/Recipe_Recommender/assets/79400700/7a3909b1-4673-474b-a533-af77bfbe654f)


