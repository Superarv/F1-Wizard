<h1 align="center" style="font-weight: heavy;"> F1 WIZARD </h1>

##### Finding accurate sports stats can be incredibly tedious, and this is more than true in Formula One. Most people are unable to read the confusing mumbo jumbo of what are racing charts. Therefore, because of these very reasons, I have decided to make F1 Stats available to all, both novice and master, to make this intimidating looking sport inviting to everyone.

##### Hi, I am Atharv Shukla, and I proudly present to you: **F1 Wizard**. F1 Wizard is built around giving its users a high quality experience while they learn more about the various drivers and teams, giving them an accurate way to compare them. 

##### (All of the race statistics in this were updated at the end of the 2022 season, and all the grid information is updated to the start of the 2023 season.)

## Part One: The GUI
##### The GUI (Graphical User Interface), follows popular organizational and visual conventions found in many modern day applications. It builds around a beautiful, modern aesthetic. 

##### For my front-end user interfaces, I used HTML (Hyper-text Markup Language) and CSS (Cascading Stylesheets). These are both very powerful languages that both serve their important roles in developing any web-based application. Below, I have given a few examples of how I used these languages to create my GUI.

##### In the interface, I prioritized user satisfaction by implementing rounded widgets. Here is the code for one of these widget classes:
```css
.personalInfo {
    width: 53%;
    height: 250px;
    background-color: black;
    color: white;
    border-radius: 45px;
    position: relative;
    }
```
##### Inside the widget sample above, there is information pertaining to the driver's personal life, such as Birthday, Birthplace, and Nationality. There is subtext, that introduces the data by labeling it with either 'Birthday', 'Birthplace', or 'Nationality'. The code for the subtext of this specific widget is as follows:
```css
.statSubtext {
    color: gray;
    font-size: 15px;
    position: absolute;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    text-align: center;
    top: 45%;
}
```
##### Underneath that is the maintext, which contains the actually information. For example, it may contain the values of '1990-01-07' or 'London'. The code for this widget's stated maintext is as follows:
```css
.statMainText {
    color: white;
    font-size: 20px;
    position: absolute;
    font-family: Arial, Helvetica, sans-serif;
    text-align: center;
    top: 55%;
}
```
## Part Two: The Data Storage

##### Efficent data collection, storage, and parsing is a big part of my application. With 20 racing drivers, each having participated in a combined thousands of races, each with their own individual statistics, I have quite a lot of data to manage. I worked with the Python programming language, which is known for its extremely powerful data science uses. However, I didn't think I needed to fully utilize this power, as I wasn't going to be needing more than 560 individual data objects. I eventually came down to two solutions, both fairly unconventional in large-scale data engineering. The two solutions were .txt files and .xlsx files. Now, text files have benefits of having all data stored in the same format, and if you think about it, you basically get to write your own rules on how the data is divided. They do, however, have a lack of efficent ways to enter in data without having to mutate the entire file. Excel sheets, on the other hand, are neatly divided into cells that allow for easy addition and subtraction of data, while having the downside of a slightly bigger file size.

##### After careful consideration, however, I came to the conclusion that because I was doing a lot of importing through web-scraping technology, I preferred Excel's .xlsx platform. I was also fortunate that python has a very reliable library that can manage excel files.

##### I made an excel sheet, and got all of the information imported into it, via the web-scraping 'BeautifulSoup' library. Once that was done, I needed to find a way to properly access this data.

## Part Three: The Data Parsing

##### So, first, I made two python dictionaries: One for the rows, and one for the columns. The dictionaries associated every letter and number with it's proper name.

##### Dictionary for Columns/Stats:
```python
columns = {
    "2023 Team" : "B",
    "Debut Race" : "C",
    "Debut Team" : "D",
    "WDCs" : "E",
    "Wins" : "F",
    "Podiums" : "G",
    "Poles" : "H",
    "Grand Slams" : "I",
    "Race Entries" : "J",
    "Highest WDC Standing" : "K",
    "Last Race" : "L",
    "Last Win" : "M",
    "DNFs" : "N",
    "Hatricks" : "O",
    "Current Teammate" : "P",
    "Birthplace" : "Q",
    "Nationality" : "R",
    "Birthday" : "S",
    "Fastest Laps" : "T",
    "Racing Number" : "U",
    "Most Wins In Season" : "V",
    "Seasons" : "W",
    "Career Points" : "X",
    "Win %" : "Y",
    "Grand Slam %" : "Z",
    "DNF %" : "AA",
    "WDC %" : "AB",
    "Birth Nation" : "AC"
}
```
##### and the one for the Rows/Drivers:
```python
rows = {
    "Max Verstappen" : "2",
    "Sergio Perez" : "3",
    "Lewis Hamilton" : "4",
    "George Russell" : "5",
    "Oscar Piastri" : "6",
    "Lando Norris" : "7",
    "Yuki Tsunoda" : "8",
    "Nyck De Vries" : "9",
    "Logan Sargeant" : "10",
    "Alexander Albon" : "11",
    "Pierre Gasly" : "12",
    "Esteban Ocon" : "13",
    "Lance Stroll" : "14",
    "Fernando Alonso" : "15",
    "Carlos Sainz" : "16",
    "Charles Leclerc" : "17",
    "Valtteri Bottas" : "18",
    "Zhou Guanyu" : "19",
    "Kevin Magnussen" : "20",
    "Nico Hulkenberg" : "21"
}
```
##### Then, I made a function that can find the information on any cell, given the desired driver and stat. The function takes both of the inputs, plugs them into their respective dictionaries to find the letter and number of the wanted cell in the worksheet, and then returns the value of its search. This is the most important function in the entire project, because it singlehandedly parses the info for all the webpages.
```python
def findDriverStat(driver, stat):
    cell = columns[stat] + rows[driver]
    return ws[cell].value
```
