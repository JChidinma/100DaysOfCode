from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from bills.flat import Bill, Flatmate
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultPage(MethodView):
    def post(self):
        # return "Here we will see the results!"
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        # name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)
        days_in_house2 = float(billform.days_in_house2.data)

        bill = Bill(float(amount), period)
        flatmate1 = Flatmate(billform.name1.data, days_in_house1)
        flatmate2 = Flatmate(billform.name2.data, days_in_house2)

        # return f"{flatmate1.name} pays {flatmate1.pays(bill, flatmate2):.2f} {flatmate2.name}"
        return render_template(
            'results.html',
            name1=flatmate1.name,
            amount1=flatmate2.pays(bill, flatmate2),
            name2=flatmate2.name,
            amount2=flatmate2.pays(bill, flatmate1)
        )


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="May 2020")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default="28")

    name2 = StringField("Name: ", default="Bob")
    days_in_house2 = StringField("Days in the house: ", default="28")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule(
    '/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule("/results", view_func=ResultPage.as_view('results_page'))

app.run(debug=True)