import sys
from github import Github


class CreateIssueError:
    def __init__(self, e):
        value = str(sys.exc_info()[1])
        line = sys.exc_info()[2].tb_lineno
        file = sys.exc_info()[2].tb_frame

        token = input('Token:\n')
        github_account = Github(token)
        repository = github_account.get_repo('sousa-jp/automatic_issues')

        body = 'Value:\n{}\n\nTraceback:\nline {}\nfile {}'.format(value, line, file)
        label = repository.get_label("bug")
        title = str(e.args[0])
        print(body)

        repository.create_issue(title=title,
                                body=body,
                                labels=[label])


if __name__ == '__main__':
    try:
        teste = 'asasda'
        int(teste)
    except Exception as E:
        CreateIssueError(E)



