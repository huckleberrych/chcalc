import web
import main
import maintest

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

        form = web.input(save="", useAscendSouls='off', mode='idle')

        #optAncients, diff, calcs, optcost, msg = main.theMonsterMath(form.save, form.useAscendSouls, form.mode, float(form.hybridMultiplier))
        curAncients, optAncients, diff, calcs, optcost, msg = maintest.theMonsterMath(form.save, form.useAscendSouls, form.mode, float(form.hybridMultiplier))

        if msg in ('You need to buy Siyalatas!',
                       'Invalid Save File',
                       'Invalid Save File - bad hash'):
            return render.fail(msg = msg)
        elif form.mode == 'hybrid':
            return render.index_hybrid_test(curAncients, optAncients, diff, calcs, optcost, msg)
        else:
            return render.index_idle_test(curAncients, optAncients, diff, calcs, optcost, msg)
    """        
        if msg in ('You need to buy Siyalatas!',
                       'Invalid Save File',
                       'Invalid Save File - bad hash'):
            return render.fail(msg = msg)
        elif form.mode == 'hybrid':
            return render.index_hybrid(optAncients, diff, calcs, optcost, msg)
        else:
            return render.index_idle(optAncients, diff, calcs, optcost, msg)
    """
if __name__ == "__main__":
    app.run()