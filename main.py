#on this episode of dragonball-z we test
# if flet will be the answer

#########Modules############
import flet as ft
from flet import *
from header import AppHeader #application header file is header.py
from functools import partial
import time
from form import AppForm #application input form 
from data_table import AppDataTable #application data table
#from export import export
#from sidebar import ModernNavBar
######end of modules########
def main(page: ft.Page):
    # add/update controls on Page still testin opacity think this is the color though
    page.bgcolor = "#3F4859"
    page.window_opacity = 1
    page.padding = 20
    page.add(
        # main column where each app component will be placed
        Column(
            expand=True,
            controls=[
                #class instance live here
               AppHeader(),
               Divider(height=2,color="transparent"),
               AppForm(),
               #we call the data table inside the column 
               Column(scroll='hidden',expand=True,controls=[AppDataTable()]),
               #ModernNavBar(),
               #export(),
            ],
        )
    )
    page.update()
    
    pass
if __name__ == "__main__":
#this how you end the app notie its ft not flet
    ft.app(target=main)
