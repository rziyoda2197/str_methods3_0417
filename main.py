#1-misol
matn = "Bugun havo yaxshi"
print("yaxshi" in matn)         # Natija: True
# yoki matn.find("yaxshi") != -1

#2-misol
matn = "Men Python o'rganaman"
print(len(matn.split()))        # Natija: 3

#3-misol
matn = "Men Python o'rganaman"
print(matn.replace(" ", ""))    # Natija: MenPythono'rganaman

#4-misol
matn = "salom salom dunyo"
print(matn.replace("salom", "hello", 1))   # Natija: hello salom dunyo

#5-misol
matn = "salom dunyo salom"
print(matn.rfind("salom"))      # Natija: 12
