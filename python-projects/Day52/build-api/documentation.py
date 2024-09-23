import justpy as jp


class Doc:
    path = "/doc"

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200  h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.instant-dictionary.com/api?w=moon",
               classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "moon", "definition": ["moon","A natural satellite of a planet."
"moon","A month, particularly a lunar month (approximately 28 days)."
"moon","To fuss over adoringly or with great affection."
"moon","Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate)."
"moon","To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."
"stave","A series of (usually five) horizontal lines on which musical notes are written."] }
        """)

        return wp
