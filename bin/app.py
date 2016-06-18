import web
import main

urls = (
  '/', 'Index',
  '/changelog', 'Changelog'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Changelog(object):
    def GET(self):
        return render.changelog()

class Index(object):
    def GET(self):
        return render.hello_form()
        
    def POST(self):

        form = web.input(save="", useAscendSouls='off')

        optAncients, diff, calcs = main.theMonsterMath(form.save, form.useAscendSouls)
        
        if isinstance(optAncients, str):
            return render.fail(failmsg = optAncients)
        else:
            return render.index(optAncients, diff, calcs)

if __name__ == "__main__":
    app.run()