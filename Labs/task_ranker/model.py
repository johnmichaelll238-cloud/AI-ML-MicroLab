FEATURE_WEIGHTS = {
    "importance" : 0.5,
    "urgency" : 0.3,
    "difficulty" : 0.2
}
def calculate_score(task, weights):
    score = 0;

    for feature, weight in weights.items():
        score += task[feature] * weight
    return score    
   
def rank_tasks(tasks, weights):
    return sorted(
        tasks,
        key=lambda task: calculate_score(task, weights),
        reverse=True
    )


