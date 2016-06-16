import web
import main
import savedecoder
import os

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

        #return render.test(test = savedecoder.fromAntiCheatFormat(form.save))

        form = web.input(save="")
        optAncients, diff = main.theMonsterMath(form.save)

        if optAncients == 'Invalid Save File':
            return render.fail()
        else:
            return render.index(optAncients.optArgaiv,
                                optAncients.optAtman,
                                optAncients.optBubos,
                                optAncients.optChronos,
                                optAncients.optDogcog,
                                optAncients.optDora,
                                optAncients.optFortuna,
                                optAncients.optKuma,
                                optAncients.optLibertas,
                                optAncients.optMammon,
                                optAncients.optMimzee,
                                optAncients.optMorg,
                                optAncients.optSiya,
                                optAncients.optSolomon,
                                diff['Argaiv'],
                                diff['Atman'],
                                diff['Bubos'],
                                diff['Chronos'],
                                diff['Dogcog'],
                                diff['Dora'],
                                diff['Fortuna'],
                                diff['Kuma'],
                                diff['Libertas'],
                                diff['Mammon'],
                                diff['Mimzee'],
                                diff['Morg'],
                                diff['Siya'],
                                diff['Solomon'])
                                
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    #app.run()