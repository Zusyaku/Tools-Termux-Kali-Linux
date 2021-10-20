from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

plt.style.use('ggplot')

pytrends = TrendReq(hl='en-US')

all_keywords = ['Delivery', 'Food']
keywords = []

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']
cat = '0'
geo = 'US'
gprop = ''

countries = ['india', 'united_states', 'united_kingdom',
             'netherlands', 'brazil']

#Part 1 - Google trends analysis

def check_trends():
    pytrends.build_payload(keywords,
                           cat,
                           timeframes[0],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = round(data.mean(),2)
    avg = round(data[kw][-52:].mean(),2) #Last year average
    avg2 = round(data[kw][:52].mean(),2) #Yearly average of 5 years ago.
    trend = round(((avg/mean[kw])-1)*100,2)
    trend2 = round(((avg/avg2)-1)*100,2)
    print('The average 5 years interest of ' + kw + ' was ' + str(mean[kw]) + '.')
    print('The last year interest of ' + kw + ' compared to the last 5 years'
          + ' has changed by ' + str(trend)+ '%.')
    #Stable trend
    if mean[kw] > 75 and abs(trend) <= 5:
        print('The interest for ' + kw + ' is stable in the last 5 years.')
    elif mean[kw] > 75 and trend > 5:
        print('The interest for ' + kw + ' is stable and increasing in the last 5 years.')
    elif mean[kw] > 75 and trend < -5:
        print('The interest for ' + kw + ' is stable and decreasing in the last 5 years.')

    #Relatively stable
    elif mean[kw] > 60 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is relatively stable in the last 5 years.')
    elif mean[kw] > 60 and trend > 15:
        print('The interest for ' + kw + ' is relatively stable and increasing in the last 5 years.')
    elif mean[kw] > 60 and trend < -15:
        print('The interest for ' + kw + ' is relatively stable and decreasing in the last 5 years.')

    #Seasonal
    elif mean[kw] > 20 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is seasonal.')

    #New keyword
    elif mean[kw] > 20 and trend > 15:
        print('The interest for ' + kw + ' is trending.')

    #Declining keyword
    elif mean[kw] > 20 and trend < -15:
        print('The interest for ' + kw + ' is significantly decreasing.')

    #Cyclinal
    elif mean[kw] > 5 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is cyclical.')

    #New
    elif mean[kw] > 0 and trend > 15:
        print('The interest for ' + kw + ' is new and trending.')

    #Declining
    elif mean[kw] > 0 and trend < -15:
        print('The interest for ' + kw + ' is declining and not comparable to its peak.')

    #Other
    else:
        print('This is something to be checked.')

    #Comparison last year vs. 5 years ago
    if avg2 == 0:
        print('This didn\'t exist 5 years ago.')
    elif trend2 > 15:
        print('The last year interest is quite higher compared to 5 years ago.'
              + ' It has increased by ' + str(trend2)+'%.')
    elif trend2 < -15:
        print('The last year interest is quite lower compared to 5 years ago.'
              + ' It has decreased by ' + str(trend2)+'%.')
    else:
        print('The last year interest is comparable to 5 years ago. '
              + ' It has changed by ' + str(trend2)+'%.')
    
    print('')

##for kw in all_keywords:
##    keywords.append(kw)
##    check_trends()
##    keywords.pop()

#Part 2 - Relative keyword comparison
    
def relative_comparison():
    plt.figure(figsize = (10,8))
    x_pos = np.arange(len(all_keywords))

    #Last 5-years
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[0],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100,2)
    ax1 = plt.subplot2grid((3,2), (0,0), rowspan = 1, colspan = 1)
    ax2 = plt.subplot2grid((3,2), (0,1), rowspan = 1, colspan = 1)
    for kw in all_keywords:
        ax1.plot(data[kw], label = kw)
    ax2.bar(x_pos, mean, align = 'center')
    plt.xticks(x_pos, all_keywords)

    #Last 12-months
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[1],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100,2)
    ax3 = plt.subplot2grid((3,2), (1,0), rowspan = 1, colspan = 1)
    ax4 = plt.subplot2grid((3,2), (1,1), rowspan = 1, colspan = 1)
    for kw in all_keywords:
        ax3.plot(data[kw], label = kw)
    ax4.bar(x_pos, mean, align = 'center')
    plt.xticks(x_pos, all_keywords)

    #Last 3-months
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[2],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100,2)
    ax5 = plt.subplot2grid((3,2), (2,0), rowspan = 1, colspan = 1)
    ax6 = plt.subplot2grid((3,2), (2,1), rowspan = 1, colspan = 1)
    for kw in all_keywords:
        ax5.plot(data[kw], label = kw)
    print(mean)
    ax6.bar(x_pos, mean[0:len(all_keywords)], align = 'center')
    plt.xticks(x_pos, all_keywords)

    ax1.set_ylabel('Last 5 years')
    ax3.set_ylabel('Last year')
    ax5.set_ylabel('Last 3 months')
    ax1.set_title('Relative interest over time', fontsize = 14)
    ax2.set_title('Relative interest for the period', fontsize = 14)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%m-%y'))
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
    ax1.legend()
    ax3.legend()
    ax5.legend()
    plt.show()
    

##relative_comparison()

#Part 3 - Interest per region
def int_per_reg():
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[1],
                           geo,
                           gprop)
    
    data = pytrends.interest_by_region(resolution = 'DMA',
                                inc_low_vol = True,
                                inc_geo_code = True)
    for kw in all_keywords:
        print(kw)
        data = data.sort_values(by = kw, ascending = False)
        print(data.head())
        print('')

##int_per_reg()
    
#Part 4 - related queries summary
def rel_queries():
    #Last 3-months related queries
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[2],
                           geo,
                           gprop)

    data = pytrends.related_queries()
    print('Last 3 months related queries.')
    for kw in all_keywords:
        print(kw + ' top queries:')
        if data[kw]['top'] is None:
            print('There isn\'t enough data.')
        else:
            print(data[kw]['top'].head(3))
        print('')
        print(kw + ' rising queries:')
        if data[kw]['rising'] is None:
            print('There isn\'t enough data.')
        else:
            print(data[kw]['rising'].head(3))
        print('')

    #Last month related queries
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[3],
                           geo,
                           gprop)

    data = pytrends.related_queries()
    print('Last month related queries.')
    for kw in all_keywords:
        print(kw + ' top queries:')
        if data[kw]['top'] is None:
            print('There isn\'t enough data.')
        else:
            print(data[kw]['top'].head(3))
        print('')
        print(kw + ' rising queries:')
        if data[kw]['rising'] is None:
            print('There isn\'t enough data.')
        else:
            print(data[kw]['rising'].head(3))
        print('')
    

##rel_queries()

#Part 5 - Trending searches
def trending_searches(country):
    data = pytrends.trending_searches(country)
    print(data.head(5))

for country in countries:
    print(country)
    print('')
    trending_searches(country)
    print('')


