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
	posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
	sorted_posts = sorted(posts, reverse=True,key=lambda page: page.meta['date'])
	return render_template('index.html' , pages = sorted_posts),200

@flake.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html' , page = page)


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "--help":
		# Print helper function docs
		pass
	# creates local build
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()

	# Push to github
	if len(sys.argv) > 1 and sys.argv[1] == "push":
		pass

	else:
		flake.run(debug=True)
