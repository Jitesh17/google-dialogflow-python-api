from flask import Flask, request #, jsonify
# from flask_cors import CORS
# import json
app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  query_result = req.get('queryResult')
  direction = query_result.get('parameters').get('direction')
  speed = query_result.get('parameters').get('speed')
  return {
        "fulfillmentText": f'This is from the replit webhook. \ndirection: {direction} \n speed: {speed}',
        "source": 'webhook'
    }

@app.route('/testwebhook', methods=['POST'])
def testwebhook():
  req = request.get_json(silent=True, force=True)
  return {
        "fulfillmentText": 'This is from the replit webhook',
        "source": 'webhook'
    }
   
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
    app.run(host='0.0.0.0', port=1709, ssl_context='adhoc') # This line is required to run Flask on repl.it