# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Wordnet(AutotoolsPackage):
    """WordNet is a large lexical database of English. Nouns, verbs, adjectives
    and adverbs are grouped into sets of cognitive synonyms (synsets), each
    expressing a distinct concept. """

    homepage = "https://wordnet.princeton.edu/"
    url      = "http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz"

    version('3.0', sha256='640db279c949a88f61f851dd54ebbb22d003f8b90b85267042ef85a3781d3a52')

    depends_on('tk')
    depends_on('tcl')

    def configure_args(self):
        args = []
        args.append('--with-tk=%s' % self.spec['tk'].prefix.lib)
        args.append('--with-tcl=%s' % self.spec['tcl'].prefix.lib)
        if self.spec.satisfies('^tcl@8.6:'):
            args.append('CPPFLAGS=-DUSE_INTERP_RESULT')

        return args

    def setup_run_environment(self, env):
        env.set('WNHOME', self.prefix)
        env.set('WNSEARCHDIR', self.prefix.dict)
