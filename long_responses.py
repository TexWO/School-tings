import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_WEATHER = "The weather is quite nice today i think, what do you think?"
R_FREETIME = "I do like to listen to Katy Perry in my freetime, what do you do in your freetime?"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Oh! It seems you wrote something I don't understand",
                "What does that mean?"][
        random.randrange(4)]
    return response