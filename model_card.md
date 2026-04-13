
Model Name

VibeMatch 1.0

Goal / Task

This recommender suggests songs based on a user’s preferences. It tries to match songs using features like genre, mood, and energy level.

Data Used

The dataset contains about 18 songs with different genres like pop, lofi, rock, jazz, and electronic. Each song has features such as energy, tempo, valence, danceability, and acousticness. The dataset is small and does not include all music styles, so it is limited.

Algorithm Summary

The model gives each song a score based on how well it matches the user’s preferences. Genre and mood matches give fixed points. Other features like energy and tempo are scored based on how close they are to the user’s target values. All scores are added together, and the songs are ranked from highest to lowest.

Observed Behavior / Biases

The system tends to favor songs with high energy because energy is strongly weighted in the scoring. Some songs appear in multiple recommendations, which shows a lack of variety. The dataset also has more pop and lofi songs, so those genres are recommended more often.

Evaluation Process

I tested the system using different user profiles such as high-energy pop, chill lofi, and intense rock. I compared the results to what I expected based on the preferences. I also tested edge cases with conflicting preferences to see how the system behaved.

Intended Use and Non-Intended Use

This system is designed for learning how recommender systems work. It should not be used for real music recommendations because the dataset is small and the model is simple.

Ideas for Improvement
Add more songs to increase variety and reduce bias
Adjust feature weights to balance recommendations better
Include more user data, like listening history or favorite artists

Personal Reflection

The biggest learning moment for me was realizing how small changes in weights can completely change the recommendations. At first, I thought the system would just pick songs randomly, but I saw how adjusting things like energy or genre made a big difference in the results.

Using AI tools helped me move faster, especially for structuring the code and understanding how to organize the scoring logic. However, I had to double-check the outputs because sometimes the AI suggested things that didn’t match my data structure or caused errors.

What surprised me most was how even a simple algorithm could feel like a real recommendation system. Even though it was just using basic rules, the results still made sense and matched user preferences in many cases.

If I extended this project, I would add more data and include features like user listening history or favorite artists. I would also try to improve diversity so the same songs don’t appear too often in different recommendations.