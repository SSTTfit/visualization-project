import requests


def authenticate():
    """
    authenticate user
    :return: session
    """
    url = 'http://10.112.226.2:7070/kylin/api/user/authentication'
    headers = {'Authorization': 'Basic QURNSU46S1lMSU4='}
    s = requests.session()
    s.headers.update({'Content-Type': 'application/json'})
    s.post(url, headers=headers)
    return s


def query(sql_str, session):
    """
    sql query
    :param sql_str: string of sql
    :param session: session object
    :return: results(type is list)
    """
    url = 'http://10.112.226.2:7070/kylin/api/query'
    json_str = '{"sql":"' + sql_str + '", "offset": 0, "limit": 50000, ' \
                                      '"acceptPartial": false, "project": "test"}'
    r = session.post(url, data=json_str)
    results1 = r.json()
    return results1['results']

if __name__ == "__main__":
    s = authenticate()
    print('Authenticated!')
    sql = "select disease from test "
    result = query(sql,s)
    print(result)
    s1 = result[0][0].split()
    s2 = result[1][0].split()
    data = {}
    data[s1[0]] = s1[1:]
    data[s2[0]] = s2[1:]
    print(data)
    print('Done!')
