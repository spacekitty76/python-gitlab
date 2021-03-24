import gitlab

# private token auth
with gitlab.Gitlab("https://gitlab.com", private_token="") as gl:
    gl.auth()

    # list projects in a given group
    group = gl.groups.get(7005886)
    for project in group.projects.list(as_list = False):
        # print(project.name, project.id, project.ssh_url_to_repo)
    # reporting = gl.projects.get(16633661)
    # print(reporting)
    # print(type(reporting))
    # tree_list = reporting.repository_tree(recursive = True, all = True)
    # for item in tree_list:
    #     # print(item)
    #     if item["name"] == ".gitlab-ci.yml":
    #         print(item["name"], item["path"])
