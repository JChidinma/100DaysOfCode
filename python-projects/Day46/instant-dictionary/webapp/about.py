import justpy as jp
from webapp import layout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200  h-screen")
        jp.Div(a=div, text="This is the About Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This about page has an interesting Quasar story. Before we get to the story, let's get me show you where to ge the documentation for this 'Beyond the Framework' framework.
        https://quasar.dev/. Come back later for the story.
        """, classes="text-lg")
        return wp
