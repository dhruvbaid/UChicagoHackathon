from flask import Flask
from flask import render_template
from flask import request
import processImage

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.run(debug = True)

@app.route('/')
def landing():
    # this is where we want to put our landing page (in t1.html, for example)
    return render_template("t1.html", name = "Dhruv")

@app.route('/input', methods=['GET', 'POST'])
def user_input():
    # if we are loading the form without any submissions, simply show the form
    if request.method == "GET":
        return render_template("input.html")
    # if there is something user(s) submitted, process the input
    else:
        # print(request.form)
        userFile = request.files["fileUpload"]

        # the uploaded file is saved as roomPic.jpg in the current directory
        userFile.save("./roomPic.jpg")

        res = processImage.process("./roomPic.jpg")

        names = []
        for x in res:
            name = x.to_dict()['name']
            names.append(name)
        print(names)
        
        electricityMessage = """You seem to have some electrical appliances in your room; energy inefficiency
                                is bad, so remember to switch those off before you leave!"""
        woodMessage = """You have wood in your house! Always keep in mind that a lot of trees had to be cut
                         down to make such a beautiful home, and try to reduce your paper/wood usage!"""
        indoorMessage = """Brrrrrr... it sure is cold outside! Remember that your heating elements are consuming
                           a lot of energy, which is certainly making the planet warmer - but not in a good way!
                           Remember to try and use geothermal sources of heating, and to not keep it TOO warm
                           indoors!"""
        bottleMessage = """Ah, I see you drink from bottles like a civilized person! Just remember, these
                           bottles do end up in landfills eventually, and producing them also takes so much
                           energy! Try to switch to reusable bottles, if possible!"""
        ceilingFanMessage = """Wow, a ceiling fan! Good job, thank you for reducing your energy usage! This is
                               definitely much better than using air conditioners to keep yourself cool!"""
        plantMessage = """Hey would you look at that, a plant! Good job, you're making the world a cooler,
                          cleaner, nicer, and more beautiful place! Plants can lower indoor temperatures, absorb
                          carbon dioxide, and overall slow down the pace of climate change! Keep it up!"""
        transportMessage = """We all love to get around! If you have a bike, remember to use it! Get some exercise
                              and keep the world healthy too! Try to avoid cars and other fuel-guzzling monsters,
                              if at all possible!"""
        allInfo = {"Electronics, LCD Screen, TV, Appliance": electricityMessage,
                   "Wood": woodMessage,
                   "Indoors": indoorMessage,
                   "Bottle, Pop Bottle, Shaker": bottleMessage,
                   "Ceiling Fan": ceilingFanMessage,
                   "Flower, Blossom, Plant, Flower Arrangement": plantMessage,
                   "Wheel, Bicycle, Transportation, Vehicle": transportMessage}
        itemsWithInfo = []

        for itemName in names:
            for itemInfo in allInfo:
                if itemName in itemInfo:
                    if allInfo[itemInfo] not in itemsWithInfo:
                        itemsWithInfo.append(allInfo[itemInfo])
                    break

        return render_template("input.html", fooResponse = itemsWithInfo)