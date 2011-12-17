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
            call(PULL_CMD.split())
            if os.path.isfile(WSGI_PATH):
                call(RESTART_CMD.split())
            else:
                print 'no such file: %s' % WSGI_PATH

if __name__ == "__main__":
    app.run()