from selenium import webdriver
from time import sleep
import pandas as pd

def find(source_location,destination,sourceLocation,targetLocation,shortestRouteTitle,shortestRouteDistance):
    # targetLocationFilename = 'Target Locations'
    # driver = webdriver.Chrome("/Users/dinaelhusseiny/Downloads/chromedriver")
    driver = webdriver.Firefox()
    sleep(2)
    driver.get("https://www.google.com/maps/dir/" + source_location)
    minDistance = 10000
    minIndex = 0
    routeTitleCol = []
    routeDetail = []
    sleep(5)
    targetLocationInput = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')
    targetLocationInput.send_keys(destination)
    sleep(5)
    searchButton = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]')
    searchButton.click()
    sleep(5)
    routes = driver.find_elements_by_class_name('section-directions-trip-title')
    routes_distances = driver.find_elements_by_class_name('section-directions-trip-distance')
    for routeTitle in routes:
        routeTitleText = routeTitle.text
        if routeTitleText != '':
            routeTitleCol.append(routeTitleText)
    count = 0
    for routeDistance in routes_distances:
        routeDistanceText = routeDistance.text.replace('km', '')
        routeDistanceInKM = routeDistanceText.replace('كم', '')
        minRouteDistance = float(routeDistanceInKM.strip())
        if minRouteDistance < minDistance:
            minDistance = minRouteDistance
            minIndex = count
        count = count + 1
    print(minIndex)
    print(len(routeTitleCol))
    print(routeDetail)
    try:
        sourceLocation.append(source_location)
        targetLocation.append(destination)
        shortestRouteDistance.append(minDistance)
        shortestRouteTitle.append(routeTitleCol[minIndex])
    except Exception as e:
        print(e)
    dict = {}
    dict["sourceLocation"] = sourceLocation
    dict["targetLocation"] = targetLocation
    dict["shortestRouteDistance"] = shortestRouteDistance
    dict["shortestRouteTitle"] = shortestRouteTitle
    driver.quit()
    return dict

    #

