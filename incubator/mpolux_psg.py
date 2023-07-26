import PySimpleGUI as sg

num_rows, num_cols = 2, 4  # Initial grid size

def create_grid(num_boxes):
    layout = [[sg.Button('', size=(8, 2), key=f'cell_{i}_{j}', disabled=True) for j in range(num_cols)] for i in range(num_rows)]
    return layout

def clear_grid():
    for i in range(num_rows):
        for j in range(num_cols):
            window[f'cell_{i}_{j}'].update('')

def on_channel_button_click(channel_count):
    global num_rows, num_cols  # Access the global grid size variables
    num_boxes = int(channel_count.split("-")[0])  # Extract the number of boxes from the button text
    clear_grid()
    num_rows = (num_boxes + num_cols - 1) // num_cols  # Calculate the new number of rows
    layout = create_grid(num_boxes)
    window['-GRID-'].update(layout)
    print(f"{channel_count} button pressed.")

sg.theme("Dark")  # Setting theme to None uses the system default theme

layout = [
    [sg.Text("mpo lux", font=("Arial", 20))],
    [sg.Column(create_grid(8), element_justification='center', k='-GRID-')],  # Initial grid with 8 boxes
    [
        sg.Button("8-channel", size=(10, 1)),
        sg.Button("12-channel", size=(10, 1)),
        sg.Button("16-channel", size=(10, 1)),
        sg.Button("24-channel", size=(10, 1)),
    ],
    [sg.Text("mpo_lux - v0.01 - author: Justin Knox - aGPL License V3.0", justification='center')]
]

print("mpo lux application started.")  # Note to the console when the application starts

window = sg.Window("mpo lux", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event.startswith('cell_'):
        print(f"Cell clicked: {event.split('_')[1]}")  # Extract row and column indices and print
    elif event in ["8-channel", "12-channel", "16-channel", "24-channel"]:
        on_channel_button_click(event)

window.close()
