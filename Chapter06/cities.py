cities = {"tokyo": {"country": "japan", "population": 9270000, "minimum wage($)": 9.13},
          "shanghai": {"country": "china", "population": 24240000, "minimum wage($)": 2.96},
          "new york": {"country": "united states", "population": 8620000, "minimum wage($)": 15.0},
          }

# print cities with their details
# format is like this:
#
# ---information about Tokyo---
#
# country: Japan
# population: 9270000
# minimum wage($): 9.13
#
for city, info_dir in cities.items():
    print("---information about " + city.title() + "---\n")
    for info, detail in info_dir.items():
        if info == "country":
            print(info + ": " + str(detail).title())
        else:
            print(info + ": " + str(detail))
            
    # go to next line when you finish to print about each city
    print("\n")


        
          
