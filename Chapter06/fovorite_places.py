favorite_places = {"sen": ["egypt", "vietnam", "japan"], "zhang": ["china", "america", "UK"],
                   "lili": ["brazil", "india", "canada"]}

friend_toppics = ["japan", "canada", "china", "vietnam"]

print("---Each person's favorite places---")
for person, place in favorite_places.items():
    favorite = person.title() + "'s favorite places are: "
    for friend_toppic in friend_toppics:
        if friend_toppic in place:
            favorite+=(friend_toppic.title() + " ")
       
    print(favorite)
                  
