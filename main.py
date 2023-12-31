from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text= str(int(data["main"]["temp"] - 273.15)))
    pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Codsoft Project")
win.config(bg= "pink")
win.geometry("500x570")

name_label = Label(win, text = "Codsoft Weather App", font = ("Ariel", 30 , "bold"))
name_label.place(x= 25, y= 50, height=50, width=450)

city_name = StringVar()
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combo = ttk.Combobox(win, text = "Codsoft Weather App",values= list_name, font = ("Ariel", 30 , "bold"), textvariable=city_name)
combo.place(x= 25, y = 120 , height= 50, width=450)

w_label = Label(win, text = "Weather climate", font = ("Ariel", 20))
w_label.place(x= 25, y= 260, height=50, width=210)

w_label1 = Label(win, text = "", font = ("Ariel", 20))
w_label1.place(x= 250, y= 260, height=50, width=210)

wb_label = Label(win, text = "Weather Description", font = ("Ariel", 17 ))
wb_label.place(x= 25, y= 330, height=50, width=210)

wb_label1 = Label(win, text = "", font = ("Ariel", 17 ))
wb_label1.place(x= 250, y= 330, height=50, width=210)

temp_label = Label(win, text = "Temperature", font = ("Ariel", 20 ))
temp_label.place(x= 25, y= 400,height=50, width=210)

temp_label1 = Label(win, text = "", font = ("Ariel", 20 ))
temp_label1.place(x= 250, y= 400,height=50, width=210)


pre_label = Label(win, text = "Pressure", font = ("Ariel", 20 ))
pre_label.place(x= 25, y= 470, height=50, width=210)

pre_label1 = Label(win, text = "", font = ("Ariel", 20 ))
pre_label1.place(x= 250, y= 470, height=50, width=210)


done_butt = Button(win, text = "DONE", font = ("Ariel", 20 , "bold"), command=data_get)
done_butt.place(y=190, height= 50, width=100, x=200)


win.mainloop()
