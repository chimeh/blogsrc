PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/../pelican-site-output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/


SSH_HOST=git@github.com
SSH_PORT=22
SSH_USER=jimagile@gmail.com
SSH_TARGET_DIR=hmean/hmean.github.com.git

DROPBOX_DIR=~/Dropbox/Public/

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   ssh_upload                       upload the web site via SSH        '
	@echo '   rsync_upload                     upload the web site via rsync+ssh  '
	@echo '   dropbox_upload                   upload the web site via Dropbox    '
	@echo '   ftp_upload                       upload the web site via FTP        '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '                                                                       '


newrepo:allclean publish
#delete all
#[ ! -d $(OUTPUTDIR)  ] || find $(OUTPUTDIR)  -mindepth 1  -delete 
#${PELICAN} ${INPUTDIR} -o ${OUTPUTDIR} -s ${PUBLISHCONF} ${PELICANOPTS} #make publish
#publish
	cd ${OUTPUTDIR} && \
	pwd && \
	git init && \
	git add -A && \
	git commit -m "first update document" && \
	git remote add origin $(SSH_HOST):$(SSH_TARGET_DIR) && \
	git remote -v && \
	echo -e "init git at `pwd` \n and add remote origin $(SSH_HOST):$(SSH_TARGET_DIR)"

html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

#clean all ,include .git
allclean:
	[ ! -d $(OUTPUTDIR)  ] || find $(OUTPUTDIR)  -mindepth 1  -delete 

#clean all but  .git
clean:
	touch $(OUTPUTDIR)/nothing
	find ${OUTPUTDIR}/* -maxdepth 0   -name '.git' -prune  -o   -exec rm -rf '{}' ';'
#[ ! -d $(OUTPUTDIR)  ] || find $(OUTPUTDIR)  -mindepth 1 -name '.git' -prune -o  -exec rm -rf '{}' ';' # funtion same as clean

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server

devserver:
	$(BASEDIR)/develop_server.sh restart

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR) $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

#add by jim
dev_push: clean
	git checkout dev
	git add -A
	git commit -v

github: clean publish
#find ${OUTPUTDIR}/* -maxdepth 0   -name '.git' -prune  -o   -exec rm -rf '{}' ';' #the funtion same as clean
	cd ${OUTPUTDIR} && \
	echo -e "now in path:`pwd`" && \
	git add -A && \
	git commit -m "update document" && \
	git push -v origin master master && \
	echo "finish"
	
.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload github newrepo clean
