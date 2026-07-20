# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



