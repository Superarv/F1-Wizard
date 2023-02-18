from flask import Flask, render_template
import f1StatsMain, os

app = Flask(__name__)

def findDriverPfp(driver):
    return f"https://www.formula1.com/content/fom-website/en/drivers/{driver}/jcr:content/image.img.1920.medium.jpg/1670841844162.jpg"

def linkRacePage(race):
    race = race.replace(" ", "_")
    race_classification = f"https://en.wikipedia.org/wiki/{race}#Race_classification"
    return race_classification


@app.route("/")
def homePage():

    return render_template("homePage.html", fds = f1StatsMain.findDriverStat, fdp = findDriverPfp)


@app.route("/<driver>")   
def driver(driver):
    driver = driver.replace("_", " ")
    team = f1StatsMain.findDriverStat(driver, "2023 Team")
    tpc = f1StatsMain.teamPrimaryColor(team)
    tsc = f1StatsMain.teamSecondaryColor(team)
    directory = os.getcwd()
    teamFile = "/static/gradients/" + team.replace(" ", "_") + ".png"
    driverUrlName = driver.lower()
    driverUrlName = driverUrlName.replace(" ", "-")
    driverPfp = f"https://www.formula1.com/content/fom-website/en/drivers/{driverUrlName}/jcr:content/image.img.1920.medium.jpg/1670841844162.jpg"
    driverBDAYList = str(f1StatsMain.findDriverStat(driver, "Birthday")).split()
    driverBDAY = driverBDAYList[0]
    driverBpFlagUrlName = f1StatsMain.findDriverStat(driver, "Nationality").replace(" ", "_")
    driverBpFlagUrl = f'https://www.sciencekids.co.nz/images/pictures/flags680/{driverBpFlagUrlName}.jpg'
    favicon = "/static/icons/" + team.replace(" ", "_") + "-icon.ico"
    DNFpercent = int(f1StatsMain.findDriverStat(driver, "DNF %")) * 1.8
    WDCpercent = int(f1StatsMain.findDriverStat(driver, "WDC %")) * 1.8
    careerPointsWKPD = f'https://en.wikipedia.org/wiki/{driver.replace(" ", "_")}#Complete_Formula_One_results'
    
    return render_template("driverBase.html", driver = driver, fds = f1StatsMain.findDriverStat, tpc = tpc, tsc = tsc, color = "red", teamFile = teamFile, driverPfp = driverPfp, driverUrl = driverUrlName, driverBDAY = driverBDAY, flag = driverBpFlagUrl, favicon = favicon, DNFpercent = DNFpercent, WDCpercent = WDCpercent, lrp = linkRacePage, cpW = careerPointsWKPD)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0.0", port=8080)
