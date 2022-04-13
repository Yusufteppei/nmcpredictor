import numpy as np
import pickle

subjects = [
         'BIOLOGY',
         'CHEMISTRY',
         'JUNIOR INFORMATICS',
         'JUNIOR MATHEMATICS',
         'JUNIOR SCIENCE',
         'PHYSICS',
         'SENIOR INFORMATICS',
         'SENIOR MATHEMATICS'
    ]

def predict(subject, score):
    features = []
    features.append(score)
    
    features += create_features(subject)[1:]
    features = np.array(features)
    pickle_out = open('nmcpredictor1.pickle', 'rb')
    model = pickle.load(pickle_out)
    v = model.predict(np.expand_dims(features, axis=0))
    p = model.predict_proba(np.expand_dims(features, axis=0))[0][1]
    success_probability = p
    if p > .7:
        result = "You'll likely qualify"
    elif p > .5:
        result = "You have about a 50-50 chance"
    else:
        result = "You'll likely not qualify"

    template = 'first_round/result.html'
    context = {
        'features': features,
        'result': result,
        'probability': success_probability
    }
    return result


def create_features(subject):
    print("Creating features...")
    print(f"Subject : {subject}")

    features = []

    for i in subjects:
        if i == subject:
            print("Subject found")
            features.append(1)
        else:
            print("Match false")
            features.append(0)
    print(f"features : {features}")
    return features
