from data import tasks
from model import rank_tasks, FEATURE_WEIGHTS

ranked_tasks = rank_tasks(tasks, FEATURE_WEIGHTS)
for task in ranked_tasks:
    print(task)