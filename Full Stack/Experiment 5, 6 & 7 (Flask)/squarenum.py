from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/sqGET',methods=['GET'])
def squarenumberGET(): #Changing the url and then geting the data out of that url
    # If method is GET, check if  number is entered or user has just requested the page.
    # Calculate the square of number and pass it to answermaths method
    if request.method == 'GET':
        # If 'num' is None, the user has requested page the first time
        if(request.args.get('num') == None):
            return render_template('squarenumGET.html')
          # If user clicks on Submit button without entering number, display error
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
          # User has entered a number
          # Fetch the number from args attribute of request accessing its 'id' from HTML
            number = (request.args.get('num'))
            
            print(number)
            sq = int(number) * int(number)
            
            # pass the result to the answer HTML
            # page using Jinja2 template
            return render_template('answer.html',
                                   squareofnum=sq, num=number)
            
            
@app.route('/sqPOST',methods=['GET','POST'])
def squarenumberPOST():#No change in url, data is gotten from from POST request sent
    # If method is POST, get the number entered by user
    # Calculate the square of number and pass it to answermaths
    if request.method == 'POST':
        if(request.form['num'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html',
                            squareofnum=sq, num=number)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("squarenumPOST.html")


if __name__ == '__main__':
    app.run(debug=True)