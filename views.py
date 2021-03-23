def product_chart(request):
   
    dataSource = OrderedDict()
    mapConfig = OrderedDict()
    mapConfig["caption"] = "Product Information"
    mapConfig["includevalueinlabels"] = "1"
    mapConfig["labelsepchar"] = ":"
    mapConfig["entityFillHoverColor"] = "#808080"
    mapConfig["theme"] = "fusion"
    colorDataObj = {"minvalue": "0", "code": "#eeccff", "gradient": "1",
                    "color": [
                        {"minValue": "0.0", "maxValue": "1.0", "code": "#e6b3ff"},
                        {"minValue": "1.0", "maxValue": "10.0", "code": "#dd99ff"},
                        {"minValue": "10.0", "maxValue": "50.0", "code": "#d580ff"},
                        {"minValue": "50.0", "maxValue": "100.0", "code": "#cc66ff"},
                        {"minValue": "100.0", "maxValue": "200.0", "code": "#c44dff"},
                        {"minValue": "200.0", "maxValue": "300.0", "code": "#bb33ff"},
                        {"minValue": "300.0", "maxValue": "400.0", "code": "#b31aff"},
                        {"minValue": "400.0", "maxValue": "500.0", "code": "#aa00ff"},
                        {"minValue": "500.0", "maxValue": "600.0", "code": "#9900e6"},
                        {"minValue": "600.0", "maxValue": "700.0", "code": "#8800cc"},
                        {"minValue": "700.0", "maxValue": "800.0", "code": "#148ea1"},
                        {"minValue": "800.0", "maxValue": "900.0", "code": "#660099"},
                        {"minValue": "900.0", "maxValue": "1000.0", "code": "#550080"},
                    ]
                    }
    data = []
    dict = {
        "001": "Andaman and Nicobar Islands", "002": "andhra pradesh", "003": "Arunachal Pradesh", "004": "assam",
        "005": "bihar", "006": "chandigarh", "007": "chattisgarh", "008": "dadra & nagar haveli", "009": "daman & diu",
        "010": "delhi", "011": "goa", "012": "gujarat", "013": "haryana", "014": "himachal pradesh",
        "015": "jammu & kashmir", "016": "jharkhand", "017": "karnataka", "018": "kerala", "019": "Lakshadweep",
        "020": "madhya pradesh", "021": "maharashtra", "022": "manipur", "023": "meghalaya", "024": "mizoram",
        "025": "nagaland", "026": "odisha", "027": "pondicherry", "028": "punjab", "029": "rajasthan", "030": "Sikkim",
        "031": "tamil nadu", "032": "tripura", "033": "uttar pradesh", "034": "uttarakhand", "035": "west bengal",
        "036": "telangana"
    }
    product_dict = {}
    final_product_dict = {}
    for index, state in dict.items():
        product_count = 0
        product_name = ""
        check_state = OrderDetails.objects.filter(address__state__icontains=state).exclude(
            status="initiated").values_list("order_id", flat=True)
        if check_state:
            product_details_list = Order.objects.filter(id__in=check_state).exclude(status="initiated").values_list(
                "product_details__product_id__name", flat=True)
            product_count_dict = Counter(product_details_list)
           
 	    if product_count_dict:
		  product_name = list(product_count_dict.keys())[0]
		  product_count = list(product_count_dict.values())[0]
   	    else:
	          product_name = str(0)
	          product_count = 0

        data_dict = {
            "id": index,
            "value": product_count,
        }
        data.append(data_dict)

        product_dict.update({
            state: [product_count, product_name]

        })
    k = Counter(product_dict)
    high = k.most_common(10)
    for i in high:
        final_product_dict.update({
            i[0]: i[1]
        })

    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = data
    fusionMap = FusionCharts("maps/india", "ex1", "400", "600", "chart-1", "json", dataSource)
    return render(request, 'map.html', {'output': fusionMap.render(), 'data': final_product_dict})

