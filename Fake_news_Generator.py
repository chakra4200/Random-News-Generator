import random

Area:list = [" in India ","In the United States","in the remote villege","at a secrect lab",
      "in space","in a university","in a tech conference"
      
]

Actions:list = ["Discovered a new technology",
          "banned a popular app",
          "Announced a secrect project",
          "revealed shocking data","lanuched an unexpected product",
          "found a hidden pattern","exposed a major issue"
]

Subjects:list = ["Scientists",
            "Goverment official","A local student",
            "Tech companies","Researchchers",
            "A mysterious group","Experts","A startup" 

]

while True:
   random_area:list = random.choice(Area)
   random_Action:list = random.choice(Actions)
   random_Subjects:list = random.choice(Subjects)

   Headlines:str = f" BREAKING NEWS: {random_Subjects} {random_Action} {random_area} !!"

   print("\n" + Headlines)

   user_input:str = input("Do you want to Generate more Headlines(yes/no)").strip().lower()

   if user_input=="no":
        break
 
print("Thanks for using Our News Detection")


