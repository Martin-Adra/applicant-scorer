# Applicant Scorer

A small Python CLI that takes in a JSON file describing your team and applicants, computes a compatibility score for each applicant (based on similarity to the team's average attributes), and outputs a JSON with each applicant’s score in [0,1].

## Usage

The script reads from `input.json` and writes to `output.json`.

### 1. Prepare your input file

Create a file named `input.json` alongside `score_applicants.py`, with this structure:

```json
{
  "team": [
    {
      "name": "Eddie",
      "attributes": {
        "intelligence": 1,
        "strength": 5,
        "endurance": 3,
        "spicyFoodTolerance": 1
      }
    }
    // …other team members…
  ],
  "applicants": [
    {
      "name": "John",
      "attributes": {
        "intelligence": 4,
        "strength": 5,
        "endurance": 2,
        "spicyFoodTolerance": 1
      }
    }
    // …other applicants…
  ]
}
```

### 2. Run the scorer

As I used windows for my program, from your PowerShell, simply call out:

```
# Windows (if using the py launcher)
py score_applicants.py
```

### 3. Output

Once the script finishes running, an `output.json` file will pop up in the same directory looking like this:

``` json
{
  "scoredApplicants": [
    { "name": "John", "score": 0.20 },
    { "name": "Jane", "score": 0.18 },
    { "name": "Joe",  "score": 0.40 }
  ]
}
```

Each "score" is the normalized Euclidean distance (0 = exact match, 1 = maximally different) between that applicant’s attribute vector and the team’s average attribute vector.