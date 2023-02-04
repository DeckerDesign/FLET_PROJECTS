# this is the maon file wher we can create the button for the application

from flet import *
from controls import return_control_reference
from form_helper import FormHelper

#get the global map
control_map = return_control_reference()


def update_text(e):
    # here if the user double clicks the cells it can be editable.

    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

# this method will handle the main data from the user
#and displaying it 

def get_input_data(e):
    # recall that ther form is saved in decitionary
    for key,value in control_map.items():
        #get the key called appform since its there the value is chilling
        if key == 'AppForm':
            #get the keys create a datarow
            data = DataRow(cells=[])
            #once it has the key, we can loop over the text field and get the values
            #first row
            for user_input in value.controls[0].content.controls[0].controls[:]:
                # here we can apphend that DataRow
                data.cells.append(

                    #call form class
                    #class need a hug remember to wrap it up just like safe sex its important 
                    DataCell(FormHelper(user_input.content.controls[1].value),
                    #the data can now in some importants events namely tap events/click event
                    on_double_tap=lambda e: update_text(e),
                    )
                )
                    
            #second row
            for user_input in value.controls[0].content.controls[1].controls[:]:
                data.cells.append(
                    #call form class
                    DataCell(FormHelper(user_input.content.controls[1].value),
                    on_double_tap=lambda e: update_text(e),
                    )
                )
            #cells to insert the sweet data boy
        if key =="AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()
        

#for the button ui, this can be changed to fit the application theme
def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor="#3D79F2",
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,

                    ),
                    Text(
                        "add input field to Table",
                        size=11,
                        weight="bold",

                    ),

                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),

                },
                color={
                    "":"white",

                },
            ),
            height=42,
            width=220,
        
        )
    )
