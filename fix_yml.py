import gitlab

# private token auth
gl = gitlab.Gitlab("https://gitlab.com", private_token="")
gl.auth()

# list projects in a given group
group = gl.groups.get(7005886)
for project in group.projects.list():
    print(project)