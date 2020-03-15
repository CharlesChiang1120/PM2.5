
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=18' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=43' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=8' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=12' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=73' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=76' width='320px' height='380px' scrolling='yes'></iframe><iframe src='https://airtw.epa.gov.tw/AirQuality_APIs/WebWidget.aspx?site=92' width='320px' height='380px' scrolling='yes'></iframe>"


app.run()
