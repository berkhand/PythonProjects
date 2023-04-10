import turtle
import pandas
from city_name_writer import Writer

screen = turtle.Screen()
screen.title('Turkish cities game')
screen.setup(width=1600, height=750)
screen.tracer(0)

image = "1600px-Turkey_provinces_blank_gray.gif"
screen.addshape(image)
turtle.shape("blank")
turtle.shape(image)

# def get_mouse_click_coordinates(x, y):
#     print(f"{x},{y}")
#
# turtle.onscreenclick(get_mouse_click_coordinates)

data = pandas.read_csv("sehirler.csv")
sehir_list = data.sehir.to_list()
w = Writer()

number_of_cities = len(data)
cities_guessed = []
is_game_on = True

first = True
screen.update()
while len(cities_guessed) <= number_of_cities:
    if first:
        answer_state = screen.textinput(title="Guess the city!", prompt="Choose the next city!").title()
        first = False
    else:
        answer_state = screen.textinput(title=f"{len(cities_guessed)}/{number_of_cities} cities correct!", prompt="Choose the next city!").title()

    # row = data[data.sehir.str.lower() == answer_state.lower()]
    # len(row) > 0
    # print(data.sehir.to_list())

    if answer_state == "Exit":
        cities_to_learn = [city for city in sehir_list if city not in cities_guessed]
        df = pandas.DataFrame(cities_to_learn)
        df.to_csv("cities_to_learn.csv", index=False)

    if answer_state in sehir_list:
        selected_data = data[data.sehir == answer_state]
        x = int(selected_data.x)
        y = int(selected_data.y)
        # w.write_name(row.sehir.to_string(header=False, index=False), int(row.x), int(row.y))
        w.write_name(selected_data.sehir.item(), x, y)
        if answer_state not in cities_guessed:
            cities_guessed.append(answer_state)


turtle.mainloop()
