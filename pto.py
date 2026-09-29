from flask import Flask, request, jsonify
import re
app = Flask(__name__)
#list of patterns
block_patterns = [
    r'ignore.previous', r'act as.*(hacker|murderer|admin|malicious|attacker)',
    r'bypass.*security', r'secret.*key', r'system.*prompt',r'jailbreak',r'dan.*mode',r'do anything now',r'ignore.*instructions',r'break.*character',r'act as.*unfiltered',r'override.*safety',r'pretend.*malicious',r'reveal.*prompt',r'exfiltrate.*data' 
]
#creating the route for checking prompts
@app.route('/check', methods=['GET','POST'])
#func def of the prompt checking method
def check_prompt():
    prompt = request.json.get('prompt', '')
    if any(re.search(p, prompt, re.IGNORECASE) for p in block_patterns): #searches for if patterns are found
        return {'safe': False, 'reason': 'injection_detected'}
    return {'safe': True}
#checking visibility of the webapi called at root
@app.route('/')
def home():
    return "LLM Safety Gateway is running. Use POST /check"

#Running the service
if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
#END
















