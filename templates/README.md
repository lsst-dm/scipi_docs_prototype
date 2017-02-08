# scipi_docs_prototype

Prototype for doing docs for the DM code structure (written in reST), these are just for the templates (in branch tickets/DM-8636, subdir 'templates')

If you'd like to see the results, clone the repo, run:

 pip install -r requirements.txt

(This will install Sphinx, Astropy-helpers, Documenteer, and the 'Bootstrap theme' for the docs, if you don't have them already.)

Then build from within the dir using 'make html', and look at it locally in dir: 

   file:///[dir you cloned to]/templates/_build/index.html
