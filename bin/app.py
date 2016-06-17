import web
import main

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()
        
    def POST(self):

        form = web.input(save="")
        optAncients, diff, calcs = main.theMonsterMath(form.save)
        
        if optAncients == 'Invalid Save File':
            return render.fail()
        else:
            return render.index(optAncients, diff, calcs)

if __name__ == "__main__":
    app.run()