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
    {"Rest", "Hydrate", "Acetaminophen or ibuprofen", "Antiviral medication"}
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

def score_all(user_symptoms, conditions): #Scores conidition based on symptoms
    scores = {}
    for condition in conditions:
        scores[condition.name] = condition.score(user_symptoms)
    return scores

def run_gui():
    root = tk.Tk()
    root.title("Symptom Checker")

    tk.Label(root, text="Check all symptoms you have:",
             font=("Arial", 12, "bold")).pack(pady=10)

    #Create dictionary mapping symptoms to its IntVar
    symptom_vars = {}
    for symptom in sorted(all_symptoms):
        var = tk.IntVar()
        tk.Checkbutton(root, text=symptom, variable=var).pack(anchor="w", padx=20)
        symptom_vars[symptom] = var

    #Box to display result
    result_box = tk.Text(root, height=12, width=50)
    result_box.pack(pady=10, padx=10)

    def on_diagnose():
        #Collect checked symptoms
        user_symptoms = {s for s, v in symptom_vars.items() if v.get() == 1}

        result_box.delte("1.0", tk.END) #Clears previous results

        if not user_symptoms:
            result_box.insert(tk.END, "Please select at least one symptom.")
            return

        results = score_all(user_symptoms, conditions)
        ranked = sorted(results.items(), key = lambda x: x[1], reverse = True) #Sort based on score from largest to smallest

        result_box.insert(tk.END, "Possible Conditions:\n")
        for name, score in ranked:
            if score > 0:
                result_box.insert(tk.END, f" - {name}: {score * 100:.1f}%") #Calculate percentage of likeliness
        best_match, best_score = ranked[0] #Gets best match
        if best_score > 0:
            for condition in conditions:
                if condition.name == best_match:
                    result_box.insert(tk.END, f"\nTreatments for {best_match}:\n")
                    for t in condition.treatments:
                        result_box.insert(tk.END, f" - {t}\n")
        else:
            result_box.insert(tk.END, "No matches found.")
    tk.Button(root, text="Diagnose", command=on_diagnose).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
