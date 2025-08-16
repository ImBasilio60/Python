import os
import random

def make_commits(days: int, max_commits_per_day: int = 5):
    if days < 1:
        os.system("git push")
        return
    else:
        num_commits = random.randint(0, max_commits_per_day)
        date_str = f"{days} days ago"

        for _ in range(num_commits):
            with open('data.txt', 'a') as file:
                file.write(f'{date_str} <- this was a commit for the day!!\n')

            os.system('git add data.txt')
            os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

        make_commits(days - 1, max_commits_per_day)

make_commits(152)
