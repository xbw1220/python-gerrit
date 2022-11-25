from pygerrit2 import GerritRestAPI, HTTPBasicAuth, HTTPBasicAuthFromNetrc, Anonymous


class Gerrit(object):
    def __init__(self):
        self.gerrit_url = 'http://ip:8086'
        self.username = 'gerrit'
        self.http_password = 'EZrNP8axZ5cJfyaLP84IdxiTDBDaH3NJYEnrrQzLag'

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

