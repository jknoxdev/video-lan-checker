import PySimpleGUI as sg

def create_grid():
    layout = [[sg.Canvas(size=(100, 40), background_color='white', pad=(10, 10), key=f'cell_{i}_{j}') for j in range(4)] for i in range(2)]
    return layout

def on_channel_button_click(channel_count):
    print(f"{channel_count}-channel button clicked.")

sg.theme(None)  # Setting theme to None uses the system default theme

layout = [
    [sg.Text("mpo lux", font=("Arial", 20))],
    [sg.Column(create_grid(), element_justification='center', k='-GRID-')],  # Call create_grid() here and pass the layout
    [
        sg.Button("8-channel", size=(10, 1)),
        sg.Button("12-channel", size=(10, 1)),
        sg.Button("16-channel", size=(10, 1)),
        sg.Button("24-channel", size=(10, 1)),
    ],
    [sg.Text("mpo_lux - v0.01 - author: Justin Knox - aGPL License V3.0", justification='center')]
]

window = sg.Window("mpo lux", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event.startswith('cell_'):
        print(f"Cell clicked: {event}")
    elif event in ["8-channel", "12-channel", "16-channel", "24-channel"]:
        on_channel_button_click(event)

window.close()
