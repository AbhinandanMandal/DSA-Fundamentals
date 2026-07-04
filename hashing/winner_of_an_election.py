
"""
Given an array of n names arr of candidates in an election, 
where each name is a string of lowercase characters. 
A candidate name in the array represents a vote casted to the candidate. 
Print the name of the candidate that received the maximum count of votes. 
If there is a draw between two candidates, then print lexicographically smaller name.
"""

def winner(arr):
    votes={}
    
    for name in arr:
        votes[name] = votes.get(name,0)+1

    # Now to find the majority i.e. winner of an election
    max_votes=max(votes.values())
    ans=""

    for name in arr:
        if votes[name]==max_votes:
            if ans=="" or name<ans:
                ans=name
    return ans, max_votes


arr = ["john", "johnny", "jackie", "johnny", "john",
       "jackie", "jamie", "jamie", "john", "johnny",
       "jamie", "johnny", "john"]
print(winner(arr))

