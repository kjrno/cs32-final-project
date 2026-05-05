import tkinter as tk #For user interface

#Revised using object-oriented programming
class Condition:
    def __init__(self, name, symptoms, treatments):
        self.name = name
        self.symptoms = symptoms
        self.treatments = treatments

    def score(self, user_symptoms):
        matched = self.symptoms & user_symptoms
        return len(matched)/len(self.symptoms)

    def get_treatments(self):
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
    {"runny nose", "cough", "sore throat"},
    ["Rest", "Hydrate", "Gargle salt water", "Decongestants"]
)
strep = Condition(
    "Strep Throat",
    {"sore throat", "fever", "difficulty swallowing"},
    ["Antibiotics", "Acetaminophen or ibuprofen", "Hydration", "Rest"]
)
food_poisoning = Condition(
    "Food Poisoning",
    {"nausea", "vomiting", "diarrhea", "abdominal pain"},
    ["Drink fluids", "Bland Diet", "Avoid irritants", "Over-the-counter medication"]
)

conditions = [flu, cold, strep, food_poisoning]

all_symptoms = set()
for c in conditions:
    all_symptoms |= c.symptoms #adds sypmtoms into all_symptoms

def user_questionaire():
    user_symptoms = set()
    print("Answer Yes/No to each symptom:\n")
    for symptom in sorted(all_symptoms):
        answer = input(f"Do you have {symptom}? ").strip().lower()
        if answer == "yes":
            user_symptoms.add(symptom)
    return user_symptoms

def score_all(user_symptoms, conditions): #Scores conidition based on symptoms
    scores = {}
    for condition in conditions:
        scores[condition.name] = condition.score(user_symptoms)
    return scores

def diagnose(user_symptoms, conditions):
    results = score_all(user_symptoms, conditions)
    ranked = sorted(results.items(), key = lambda x: x[1], reverse = True) #Sort based on score from largest to smallest

    print("\nPossible Conditions:")
    for name, score in ranked:
        if score > 0:
            print(f" - {name}: {score * 100}%") #Calculate percentage of likeliness

        best_match, best_score = ranked[0] #Gets best match
        if best_score > 0:
            for condition in conditions:
                if condition.name == best_match:
                    condition.get_treatments()
        else:
            print("No matches found.")

