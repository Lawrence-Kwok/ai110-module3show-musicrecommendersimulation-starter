# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MusicMuse 1.0**
---

## 2. Intended Use  

The intended use of the recommendation system is to provide songs for the end
users whose profiles or preferences are put into the system. Currently it  features 3 profiles (high pop energy, chill lofi, and deep  intense rock) in  which it compares against the songs in the database.This is intended for  classroom exploration, but future subsequent revisions  or further enhancements may cater the end product towards actual usage once
fleshed out.  

## 3. How the Model Works  

The scoring approach is simple in utilizing 4 key criteria:
* genre 
* mood
* energy
* acousticness

Other criteria that is present in the songs csv file is not currently used.  
The model itself assigns a specific weight value to each criteria multiplied 
by the binary or gradient scaled value of each. In other words if its present 
it would recieve x number of points for genre or mood, whereas it would    
recieve a percentage of points dependent on the closesness of energy and    
acousticness. Theres not much changes from the starter logic other than using
a 100 pt grading scale rather than assign arbitrary 1 to 2 pts per category.

## 4. Data  

Song catalog consists of 20 synthetic song profiles, of which pop, lofi, rock,
jazz, and other categories are present as well as moods such as happy, chill, intense, relaxed, or moody being present. Approximately 10 songs were  present  with the project starter files, with 10 additional synthetic song profiles g enerated. In terms of missing parts of musical taste, theres a lack of accounting for length, instruments, and loudness, etc.

## 5. Strengths  

System works really well for finding songs that match the genre and/or mood well. It captures near perfect match song profiles well for the most part, with the top 2 - 3 songs being consistent with the users intended  taste  profiles when examining results. 

## 6. Limitations and Bias 

System currently faces the following biases as follows:
1. Fixed weighing is heavily biased towards genre and mood accounting
for two-thirds of the entire scoring system.
2. Exact match for mood and genre criteria which discounts songs that 
might be a related genre or similar mood due to lack of relational scoring
to adjust for non-exact matches.
3. No current diversity mechanism, which can cause one artists songs to appear
more frequently.
4. Gradient scoring mechanisms carry the least amount of weight despite being
more fair in terms of showing actual relation. 
5. Valence, danceability, and tempo are parameters that aren't currently used 
in this iteration despite being present.

## 7. Evaluation  

The recommender doesn't perform as expected precisely; there were three user  profiles tested (High Energy Pop, Chill Lofi, and Deep Intense Rock). When  looking at the recommendation outputs I looked for the genre then mood fits, then to the energy and acousticness. While for the most part the top 2-3 songs
for each category were as expected, there was a huge deviation in the later results where energy and acousticness took precedence. Tests were run to  lower the weight or remove the genre and mood categories, which greatly  affected the High Energy Pop profile; showing the huge impact of their weight in the system which is very binary in terms of scoring. 

## 8. Future Work  

In the future, gradient scaling needs to be considered for all scoring categories for more robust and effective results. Currently its an all or 
nothing scoring system, which is good for near perfect matches but heavily
disadvantages relatable songs that the user may like in favor of songs that
score better on the gradient scale categories. In addition adding more criteria would help better refine the results to be more specified as with
all queries, but hadn't been considered outside of the original starting categories, such as length of song, diversity of artists, etc.

## 9. Personal Reflection  

Working through the recommender system, I learned alot about how its an 
evaluation system that is aimed at finding the best statistical matches for   
the users inputted profile or preferences. I find it particularly interesting
that the way you assign weights or add/remove the parameters can greatly 
enhance or destroy the accuracy or expected results of the outputs. This  
makes me think back to how llms work, where they operate on a similar  
principle with next token generation and evaluating the output generation 
via a weighted model as well. In terms of thinking about music recommendation
applications, its both fascinating and scary how much user data they're  collecting in order to facilitate the personalization.