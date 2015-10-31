"""
    hdrs.py compares http response headers
    Copyright (C) 2015 Aaron Hampton

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import http.client
import sys

UA = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"

HEADERS = {'User-Agent': UA}

methods = ('GET', 'HEAD', 'PUT', 'POST', 'OPTIONS', 'TRACE', 'BATMAN')

def main(url, path):
    for m in methods:
        conn = http.client.HTTPConnection(url)
        conns = http.client.HTTPSConnection(url)

        conn.request(m, path)
        conns.request(m, path, headers=HEADERS)
        resp = conn.getresponse()
        resps = conns.getresponse()

        print(m, "\n")

        if resp.getcode() in http.client.responses:
            code = http.client.responses[resp.getcode()]
        else:
            code = resp.getcode()

        if resps.getcode() in http.client.responses:
            codes = http.client.responses[resps.getcode()]
        else:
            codes = resps.getcode()

        print("HTTP", code)
        for i in resp.getheaders():
            print(i[0], '=', i[1])
        if m == 'TRACE' and resp.getcode() == 200:
            print(resp.read().decode('utf-8'))
        print("\nHTTPS", codes)
        for i in resps.getheaders():
            print(i[0], '=', i[1])
        if m == 'TRACE' and resps.getcode() == 200:
            print(resps.read().decode('utf-8'))
        print("\n")

if __name__=='__main__':
    arg = sys.argv[1].split("/")
    if len(arg) > 1:
        url = arg[0]
        path = "/" + "/".join(arg[1:])
    else:
        url = arg[0]
        path = ""

    main(url, path)