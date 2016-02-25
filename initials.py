from fetchable import fetchable


class commits(fetchable):
    """
    docstring for commits
    """
    def __init__(self, ghub):
        self.repo = ghub.get_repo('cujomalainey/Dstancr')

    def fetch(self):
        return [c.author.name for c in self.repo.get_commits()[0:8]]


class repos(fetchable):
    """
    docstring for commits
    """
    def __init__(self, ghub):
        self.user = ghub.get_user()

    def fetch(self):
        return [r.name for r in self.user.get_repos()[0:8]]
