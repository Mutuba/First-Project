from flask import Flask
from twilio import twiml
 
# Define our app
app = Flask(__name__)
 
# Define an endpoint to use as the conference room
@app.route('/conference', methods=['POST'])
def voice():
    response = twiml.Response()
    with response.dial() as dial:
        # Let's use the right attribute now.
        dial.conference("Rob's Blog Party")
    return str(response)
 
# Run the app in debug mode on port 5000
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)