#!/usr/bin/env python

from flake.flake import *
import datetime
import os
import errno

if __name__ == '__main__':

    # if len(sys.argv) > 1 and sys.argv[1] == "--help":
    #   # Print helper function docs
    #   pass

    # creates local build
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()

    if len(sys.argv) > 1 and sys.argv[1] == "new" and sys.argv[2] == "post":
        now = datetime.datetime.now()
        now = now.strftime("%-d %b %Y")
        title = str(raw_input("Enter title for the post :  "))
        filename = "./flake/pages/" + title + ".md"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, "w") as f:
            f.write("title: " + title + "\ndate: " + now + "\n\nWrite here.")

    # # Push to github
    # if len(sys.argv) > 1 and sys.argv[1] == "push":
    #   pass

    if len(sys.argv) > 1 and sys.argv[1] == "run":
        '''
        Runs a local server with website
        '''
        flake.run(debug=False)

    if len(sys.argv) > 1 and sys.argv[1] == "run" and sys.argv[2] == "debug":
        '''
        Runs a local server with website with debug
        '''
        flake.run(debug=True)
