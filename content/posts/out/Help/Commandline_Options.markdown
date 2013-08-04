title: Commandline Options
date: 2013-08-03
**Output from "zim --help":**

	usage: ./zim.py [OPTIONS] [NOTEBOOK [PAGE]]
	   or: ./zim.py --server [OPTIONS] [NOTEBOOK]
	   or: ./zim.py --export [OPTIONS] NOTEBOOK [PAGE]
	   or: ./zim.py --search NOTEBOOK QUERY
	   or: ./zim.py --index  [OPTIONS] NOTEBOOK
	   or: ./zim.py --plugin PLUGIN [ARGUMENTS]
	   or: ./zim.py --manual [OPTIONS] [PAGE]
	   or: ./zim.py --help
	
	General Options:
	  --gui           run the editor (this is the default)
	  --server        run the web server
	  --export        export to a different format
	  --search        run a search query on a notebook
	  --index         build an index for a notebook
	  --plugin        call a specific plugin function
	  --manual        open the user manual
	  -V, --verbose   print information to terminal
	  -D, --debug     print debug messages
	  -v, --version   print version and exit
	  -h, --help      print this text
	
	GUI Options:
	  --list          show the list with notebooks instead of
	                  opening the default notebook
	  --geometry      window size and position as WxH+X+Y
	  --fullscreen    start in fullscreen mode
	  --standalone     start a single instance, no background process
	
	Server Options:
	  --port          port to use (defaults to 8080)
	  --template      name of the template to use
	  --gui           run the gui wrapper for the server
	
	Export Options:
	  --format        format to use (defaults to 'html')
	  --template      name of the template to use
	  -o, --output    output directory
	  --root-url      url to use for the document root
	  --index-page    index page name
	
	  You can use the export option to print a single page to stdout.
	  When exporting a whole notebook you need to provide a directory.
	
	Search Options:
	  None
	
	Index Options:
	  -o, --output    output file


