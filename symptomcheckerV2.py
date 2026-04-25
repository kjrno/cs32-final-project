#Revised ussing object-oriented programming
class Condition:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

    def score(self, user_symptoms):
        matched = self.symtpoms & user_symptoms
        return len(matched/len(self.symptoms))

    def treatments(self):
        print(f'\nRecommended treatments for {self.name}:')
        for treatment in self.treatments:
            print(f' - {treatment}')

#Create objects from Disease
flu = Condition(
    "Flu",
    {"fever", "cough", "body aches", "fatigue", "chills"},
    {"Rest", "Hydrate", "Acetminophen or ibuprofen", "Antiviral medication"}
)
cold = Condition(
    "Cold",
    {"runny nose", "cough", "sore throat"}
    ["Rest", "Hydrate", "Gargle salt water", "Decongestants"]
)
strep = Condition(
    "Strep Throat",
    {"sore throat", "fever", "difficulty swallowing"}
    ["Antibiotics", "Acetminophen or ibuprofen", "Hydration", "Rest"]
)
food_poisoning = Condition(
    "Food Poisoning",
    {"nausea", "vomiting", "diarrhea", "abdominal pain"}
    []
)

conditions = [flu, cold, strep, food_poisoning]

user_symptoms1 = {"fever", "cough"} #sample symptoms
user_symptoms2 = {"nausea", "vomiting"}
user_symptoms3 = {"runny nose", "cough", "sore throat"}


def score_all(user_symptoms, conditions):
    scores = {}
    for condition in conditions:
        scores[condition.name] = condition.score(user_symptoms)
    return scores

def diagnose(user_symptoms, conditions):
    results = score_all(user_symptoms, conditions)
    print(results)

    best_match = max(results, key=results.get) #Finds condition with highest score
    for condition in conditions:
        if condition.name == best_match:
            condition.treatments()

diagnose(user_symptoms1, conditions)
