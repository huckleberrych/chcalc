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

        optAncients, diff, calcs, msg = main.theMonsterMath(form.save, form.useAscendSouls)
        
        if msg in ('You need to buy Siyalatas!',
                       'Invalid Save File',
                       'Invalid Save File - bad hash'):
            return render.fail(msg = msg)
        else:
            return render.index(optAncients, diff, calcs, msg)

if __name__ == "__main__":
    app.run()