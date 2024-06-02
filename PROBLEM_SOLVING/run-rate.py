run_rate = float(input("enter a run_rate for T20 match: "))

def total_runs(run_rate, overs):
    score = run_rate * overs
    return score

print(total_runs(run_rate,overs=20))
