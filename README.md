# 🎵 Music Recommender Simulation

## Project Summary

The Music Recommender project intends to create a system that scores songs
against a given user profile and recommend songs that matches the user  
profile via a scoring system of criteria. The recommender gets near exact 
matches well but falls in accuracy as the songs start to differ from the user 
profiles. This mirrors real world AI recommenders that are supposedly fine 
tuned to meet their use case but sometimes theres blind or missing factors
that could bias the results. 

## How The System Works

Real system recommendations prioritize selections primarily on attention or likes /
dislikes each user has, and based on the songs that the user interacts with, creates
a personalized listing based on songs that match the what the user is most engaged by. 

In the case of the system that the music recommender intends to implement, the 
songs are characterized by its genre, mood, energy, tempo, valence, danceability, and acousticness values, though only the values in the userProfile would be the ones
that I intend to use. Of these categories, the UserProfile stores the users favorite
genre, mood, energy, and acousticness preferences.

For the recommender, we will go down the list of criteria presented and assign a positive or negative score to the criteria measured based on how close the songs
characterisitcs are to the users preferences. The weighting scale (tentative to change) is as follows: 35% genre, 30% mood, 25% energy, and 10% acoustiness. 

Formula is as follows: (genre match) 35 + (mood match) 30 + 
(energy closeness) (max(0,1 - abs(energy - target_energy))) 25 +
(acoustinesses) ( 1 - acousticness value) 10 

Songs are chosen based on the sum of all the weighted values and compared to
a set minimum value, with filtered songs sorted from highest to lowest in the list.

In terms of biases, there are severe blind spots in all or nothing
approaches to genre and mood matches, since tangential relation 
to the genre isn't accounted for (i.e. hip hop and pop),  similarly with mood. Given the strength of genre and mood accounting for over 55% of the weight, it might be overbiases to match those two precisely. 

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Top recommendations for 'High-Energy Pop':

============================================================
1. Sunrise City by Neon Echo
   Score   : 96.20
   Genre   : pop
   Mood    : happy
   Reasons :
   - matches your favorite genre (+35)
   - matches your favorite mood (+30)
   - energy is close to your target (+23.0)
   - acousticness fits your preference (+8.2)
------------------------------------------------------------
2. Gym Hero by Max Pulse
   Score   : 68.75
   Genre   : pop
   Mood    : intense
   Reasons :
   - matches your favorite genre (+35)
   - energy is close to your target (+24.2)
   - acousticness fits your preference (+9.5)
------------------------------------------------------------
3. Rooftop Lights by Indigo Parade
   Score   : 58.00
   Genre   : indie pop
   Mood    : happy
   Reasons :
   - matches your favorite mood (+30)
   - energy is close to your target (+21.5)
   - acousticness fits your preference (+6.5)
------------------------------------------------------------
4. Neon District by Kilo Phase
   Score   : 33.90
   Genre   : techno
   Mood    : euphoric
   Reasons :
   - energy is close to your target (+24.5)
   - acousticness fits your preference (+9.4)
------------------------------------------------------------
5. Storm Runner by Voltline
   Score   : 33.75
   Genre   : rock
   Mood    : intense
   Reasons :
   - energy is close to your target (+24.8)
   - acousticness fits your preference (+9.0)
------------------------------------------------------------

Top recommendations for 'Chill Lofi':

============================================================
1. Library Rain by Paper Lanterns
   Score   : 64.85
   Genre   : lofi
   Mood    : chill
   Reasons :
   - matches your favorite genre (+35)
   - energy is close to your target (+21.3)
   - acousticness fits your preference (+8.6)
------------------------------------------------------------
2. Focus Flow by LoRoom
   Score   : 62.80
   Genre   : lofi
   Mood    : focused
   Reasons :
   - matches your favorite genre (+35)
   - energy is close to your target (+20.0)
   - acousticness fits your preference (+7.8)
