import justpy as jp


class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200  h-screen")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This home page has an interesting Quasar story. While I develop the story, go for a walk or a run or sip a cup of tea.
        Read about Tailwind CSS: https://tailwindcss.com/
        
        Come back later for the story.
        """, classes="text-lg")
        return wp


# jp.Route(Home.path, Home.serve)
# jp.juspy(port=8001)
