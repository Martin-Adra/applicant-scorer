import json
import numpy as np
from collections import Counter

def compute_score(applicant_attrs, team_attrs_list):
    """
    Compute the score of an applicant based on the distance from the team average.
    The score is normalized to be between 0 and 1, where 0 is a perfect match and 1 is a complete mismatch.
    The distance is calculated using the Euclidean distance formula, and then normalized by the maximum possible distance.

    Parameters:
    applicant_attrs: dict, attributes of the applicant
    team_attrs_list: list of dicts, attributes of the team members
    """

    # 1) Sum all team attributes
    sums = Counter() 
    for member in team_attrs_list:
        sums.update(member) # Using Counter to sum the attributes

    # 2) Compute the average for each attribute
    team_size = len(team_attrs_list)
    team_avg = {}
    for attr, total in sums.items():
        team_avg[attr] = total / team_size # Average for each attribute

    # 3) Euclidean distance between applicant and team average
    dist_sq = 0.0
    for a in applicant_attrs:
        diff = applicant_attrs[a] - team_avg[a] # Difference between applicant and team average
        dist_sq += diff ** 2 
    dist = np.sqrt(dist_sq) # Euclidean distance

    # 4) Normalize the distance into [0,1]
    max_range = 10.0 # Assuming the max range of each attribute is 10 from what I have seen in the input example
    max_dist = np.sqrt(len(applicant_attrs) * (max_range ** 2))
    normalized_dist = dist / max_dist # Normalizing the distance
    return normalized_dist


def main():

    # Read the input JSON file
    with open('input.json', 'r') as in_f:
        data = json.load(in_f)

    # Extract team and applicants from the input data
    team = data["team"]
    applicants = data["applicants"]
    team_attrs_list = [m["attributes"] for m in team]

    # Compute the score for each applicant and append to the list "scored"
    scored = []
    for app in applicants:
        s = compute_score(app["attributes"], team_attrs_list)
        scored.append({"name": app["name"], "score": round(s,2)})

    # Output the results to a JSON file
    with open('output.json', 'w') as out_f:
        json.dump({"scoredApplicants": scored}, out_f, indent=2)

if __name__ == "__main__":
    main()
