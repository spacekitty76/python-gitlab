import gitlab
import subprocess
import sys
from ruamel.yaml import YAML
# pip3 install ruamel.yaml
# pip3 install ruamel.yaml.cmd

    # private token auth
    with gitlab.Gitlab("https://gitlab.com", private_token="") as gl:
        gl.auth()

        # repos_to_pull = []

        list projects in a given group
        group = gl.groups.get(7005886) #hg group
        for project in group.projects.list(as_list = False):
            # print(project.name, project.id, project.ssh_url_to_repo)
            repo = gl.projects.get(project.id)
            # print(repo.path) # this is how we get the file name to load
            # print(reporting)
            # print(type(reporting))
            tree_list = repo.repository_tree(recursive = True, all = True)
            for item in tree_list:
                # print(item)
                if item["name"] == ".gitlab-ci.yml":
                    # repos_to_pull.append(project.ssh_url_to_repo)
                    print(item["name"], project.ssh_url_to_repo)
                    subprocess.call(['git', 'clone', repos_to_pull[0]])
        # print(repos_to_pull)


# file_name = "export-service/.gitlab-ci.yml"
# yaml = YAML()
# with open(file_name) as fp:
#     data = yaml.load(fp)


# with open(file_name, 'w') as fp:
#     yaml.dump(data, fp)