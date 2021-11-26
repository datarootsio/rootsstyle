import os
import re
import logging
import subprocess

LAST_COMMIT_HASH = "51c290b268f463daf50713fbd719ec844a855712" #Merge pull request #8 from datarootsio/v0.1.7
LOG_FILE = 'CHANGELOG.md'
patterns_to_ignore = [
    "- testing gh actions",
    "- update[d]? gh actions",
    "- update[d]? readme[.md]?",
    "- readme[.md]? update[d]?",
    "- update[d]? version",
    "- linting",
    "- automated commit of .*",
    "- merge branch .* of .* into .*"
]
patterns_to_ignore = "(" + ")|(".join(patterns_to_ignore) + ")"

def read_current_changelog():
    with open(LOG_FILE, 'r') as f:
        return f.readlines()

def get_new_commits():
    cmd = f"git log {LAST_COMMIT_HASH}.. --pretty=format:'- %ad%x09%s' --date=short"
    git_output = subprocess.check_output(cmd, shell=True).decode('utf-8')
    return git_output.split('\n')

def cleanup_commits(commits):
    commit_pattern = re.compile(r"- (?P<date>[\d]{4}-[\d]{2}-[\d]{2})\s(?P<message>.*)", re.ASCII)
    pr_merge_pattern = re.compile(r"Merge pull request #[\d]* from datarootsio/(?P<version>.*)")
    def create_version_header(date, version):
        return f"""<div align=center>
            <b>
            <p>========================</p>
            <p>{date}   --   {version}</p>
            <p>========================</p>
            </b>
        </div>\n\n"""

    def handle_commit(commit):
        m = re.match(commit_pattern, commit)
        if m is not None:
            date, message = m.group('date'), m.group('message')
            m_pr = re.match(pr_merge_pattern, message)
            if m_pr is not None:
                return create_version_header(date, m_pr.group('version'))
            else:
                return f"- {message}\n"
        else:
            logging.warning("Commit does not match pattern")
            return f"{commit}\n"

    # Cleanup the commits and return all commits that do not need to be filtered out
    for i, commit in enumerate(commits):
        commits[i]= handle_commit(commit)
    commits = [c for c in commits if not re.match(patterns_to_ignore, c.strip().lower())]
    return commits


if __name__=="__main__":
    existing_commits = read_current_changelog()
    new_commits = get_new_commits()
    new_commits = cleanup_commits(new_commits)
    new_commits.extend(existing_commits)
    with open(LOG_FILE, 'w') as f:
        [f.write(commit) for commit in new_commits]
        