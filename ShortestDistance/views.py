from django.shortcuts import render
import ShortestDistance.PathCalculator as pathCalc
import pandas as pd
# Create your views here.
def index(request):
    return render(request,'index.html')

def ShortestPath(request):
    sourceLocation = []
    targetLocation = []
    shortestRouteTitle = []
    shortestRouteDistance = []

    outputFileName = 'Shortest Distance'
    source_location = request.POST["location"]
    EXCEL = request.POST["excel_path"]
    target_locations = pd.read_csv(EXCEL)
    dataframe = pd.DataFrame

    for target_location in target_locations['Target Locations']:
        dataframe = pathCalc.find(source_location,target_location,sourceLocation,targetLocation,shortestRouteTitle,shortestRouteDistance)

    df = pd.DataFrame(
        {'Source Location': dataframe['sourceLocation'],
         'Target Location': dataframe['targetLocation'],
         'Route Name': dataframe['shortestRouteTitle'],
         'Route Distance': dataframe['shortestRouteDistance']
         })

    # export_file_path = '/Users/dinaelhusseiny/Desktop/WebScraping/Google maps/' + outputFileName + '.csv'
    export_file_path = '/Users/markessam/Documents/python_projects/GoogleMaps/ShortestDistance/' + outputFileName + '.csv'

    df.to_csv(export_file_path, index=False, header=True, encoding='utf-8-sig')
    context = {}
    context["result"] = df.to_html()
    return render(request,'Distances.html',context)

