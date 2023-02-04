#main class for data table UI
from flet import *
from controls import add_to_control_reference


class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()


# need to send the instance of data table to the dict
    def app_datatable_instances(self):
        add_to_control_reference("AppDataTable",self)


    def build(self):
        self.app_datatable_instances()
        return Row(
            # in order to make the data table control it needs to be configured with certain parametrs
            expand=True,
            controls=[
                DataTable(
                        expand=True,
                        border_radius=8,
                        border=border.all(2,"#0D000D"),
                        # columns args will set the number of columns
                        columns=[
                            DataColumn(
                                Text("text placeholder", size=12, color="#F2F2F2",weight="bold")
                            ),
                             DataColumn(
                                Text("text placeholder", size=12, color="#F2F2F2",weight="bold")
                            ),
                             DataColumn(
                                Text("text placeholder", size=12, color="#F2F2F2",weight="bold")
                            ),
                             DataColumn(
                                Text("text placeholder", size=12, color="#F2F2F2",weight="bold")
                            
                            ),
                            DataColumn(
                                Text("text placeholder", size=12, color="#F2F2F2",weight="bold")
                            
                            ),
                        ],
                        # configurinf the form button to append the data rows

                        rows=[

                        ],
                )


            ],


        )
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
                        "export",
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