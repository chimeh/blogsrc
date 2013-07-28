#!/bin/sh

PY=python
PELICAN=pelican
PELICANOPTS=
BASEDIR="`pwd`"
INPUTDIR="${BASEDIR}/content"
OUTPUTDIR="${BASEDIR}/../pelican-site-output"
CONFFILE="${BASEDIR}/pelicanconf.py"
PUBLISHCONF="${BASEDIR}/publishconf.py"


#clean:
find ${OUTPUTDIR}/* -maxdepth 0   -name '.git' -prune  -o   -exec rm -rf '{}' ';'

#publish:
	  ${PELICAN} ${INPUTDIR} -o ${OUTPUTDIR} -s ${PUBLISHCONF} ${PELICANOPTS}
      cd ${OUTPUTDIR} && \
      #ls -al
      git add -A
      git commit -m "update document"
      
	 # git checkout  gh-pages
     # rm -rf ${BASEDIR}/*
	 # cp -r ${OUTPUTDIR}/* ${BASEDIR}/
	 # git add -A
	 # git commit -m "update document"
	# git push -v  origin gh-pages:master && \
	# echo -e "更新到服务器成功"
	 # echo -e "checkout 回master"
	 # git checkout master
