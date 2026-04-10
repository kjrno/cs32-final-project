#
diseases = {
    "Flu": {"fever", "cough", "body aches", "fatigue", "chills"},
    "Cold": {"runny nose", "cough", "sore throat"}


} #Sa

user_symptoms = {"fever", "cough"}

def score_conditions(user_symptoms, diseases):
    scores = {} #empty dictionary holds results
    for condition_name, condition_symptoms in diseases.items():
        matched = condition_symptoms & user_symptoms
        score = len(matched) / len(condition_symptoms)
        scores[condition_name] = score
    return scores
