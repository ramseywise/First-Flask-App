# def clean_word(text):
#     # Removes symbols, numbers, some stop words
#     return cleaned_text

# def raw_chat_to_model_input(raw_input_string):
#     # Converts string into cleaned text, converts it to model input
#     return word_vectorizer.transform(cleaned_text)
# def predict_toxicity(raw_input_string):
#     # Takes in a user input string, predict the toxicity levels
#     model_input = raw_chat_to_model_input(raw_input_string)
#     results = []
#     # I use a dictionary of multiple models in this project
#     for key,model in model_dict.items():
#         results.append(round(model.predict_proba(model_input)))
#     return results
# def make_prediction(input_chat):
#     '''
#     Given string to classify, returns the input argument and the
#     dictionary of model classifications in a dict so that it may be
#     passed back to the HTML page.
#     '''
#     # Calls on previous functions to get probabilities of toxicity
#     pred_probs = predict_toxicity(input_chat)
#     probs = [{'name': list(model_dict.keys())[index], 'prob': \
#             pred_probs[index]} \
#             for index in np.argsort(pred_probs)[::-1]]
# return (input_chat, probs)
