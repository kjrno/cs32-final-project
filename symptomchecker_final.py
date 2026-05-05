from flask import Flask, request #Import Flask

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
    all_symptoms |= c.symptoms #adds symptoms into all_symptoms

def score_all(user_symptoms, conditions): #Scores conidition based on symptoms
    scores = {}
    for condition in conditions:
        scores[condition.name] = condition.score(user_symptoms)
    return scores

#Create Flask web app
app = Flask(__name__)

@app.route("/")
def home():
    #Build checkboxes from symptoms
    checkboxes = ""
    for symptom in sorted(all_symptoms):
        checkboxes += f'<input type="checkbox" name="symptoms" value="{symptom}"> {symptom}<br>' #Builds one HTML checkbox for each symptom

    return f"""
    <h1>Symptom Checker</h1>
    <p>Check all symptoms you have:</p>
    <form action="/diagnose" method="post">
        {checkboxes}
        <br>
        <button type="submit">Diagnose</button>
    </form>
    """
@app.route("/diagnose", methods=["POST"]) #Runs when form is submitted
def diagnose():
    user_symptoms = set(request.form.getlist("symptoms")) #Gets checked symptoms from the form

    if not user_symptoms:
        return '<p>Please select at least one symtpom.</p><a href="/">Back</a>'

    results = score_all(user_symptoms, conditions)
    ranked = sorted(results.items(), key = lambda x: x[1], reverse = True) #Sort based on score from largest to smallest

    output = "<h1>Possible Conditions:</h1><ul>" #Builds results page
    for name, score in ranked:
        if score > 0:
            output += f"<li>{name}: {score * 100:.1f}%</li>" #Adds each condition with percentage of likeliness
    output += "</ul>"

    best_match, best_score = ranked[0] #Gets best match
    if best_score > 0:
        for condition in conditions:
            if condition.name == best_match:
                output += f"<h2>Treatments for {best_match}:</h2><ul>"
                for treatment in condition.treatments:
                    output += f"<li>{treatment}</li>"
                output += "</ul>"
    else:
        output += "<p>No matches found.</p>"

    output += '<br><a href="/">Start over</a>'
    return output

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000) #Starts the web server
