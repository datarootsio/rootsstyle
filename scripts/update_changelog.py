import os
import re

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

def write_git_commit_to_log_file():
    cmd = f"git log --pretty=format:'- %ad%x09%s' --date=short > {LOG_FILE}"
    os.system(cmd)

def split_logs_into_version_release():
    line_pattern = re.compile(r"- (?P<date>[\d]{4}-[\d]{2}-[\d]{2})\s(?P<message>.*)", re.ASCII)
    pr_merge_pattern = re.compile(r"Merge pull request #[\d]* from datarootsio/v(?P<version>[\d].[\d].[\d])")
    def create_version_header(date, version):
        return f"""<div align=center>
            <b>
            <p>========================</p>
            <p>{date}   --   v{version}</p>
            <p>========================</p>
            </b>
        </div>\n\n"""
    def handle_line(line):
        m = re.match(line_pattern, line)
        if m is not None:
            date, message = m.group('date'), m.group('message')
            m_pr = re.match(pr_merge_pattern, message)
            if m_pr is not None:
                return create_version_header(date, m_pr.group('version'))
            else:
                return f"- {message}\n"
        else:
            raise ValueError("invalid commit line, not able to match")


    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i]= handle_line(line)
    return lines

write_git_commit_to_log_file()
new_lines = split_logs_into_version_release()
new_lines = [l for l in new_lines if not re.match(patterns_to_ignore, l.strip().lower())]
with open(LOG_FILE, 'w') as f:
    [f.write(line) for line in new_lines]
        