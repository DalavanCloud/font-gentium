#!/usr/bin/python
# this is a smith configuration file

# set the default output folders
out="results"
DOCDIR="documentation"
OUTDIR="installers"
ZIPDIR="releases"
STANDARDS = 'standards'

# set the font name, version, licensing and description
APPNAME="GentiumPlusSIL"
FILENAMEBASE="GentiumPlus"
VERSION="6.000"
TTF_VERSION="6.000"
COPYRIGHT="Copyright (c) 2007-2016, SIL International (http://www.sil.org)"
LICENSE='OFL.txt'

DESC_SHORT = "Unicode font for Roman- and Cyrillic-based writing systems"
DESC_LONG = """
GentiumPlusSIL is a Unicode font for Roman- and Cyrillic-based writing systems
Font sources are published in the repository and a smith open workflow is
used for building, testing and releasing.
"""
DESC_NAME = "GentiumPlus"
DEBPKG = 'fonts-sil-gentium'

import os

# set the build and test parameters

for style in ('-Regular','-Italic') :
    fname = FILENAMEBASE + style
    feabase = 'source/opentype/'+FILENAMEBASE
    font( target = process(fname + '.ttf', name(FILENAMEBASE, lang='en-US', subfamily=(style[1:])),
            cmd('FFchangeGlyphNames -i ../source/psnames ${DEP} ${TGT}')),
        source = create(fname + '-not.sfd', cmd("FFremoveAllOverlaps ${SRC} ${TGT}", ['source/' + fname + '.ufo'])),
        version = VERSION,
        ap =  'source/' + fname +'_ap' + '.xml',
        opentype = fea('source/' + fname + '.fea',
            master = 'source/opentype/' + fname + '_bld.fea',
            make_params="-o 'C L11 L12 L13 L21 L22 L23 L31 L32 L33 C11 C12 C13 C21 C22 C23 C31 C32 C33 U11 U12 U13 U21 U22 U23 U31 U32 U33'",
           depends = (feabase + '_gsub.fea', feabase + style + '_gpos_lkups.fea', feabase + '_gpos_feats.fea', feabase + '_gdef.fea')
            ),
        graphite = gdl('source/' + fname + '.gdl',
            master = 'source/graphite/main.gdh'),
        license = ofl('GentiumPlusSIL','SIL'),
        woff = woff()
        )