------------------------------------------------------------
3. Midnight Coding by LoRoom
   Score   : 61.60
   Genre   : lofi
   Mood    : chill
   Reasons :
   - matches your favorite genre (+35)
   - energy is close to your target (+19.5)
   - acousticness fits your preference (+7.1)
------------------------------------------------------------
4. Velvet Dawn by Aster Vale
   Score   : 34.20
   Genre   : classical
   Mood    : serene
   Reasons :
   - energy is close to your target (+24.5)
   - acousticness fits your preference (+9.7)
------------------------------------------------------------
5. Spacewalk Thoughts by Orbit Bloom
   Score   : 32.20
   Genre   : ambient
   Mood    : chill
   Reasons :
   - energy is close to your target (+23.0)
   - acousticness fits your preference (+9.2)
------------------------------------------------------------

Top recommendations for 'Deep Intense Rock':

============================================================
1. Storm Runner by Voltline
   Score   : 97.50
   Genre   : rock
   Mood    : intense
   Reasons :
   - matches your favorite genre (+35)
   - matches your favorite mood (+30)
   - energy is close to your target (+23.5)
   - acousticness fits your preference (+9.0)
------------------------------------------------------------
2. Gym Hero by Max Pulse
   Score   : 62.50
   Genre   : pop
   Mood    : intense
   Reasons :
   - matches your favorite mood (+30)
   - energy is close to your target (+23.0)
   - acousticness fits your preference (+9.5)
------------------------------------------------------------
3. Neon District by Kilo Phase
   Score   : 33.65
   Genre   : techno
   Mood    : euphoric
   Reasons :
   - energy is close to your target (+24.2)
   - acousticness fits your preference (+9.4)
------------------------------------------------------------
4. Mirrorball Static by Juniper Glow
   Score   : 32.60
   Genre   : funk
   Mood    : playful
   Reasons :
   - energy is close to your target (+24.0)
   - acousticness fits your preference (+8.6)
------------------------------------------------------------
5. Sunrise City by Neon Echo
   Score   : 32.45
   Genre   : pop
   Mood    : happy
   Reasons :
   - energy is close to your target (+24.2)
   - acousticness fits your preference (+8.2)
------------------------------------------------------------
## Experiments You Tried

During this project, I ran three different changes: 2 of them being weight changes to genre and mood, and 1 feature removal with the exclusion of genre. The weights were decreased for
genre and mood since they were the most heavily weighed categories, with the experiments  reducing their values to a quarter of the original. When running the changed individually,  the results shifted drastically with the lowered genre value, whereas the mood reduction  kept mostly the same results with the normal weighing. When excluding the genre, the results
differed drastically from the original results, with high-energy pop users showing the most
drastic difference. This shows me that genre has an extremely heavy influence on the system, and in the future there needs to be redundancies to add points for similiar genres.   

## Limitations and Risks

Some limitations of the recommender is the implicit blind spot of not being
able to see relations or the intentions of the songs, rather its very binary
and objective where things need to match otherwise it considers it not  
matching at all. It is heavily biased towards exact mood and genre matches  
which makes the recommendation model extremely shallow when it comes to 
finding non ideal matches. 

## Reflection

Recommenders turn data into predictions by ingesting data profiles and running
comparisons through a statistical scoring system based on a set number of  target criteria and parameters collected from the users and subject data to 
approximate matches or best fits. Biases and unfairness as discussed in class
could arise from adhering too closely to the original baseline, which could 
discount prefectly acceptable results due to a huge bias or weight put towards
matching other criteria such as gender, gaps. It could even disregard useful 
data just because it hasn't been considered, such as publications. 

In terms of future work, I'll look at diversifying the results to avoid 
heavily recommending a select few of the artists because their entire song
list is of said genre, add methods for filtering out disliked categories,
customization for different search types, and also improve on the user  
interface by adding a GUI via streamlit and data persistence. 

