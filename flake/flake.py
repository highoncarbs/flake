from flask import Flask , render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import sys

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

flake = Flask(__name__)
flake.config.from_object(__name__)
pages = FlatPages(flake)
freezer = Freezer(flake)

@flake.route('/')
def index():
	return render_template('index.html' , pages = pages),200

@flake.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html' , page = page)


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		flake.run(debug=True)
