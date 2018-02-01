#!/usr/bin/env python
from flake.flake import *

if __name__ == '__main__':
	# if len(sys.argv) > 1 and sys.argv[1] == "--help":
	# 	# Print helper function docs
	# 	pass
	# creates local build
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()

	# # Push to github
	# if len(sys.argv) > 1 and sys.argv[1] == "push":
	# 	pass

	else:
		flake.run(debug=True)
