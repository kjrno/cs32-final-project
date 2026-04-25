#Revised ussing object-oriented programming
class Disease:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

    def score(self, user_symptoms):
        matched = self.symtpoms & user_symptoms
        return len(matched/len(self.symptoms))

#Create objects from Disease
conditions = {
    "Flu": {"fever", "cough", "body aches", "fatigue", "chills"},
    "Cold": {"runny nose", "cough", "sore throat"},
    "Strep Throat": {"sore throat", "fever", "difficulty swallowing"},
    "Food Poisoning": {"nausea", "vomiting", "diarrhea", "abdominal pain"}


} #sample diseases

user_symptoms1 = {"fever", "cough"} #sample symptoms
user_symptoms2 = {"nausea", "vomiting"}
user_symptoms3 = {"runny nose", "cough", "sore throat"}


def score_conditions(user_symptoms, conditions):
    scores = {} #empty dictionary holds results
    for condition_name, condition_symptoms in conditions.items():
        matched = condition_symptoms & user_symptoms #finds symptoms that match with condition
        score = len(matched) / len(condition_symptoms) #calculates percentage matched of total condition symptoms
        scores[condition_name] = score
    return scores

results = score_conditions(user_symptoms1, conditions)
print(results)
