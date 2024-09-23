import justpy as jp
from webapp import layout
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200  h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type. Let's get started.", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus: border-purple-500 py-2 px-4")
        input_box.on('input', cls.get_definition)

        # jp.Button(a=input_div, text="Get Definition",
        #           classes="border-2 text-gray-500", click=cls.get_definition, outputdiv=output_div, input_box=input_box)

        # jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        print(cls, req)

        return wp

    @staticmethod
    def get_definition(widget, msg):

        widget.outputdiv.text = "Looking up the dictionary..."
        defined = definition.Definition(widget.value).get()

        if defined:
            widget.outputdiv.text = " ".join(defined)
        else:
            widget.outputdiv.text = "Definition not found."
