from django.shortcuts import render

boroughDict = {
    "City of London": "5E61224",
    "Barking and Dagenham": "5E61400",
    "Barnet": "5E93929",
    "Bexley": "5E93932",
    "Brent": "5E93935",
    "Bromley": "5E93938",
    "Camden": "5E93941",
    "Croydon": "5E93944",
    "Ealing": "5E93947",
    "Enfield": "5E93950",
    "Greenwich": "5E61226",
    "Hackney": "5E93953",
    "Hammersmith and Fulham": "5E61407",
    "Haringey": "5E61227",
    "Harrow": "5E93956",
    "Havering": "5E61228",
    "Hillingdon": "5E93959",
    "Hounslow": "5E93962",
    "Islington": "5E93965",
    "Kensington and Chelsea": "5E61229",
    "Kingston upon Thames": "5E93968",
    "Lambeth": "5E93971",
    "Lewisham": "5E61413",
    "Merton": "5E61414",
    "Newham": "5E61231",
    "Redbridge": "5E61537",
    "Richmond upon Thames": "5E61415",
    "Southwark": "5E61518",
    "Sutton": "5E93974",
    "Tower Hamlets": "5E61417",
    "Waltham Forest": "5E61232",
    "Wandsworth": "5E93977",
    "Westminster": "5E93980",
}

boroughImageDict = {
    "City of London": "https://www.arubanetworks.com/wp-content/uploads/cs-header-city-of-london_1400x350.jpg",
    "Barking and Dagenham": "null",
    "Barnet": "null",
    "Bexley": "null",
    "Brent": "https://www.visitbritain.com/sites/default/files/styles/wysiwyg_image/public/consumer_components_enhanced/highlighted_page/credit_brent_london_borough_of_culture_2020_and_jason_hawkes.png?itok=a-nkb-qB",
    "Bromley": "null",
    "Camden": "https://fullsuitcase.com/wp-content/uploads/2021/10/Colorful-shops-on-Camden-High-Street-in-London.jpg.webp",
    "Croydon": "https://croydon.digital/wp-content/uploads/2020/06/cronx1small-1000x500.jpg",
    "Ealing": "null",
    "Enfield": "null",
    "Greenwich": "https://www.visitgreenwich.org.uk/imageresizer/?image=%2Fdmsimgs%2FGreenwich_Park_1454583505.png&action=ProductDetailProFullWidth",
    "Hackney": "null",
    "Hammersmith and Fulham": "null",
    "Haringey": "null",
    "Harrow": "null",
    "Havering": "null",
    "Hillingdon": "null",
    "Hounslow": "null",
    "Islington": "https://www.marshandparsons.co.uk/wp-content/uploads/2021/08/MAP_Islington_header.jpg",
    "Kensington and Chelsea": "https://www.thebuyingagents.com/wp-content/uploads/2021/05/Buying-Agents-South-Kensington.jpg",
    "Kingston upon Thames": "https://cf.bstatic.com/xdata/images/city/1680x560/969891.jpg?k=5be9ea50f912ed0ef1ec21efc7808dfe62940f1b21577011a56aed23f8c05ec0&o=",
    "Lambeth": "null",
    "Lewisham": "null",
    "Merton": "null",
    "Newham": "null",
    "Redbridge": "null",
    "Richmond upon Thames": "https://www.rogersremovals.co.uk/cupboard/uploads/2019/07/richmond-london.jpeg",
    "Southwark": "https://jobs.theguardian.com/getasset/0891dd2d-2f0c-417f-8fd0-670fd5331250/",
    "Sutton": "null",
    "Tower Hamlets": "https://elba-1.org.uk/wp-content/uploads/2020/07/whitechapel-tower-hamlets.jpg",
    "Waltham Forest": "null",
    "Wandsworth": "null",
    "Westminster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Parliament_at_Sunset.JPG/1024px-Parliament_at_Sunset.JPG",
}

def lowerDict(dict):
    d = {}
    for i in dict:
        d[i.lower()] = i

    return d

lowerDict = lowerDict(boroughDict)

def home(request):
  return render(request, 'index.html')

def results(request):
    inp_value = request.GET.get('results', 'This is a default value').lower()

    try:
        context = {'inp_value': [lowerDict[inp_value]]}
    except:
        possibleBoroughs = []
        for name in lowerDict:
            for word in inp_value.split(" "):
                if (word in name) and (lowerDict[name] not in possibleBoroughs):
                    possibleBoroughs.append(lowerDict[name])
                    
        context = {'inp_value': possibleBoroughs}
                    
    return render( request, 'results.html', context)