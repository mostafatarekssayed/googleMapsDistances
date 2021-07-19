from selenium import webdriver
from time import sleep
import os


def find(source_location,destination,sourceLocation,targetLocation,shortestRouteTitle,shortestRouteDistance):
    ROOT_DIR = os.path.dirname(os.path.abspath("chromedriver.exe"))
    driver = webdriver.Chrome(ROOT_DIR)
    sleep(2)
    driver.get("https://www.google.com/maps/dir/" + source_location)
    minDistance = 10000
    minIndex = 0
    routeTitleCol = []
    sleep(10)
    targetLocationInput = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')
    targetLocationInput.send_keys(destination)
    sleep(10)
    searchButton = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]')
    searchButton.click()
    sleep(10)
    routes = driver.find_elements_by_class_name('section-directions-trip-title')
    routes_distances = driver.find_elements_by_class_name('section-directions-trip-distance')
    print(len(routes))
    print(len(routes_distances))
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
    sourceLocation.append(source_location)
    targetLocation.append(destination)
    shortestRouteDistance.append(minDistance)
    shortestRouteTitle.append(routeTitleCol[minIndex])
    dict = {}
    dict["sourceLocation"] = sourceLocation
    dict["targetLocation"] = targetLocation
    dict["shortestRouteDistance"] = shortestRouteDistance
    dict["shortestRouteTitle"] = shortestRouteTitle
    driver.quit()
    return dict

