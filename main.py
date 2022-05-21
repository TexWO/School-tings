import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Tæller hvor mange ord der er tilstede i user_message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Regner procenten ud fra hvilken respons der passer bedst
    percentage = float(message_certainty) / float(len(recognised_words))

    #Tjekker required_words i gennem for at se om den genkender et ord i user_message
    for word in required_words:
        if word not in user_message:
            has_required_words = False
        break

    #Skal enten have required word eller single response, ellers return 0 så man får unknown response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    


#Responses  (Bot_response, list of keywords, single_response eller om der er required_words)
    response("Hello!", ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('I like Katy Perry', ['music', 'like'], required_words=['music'])
    response("What a nerd", ["gaming"], single_response=True)
    
    #Long responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['eat'])  
    response(long.R_WEATHER, ['how', 'weather', 'today'], required_words=['weather', 'today'])
    response(long.R_FREETIME, ['freetime', 'your', 'what'], required_words=['freetime'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    

#Får response
def get_response(user_input):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response

#While loop der holder chatbotten igang
while True:
    print("Sam: " + get_response(input("You: ")))
