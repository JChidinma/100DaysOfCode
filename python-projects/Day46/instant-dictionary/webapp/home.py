import justpy as jp
from webapp import layout
from webapp.page import Page


class Home(Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200  h-screen p-2")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This home page has an interesting Quasar story. While I develop the story, go for a walk or a run or sip a cup of tea.
        Read about Tailwind CSS: https://tailwindcss.com/
        
        Come back later for the story.
        """, classes="text-lg")
        return wp
