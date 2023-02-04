# this is the form class for the desktop app
from flet import *
from controls import add_to_control_reference
from button import return_form_button

class AppForm(UserControl):
    def __init__(self):
        super().__init__()

        #makeing it push like the header
    def app_form_input_instance(self):
        add_to_control_reference("AppForm",self)
    
    # some re-usable UI
    def app_form_input_field(self,name:str,expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#999BA9',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(value=name,size=9,color='#F2F2F2',weight=("bold")),
                    TextField(
                        border_color="transparent",
                        height=20,text_size=13,
                        content_padding=0,
                        cursor_color="#F2F2F2",
                        cursor_width=1,
                        cursor_height=18,
                        color="F2F2F2",
                ),
            ],

        ),
    )



    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True,
            height=190,
            bgcolor="#C4D3F0",
            border=border.all(1,"#3F4859"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[self.app_form_input_field("text placeholder*", True)],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("text placeholder*", 3),
                            self.app_form_input_field("text placeholder*", 1),
                            self.app_form_input_field("text placeholder*", 1),
                            self.app_form_input_field("text placeholder*", 1),

                        ],
                        
                    ),
                    Divider(height=1,color="transparent"),
                    

                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button()   
                        ]
                    )
                            
                ],
                        
            ),
        )




