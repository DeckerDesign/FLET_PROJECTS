#this is the header of the desktop appp

#modules
from flet import *
from controls import add_to_control_reference, return_control_reference

# setting the returned dict as variable at top of class

control_map =return_control_reference()

#main class

class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_instance (self):
        #this function sets the class as a key:value
        add_to_control_reference("AppHeader",self)
        #so the key => "appheader"
        #and the value=> self(which is the instances..aka the object in memory)
        
    def show_search_bar(self, e):
        # define the show_search_bar function here
        pass
# created a few of the inner components 
    def app_header_brand(self):
        return Container(
            content=Text("text placeholder ",size=15))

    def app_header_search(self):
        return Container(
            width=320,
            bgcolor='#182E59',
            border_radius=6,
            opacity=0,
            animate_opacity=320,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED,size=17,opacity=0.9),
                    TextField(
                        #basic UI
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="search",
                        #make sure to set the function here 
                        # it should be on_change
                        on_change=lambda e: self.filter_data_table(e),
                    )
                ],
            ),
        )

    def app_header_avatar(self):
        return Container(content=IconButton(icons.PERSON_OUTLINED))
        img = Container(
        on_hover=lambda x: scaleUpImage(x),
        scale=Scale(scale=1.6),
        animate_scale=animation.Animation(800, "bounceOut"),
        content=Image(
            src=f"./INSPECTIONS.png",
            width=250,
            height=220,
        ),
    )
        images = ft.Row(expand=1, wrap=False, scroll="always")

    #now to show the search bar whenever the user hovers over the header
    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            # remove the text when search bar disapears
            self.controls[0].content.controls[1].content.controls[1].value =""
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()

    #final part for this version,2/3/2023 implement some searching and filter

    def filter_data_table(self, e):
        #not the textfield for the search bar has a method that returns the data
        # so filering of table can be done 
        # we call our data map here
        for key,value in control_map.items():
            if key == "AppDataTable":
            # check id the data rows are not empty

                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        #here we loop through the First Column not alll all of them we check to 
                        #to see if the written charater is in the value of each data cell

                        if e.data in data.cells[0].content.controls[0].value.lower():
                            data.visible =True
                            data.update()
                        else:
                            data.visible =False
                            data.update()

 


    def build(self):
        self.app_header_instance ()

        return Container(
            expand=True,
            on_hover=lambda e: self. show_search_bar(e), 
            height=60, 
            bgcolor="#182E59",
            border_radius=border_radius.only(topLeft=15, topRight=15),
            padding=padding.only(left=15,right=15),
            content=Row(
                expand=True,
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                    
                    
                    
                ]
                

            ),
        ) 
    