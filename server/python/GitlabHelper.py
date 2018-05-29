import re
from categories import categories
import json
import requests

import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

import datetime
import configparser

ROOT = dirname(__file__)[:-14]
dotenv_path = ROOT + "/server/documents/local/app-env"
load_dotenv(dotenv_path)

class GitlabHelper ():
    # get all commits
    def getcommits(self, GITLAB_URL, projectid, TOKEN):
        commits = []
        counter = 1
        URL = GITLAB_URL + "/projects/" + str(projectid) + "/repository/commits?ref_name=master&per_page=100&page="
        r = requests.get(URL + str(counter), headers={'PRIVATE-TOKEN': TOKEN})

        while len(r.json()) > 0:
            commits.extend(r.json())
            counter += 1
            r = requests.get(URL + str(counter), headers={'PRIVATE-TOKEN': TOKEN})

        return commits

    def convertEmailtoGitlabId(self, authoremail, studentidmaps):

        indexofat = authoremail.find("@")
        authorname = authoremail[:indexofat]

        if authorname in studentidmaps["email"]:
            authorname = studentidmaps["email"][authorname]
        elif authorname in studentidmaps["netid"]:
            authorname = studentidmaps["netid"][authorname]
        return authorname