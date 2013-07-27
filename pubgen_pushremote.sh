#!/bin/sh

PY=python
PELICAN=pelican
PELICANOPTS=
BASEDIR="`pwd`"
INPUTDIR="${BASEDIR}/content"
OUTPUTDIR="${BASEDIR}/../pelican-site-output"
CONFFILE="${BASEDIR}/pelicanconf.py"
PUBLISHCONF="${BASEDIR}/publishconf.py"

    echo ${PY}
    echo ${PUBLISHCONF}
#clean:
#	[ ! -d ${OUTPUTDIR}  ] || find ${OUTPUTDIR}  -mindepth 1  -delete 
	rm -rf ${OUTPUTDIR}/*
	git add -A
#publish:
	 ${PELICAN} ${INPUTDIR} -o ${OUTPUTDIR} -s ${PUBLISHCONF} ${PELICANOPTS}
	 git checkout  gh-pages
     rm -rf ${BASEDIR}/*
	 cp -r ${OUTPUTDIR}/* ${BASEDIR}/
	 git add -A
	 git commit -m "update document"
	# git push -v  origin gh-pages:master && \
	# echo -e "更新到服务器成功"
	 echo -e "checkout 回master"
	 git checkout master
