from github import Github
from getpass import getpass
user = raw_input("Username: ")
password = getpass("Password: ")

g = Github(user, password)
u = g.get_user(user)
l = u.get_repos()
for r in l:
    print("")
    print("")
    print r.full_name
    lc = r.get_commits()
    print("Commits:")
    for c in lc:
        print("  " + c.commit.message)

# >>> r.get_commits()
# <github.PaginatedList.PaginatedList instance at 0x1080ba320>
# >>> c = r.get_commits()
# >>> dir(c)
# ['_PaginatedListBase__elements', '_PaginatedListBase__fetchToIndex', '_PaginatedList__contentClass', '_PaginatedList__firstParams', '_PaginatedList__firstUrl', '_PaginatedList__nextParams', '_PaginatedList__nextUrl', '_PaginatedList__parseLinkHeader', '_PaginatedList__requester', '_PaginatedList__reverse', '_PaginatedList__totalCount', '_Slice', '__doc__', '__getitem__', '__init__', '__iter__', '__module__', '_couldGrow', '_fetchNextPage', '_getLastPageUrl', '_grow', '_isBiggerThan', '_reversed', 'get_page', 'reversed', 'totalCount']
# >>> c[0]
# <github.Commit.Commit object at 0x1080febd0>
# >>> c[0].comit
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Commit' object has no attribute 'comit'
# >>> c[0].commit
# <github.GitCommit.GitCommit object at 0x1080fec50>
# >>> c[0].commit.message
# u'code markup'
