from pygerrit2 import GerritRestAPI, HTTPBasicAuth, HTTPBasicAuthFromNetrc, Anonymous


class Gerrit(object):
    def __init__(self):
        self.auth = None
        self.gerrit_url = 'http://gerrit.auto-link.com.cn:8086'
        self.username = 'gerrit'
        self.http_password = 'cOLkcE21+TElvymOvviT4cVyLJQng0/cBmRhNs5P2w'

    def login(self):
        self.auth = HTTPBasicAuth(self.username, self.http_password)
        rest = GerritRestAPI(url=self.gerrit_url, auth=self.auth)
        return rest

    def query_change_para(self, owner: str, start_time: str, end_time: str):
        username = owner
        star_time = start_time
        end_time = end_time
        query = ["status:merged"]
        query += ["owner:{0}".format(username)]
        query += ["after:{0}".format(star_time)]
        query += ["before:{0}".format(end_time)]
        return query