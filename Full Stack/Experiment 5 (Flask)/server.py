from flask import Flask
app = Flask(__name__)
print("Initialized the app! With a name of: ",__name__)

@app.route('/', methods=['GET']) #there is no need to specify the GET method since it is by default called by flask anyway
@app.route('/home') #you can stack multiple routes onto one function so multiple paths will load the same page
def home():
    print("Hey, I'm visiting the home page!")
    return '''
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous" />
    <h1 style=margin:20>Hello,</h1>
    <p style=margin:20 >world!<p>
    <a href="/important"
        <button type="button" class="btn btn-dark btn-sm mx-3">IMPORTANT</button>
    
    <a href="/mumbai"
        <button type="button" class="btn btn-dark btn-sm mx-3">Mumbai Map</button>
    
    '''

@app.route('/important')
def important():
    print("You have been rick-rolled :>")
    return '''
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
        <button class="btn btn-dark">VERY IMPORTANT LINK</button>
    </a>
    '''
    
@app.route('/aquaman')   
def test():
    return '''<iframe width="560" height="315" src="https://www.youtube.com/embed/FV3bqvOHRQo?si=90_-X-PGhWDitthC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
'''
 

@app.route('/mumbai')
def mumbai():
    print("This is the map of Mumbai!")
    return '''
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2577.196784962171!2d72.83814929293969!3d19.107817486706736!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c9c676018b43%3A0x75f29a4205098f99!2sSVKM&#39;s%20Dwarkadas%20J.%20Sanghvi%20College%20of%20Engineering!5e0!3m2!1sen!2sin!4v1694665308205!5m2!1sen!2sin" width="1920" height="1080" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    '''
    
@app.route('/string/<variable>')
def string(variable):
    return f'''
    <h1>Hi {variable}!</h1>
    <h1>Hi %s!</h1>
''' % variable

@app.route('/int/<int:id>')
def int(id):
    return f'''
    <h1>This POST request has the id: {id}!</h1>
    <h1>This POST request has the id: %d!</h1>
''' % id

@app.route('/float/<float:balance>')
def float(balance):
    return f'''
    <h1>This POST request has the id: {balance}!</h1>
    <h1>This POST request has the id: %f!</h1>
''' % balance


def extra(username):
    return f'''
    <h1>Hi {username}!</h1>
    This is to show how to add a url route to a function using the add_url_rule method.
    <br><br>
    This approach is mainly used in case we are importing the view function from another module.
    '''

app.add_url_rule('/extra/<username>', 'extra', extra) #'extra' is the name assigned to the url route '/extra/<username>' and is used to call the view function extra 

from flask import render_template

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/home2')
def home2():
    return render_template('home2.html')

@app.route('/about')
def about():
    sites = ['https://www.google.com','https://www.youtube.com','https://www.facebook.com']
    return render_template('about.html',sites=sites)

@app.route('/contact/<role>')
def contact(role):
    return render_template('contact.html',person=role)

if __name__ == '__main__':
    print("App is starting...I think?")
    app.run(debug=True, use_reloader=True) #this will autoreload the server on reloading website when you start app using flask run. IF you run each individual .py file with python only then in that case the server automatically reloads every time a change is masde, no need for using auto reloader
    print("Umm...no idea what/how this message will be seen")