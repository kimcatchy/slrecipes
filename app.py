from flask import Flask, render_template
from src.game_info import get_cards, get_recipes

app = Flask(__name__)


@app.route('/')
@app.route('/recipes')
def main_page():
    cards = get_cards()
    cards_by_category = {}
    for card in cards:
        category = cards[card]['category']
        if category in cards_by_category:
            cards_by_category[category].append(cards[card])
        else:
            cards_by_category[category] = [cards[card]]
    return render_template('main_page.jinja', cards=cards_by_category)


@app.route('/recipes/<name>')
def recipes(name=None):
    cards = get_cards()
    create_recipes = get_recipes(output=name)
    return render_template(
        'card_templ.jinja',
        card=cards[name],
        create_recipes=create_recipes
    )


if __name__ == '__main__':
    main_page()
