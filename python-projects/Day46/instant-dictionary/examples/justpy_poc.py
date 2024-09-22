import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bp-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a=wp, placeholder="Enter first value",
                    classes="form-input")
    in_2 = jp.Input(a=wp, placeholder="Enter second value",
                    classes="form-input")

    d_output = jp.Div(a=wp, text="Result goes here...",
                      classes="text-gray-600")
    jp.Div(a=wp, text="Just another div", classes="text-gray-600")
    jp.Div(a=wp, text="Yet another div", classes="text=gray-600")
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.QBtn(a=div2, color="seconday", label="primary",
            icon="map", text="Calculate", d=d_output)
    jp.Div(a=div2, text="I am a cool interactive div!", mouseenter=mouse_enter,
           mouseleave=mouse_leave, classes="hover:bg-red-500")
    return wp

    jp.Button(a=wp, text="Calculate")

    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello World", classes="text-green-100")
    jp.Div(a=wp, text="Hello World Again")
    return wp


def sum_up(widget, msg):
    sum = float(widget.in_1.value) + float(widget.in_2.value)
    widget.d.text = sum


def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house!"


def mouse_leave(widget, msg):
    widget.text = "A mouse left!"


# @jp.SetRoute("/about")
# def about():
#     wp = jp.WebPage()
#     jp.Input(a=wp, placeholder="Enter first value", classes="form-input")
#     jp.Input(a=wp, placeholder="Enter second value", classes="form-input")

#     # jp.Div(a=wp, text="Result goes here..", classes="text-blue-900 bg-yellow-500")
#     jp.Div(a=wp, text="Result goes here...")
#     jp.Button(a=wp, text="Calculate")
#     return wp

# jp.Route("/", home)


jp.justpy()
