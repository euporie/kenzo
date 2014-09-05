from __future__ import print_function
import urllib.request
import json
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from datetime import datetime



def lovechart(api='4srgf38o',key='52eed60d426356ee3dc0fe967d50b6ab'):
    url='https://www.kimonolabs.com/api/'+api+'?apikey='+key+'&kimseries=1'
    #url = 'https://www.kimonolabs.com/api/641sxm9c?apikey=52eed60d426356ee3dc0fe967d50b6ab&kimseries=1'
    # result = json.loads(urllib.request.urlopen(url).readall().decode('utf-8')) #downloads the json file and parses it
    print(url)
    result = json.loads(urllib.request.urlopen(url).readall().decode('utf-8'))
    #print(result['results']['collection1'][0]['property1'][4]['d'])
    dictionary = dict()
    days = list()
    prop=list(result["results"]["collection1"][0].keys())[0]
    for entry in result['results']['collection1'][0][prop]:  #goes through each day in week

        #print (result['results']['collection1'][0]['property1'][i]['d'])
        #date=datetime.strptime(result['results']['collection1'][0]['property1'][i]['d'], '%Y-%m-%dT%H:%M:%S.%fZ') #converts from string to datetime object and stores it in a list
        date = datetime.strptime(entry['d'], '%Y-%m-%dT%H:%M:%S.%fZ')
        days.append(date)
        #print vars(date)
        dictionary[date] = entry['v']  #stores the date and coresponding value in a dictionary

    days.sort()  #sorts the list of dates
    values = list()

    for day in days:  #appends values corresponding to each day in order to a list
        values.append(dictionary[day])

    fig, ax = plt.subplots()  #creates a figure and returns it along with axis.
    plt.title(result['name'])



    ax.plot(days, values, 'g-', linewidth=5)  #plots the values against dates
    fig.autofmt_xdate()  #auto formats dates displayed along the x axis
    fig.set_size_inches(10,10)

    outtext=(str(result['name'])+'.png')
    outtext2=outtext.replace(" ", "").replace("-", "")
    print(outtext2)
    plt.savefig(outtext2,
                facecolor=(0.713, 0.803, 0.901),
                edgecolor=(0.713, 0.803, 0.901),
                dpi=100
    )  #displays the plot.

    return outtext2

