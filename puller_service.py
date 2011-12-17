import urlparse, web, json, os
from config import REF, PATH, REMOTE, BRANCH, WSGI_PATH
from subprocess import call

PULL_CMD = 'git --git-dir=%(path)s pull %(remote)s %(branch)s' %  \
                                {'path':PATH,'remote':REMOTE,'branch':BRANCH}
RESTART_CMD = 'touch %s' % WSGI_PATH

urls = (
    '/(.*)', 'hello'
    )
app = web.application(urls, globals())

class hello:

    def POST(self,*args,**kwargs):
        response = urlparse.parse_qs(web.data())
        payload = response['payload'][0]
        data = json.loads(payload)
        if data['ref']==REF:
            code1 = call(PULL_CMD.split())
            print code1
            if os.path.isfile(WSGI_PATH):
                code2 =call(RESRTART_CMD.split())
                print code2

if __name__ == "__main__":
    app.run()