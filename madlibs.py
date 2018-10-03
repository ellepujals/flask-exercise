"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliment)

@app.route('/game')
def show_madlib_form():
    """Show user the madlib form."""
    response = request.args.get('yesorno')
    player = request.args.get('person')

    if response == 'yes':
        return render_template("game.html", person=player)
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    
    person = request.args.get('person')
    color = request.args.get('colorchoice')
    noun = request.args.get('nounchoice')
    adjective = request.args.get('adjectivechoice')

    return render_template('madlib.html', person=person,
                            color=color, noun=noun,
                            adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
