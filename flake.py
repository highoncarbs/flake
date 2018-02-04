#!/usr/bin/env python

from flake.flake import *
import datetime
import os
import errno
import git

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == "--help" or sys.argv[1] == "-h":
      # Print helper function docs
      print('''
        flake v0.1\n
        Padam Sethia <padamsethia5@gmail.com>\n
        Static Site generator written with flask and python.\n
        USAGE:
        \t ./flake.py [FLAGS] [OPTIONS]\n\n
        FLAGS:
        \t -h, --help\t Displays the help section\n
        \t -b, build\t  Freezes to static files at root\n
        \t -n, new\t    New post/page\n
        \t -u, update\t Updates flake from root repository\n
        \t -r, run\t    Runs on local server\n
        OPTIONS:
        \t post\t       Used with new to create a new post\n
        \t port\t       Set desired port number for run\n''')

    # creates local build
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()

    if len(sys.argv) > 1 and sys.argv[1] == "new":
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

    # Update flake from base repo
    if len(sys.argv) > 1 and sys.argv[1] == "update":
        # Needs fixing
        git_dir = "./"
        g = git.cmd.Git(git_dir)
        g.pull()

    if len(sys.argv) > 1 and sys.argv[1] == "run":
        '''
        Runs a local server with website
        '''
        port = int(sys.argv[2])
        flake.run(debug=False , port = port)

    if len(sys.argv) > 1 and sys.argv[1] == "run" and sys.argv[2] == "debug":
        '''
        Runs a local server with website with debug
        '''
        flake.run(debug=True)
