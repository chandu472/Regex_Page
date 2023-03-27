from flask import Flask, render_template, request
import re

app = Flask(__name__)

################################################
# Route 1
@app.route('/')
def home_fun():
    return render_template('regex.html')

# Route 2
@app.route('/match', methods=['POST', 'GET'])
def match_fun():

    if request.method == 'POST':
        test_string = request.form.get('test_string')
        regex_pattern = request.form.get('pattern')

        matched_strings = re.findall(regex_pattern, test_string)

        if matched_strings:
            output = "Matched strings:\n"
            for string in set(matched_strings):
                count = matched_strings.count(string)
                output += f"{string}: {count} time(s)\n"
        else:
            output = "No matched strings found."

        return render_template('regex.html', output=output)

    return render_template('regex.html')

###############################################

if __name__ == '__main__':
    app.run(debug=True)
