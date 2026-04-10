#
diseases = {
    "Flu": {"fever", "cough", "body aches", "fatigue", "chills"},
    "Cold": {"runny nose", "cough", "sore throat"},
    "Strep Throat": {"sore throat", "fever", "difficulty swallowing"},
    "Food Poisoning": {"nausea", "vomiting", "diarrhea", "abdominal pain"}


} #sample diseases

user_symptoms1 = {"fever", "cough"} #sample symptoms
user_symptoms2 = {"nausea", "vomiting"}
user_symtpoms_3 = {"runny nose", "cough", "sore throat"}


def score_conditions(user_symptoms, diseases):
    scores = {} #empty dictionary holds results
    for condition_name, condition_symptoms in diseases.items():
        matched = condition_symptoms & user_symptoms
        score = len(matched) / len(condition_symptoms)
        scores[condition_name] = score
    return scores
