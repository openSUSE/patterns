#!/usr/bin/python
# Copyright (c) 2016 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pprint import pprint
import os
import sys
import re
import logging
import cmdln

from translate.storage import po
from fnmatch import fnmatch
from ConfigParser import SafeConfigParser
import solv
import rpm


class Packages2Po(cmdln.Cmdln):
    def __init__(self, *args, **kwargs):
        cmdln.Cmdln.__init__(self, args, kwargs)

    def get_optparser(self):
        parser = cmdln.CmdlnOptionParser(self)
        parser.add_option("--dry", action="store_true", help="dry run")
        parser.add_option("--debug", action="store_true", help="debug output")
        parser.add_option("--verbose", action="store_true", help="verbose")
        return parser

    def postoptparse(self):
        level = None
        if self.options.debug:
            level = logging.DEBUG
        elif self.options.verbose:
            level = logging.INFO

        logging.basicConfig(level=level)

        self.logger = logging.getLogger(self.optparser.prog)
        if level:
            self.logger.setLevel(level)  # wtf?

    def _read_repos(self, repos):
        repodir = '/etc/zypp/repos.d'
        solvfile = '/var/cache/zypp/solv/%s/solv'

        self.pool = solv.Pool()
        self.pool.createwhatprovides()
        self.pool.addfileprovides()

        parser = SafeConfigParser()

        if not repos:
            repos = [f for f in os.listdir(repodir) if fnmatch(f, '*.repo')]
        else:
            repos = [r+'.repo' for r in repos]

        for repofile in repos:
            try:
                name = os.path.splitext(repofile)[0]
                parser.read('/'.join((repodir, repofile)))
                if parser.get(name, 'enabled') == '1':
                    repo = self.pool.add_repo(name)
                    repo.add_solv(solvfile % name)
                    self.logger.debug("add repo %s" % name)
            except Exception, e:
                self.logger.error(e)
                pass

    @cmdln.option("-r", "--repo", dest="repo", action="append",
                  help="repo to use")
    @cmdln.option("-o", "--output", dest="filename",
                  help="output file")
    def do_patterns(self, subcmd, opts, *args):
        """${cmd_name}: generate pot file for patterns

        ${cmd_usage}
        ${cmd_option_list}
        """

        self._read_repos(opts.repo)

# libsolv segfaulting bullshit
#        if len(args):
#            p = str(args[0])
#            print p
#            sel = self.pool.Selection()
#            di = self.pool.Dataiterator(solv.SOLVABLE_NAME, args[0],
#                                        solv.Dataiterator.SEARCH_SUBSTRING|solv.Dataiterator.SEARCH_NOCASE)
#            for d in di:
#                sel.add_raw(solv.Job.SOLVER_SOLVABLE, d.solvid)
#
#            if not sel.isempty():
#                for s in sel.solvables():
#                    print  s

        pofile = po.pofile()

        seen = set()
        for s in self.pool.solvables:
            if s.name.startswith('pattern:'):
                if s.name in seen:
                    continue
                seen.add(s.name)

                def translate(msg):
                    u = po.pounit(encoding="UTF-8")
                    u.addlocation(s.name)
                    u.source = msg
                    u.target = ""
                    pofile.addunit(u)

                translate(s.lookup_str(solv.SOLVABLE_SUMMARY))
                translate(s.lookup_str(solv.SOLVABLE_DESCRIPTION))

        pofile.removeduplicates(duplicatestyle="merge")

        if opts.filename:
            with open(opts.filename, 'w') as fh:
                fh.write(str(pofile))
        else:
            print pofile

    def _readRpmHeader(self, filename):
        """ Read an rpm header. """
        fd = os.open(filename, os.O_RDONLY)
        h = self._readRpmHeaderFD(fd)
        os.close(fd)
        return h

    def _readRpmHeaderFD(self, fd):
        h = None
        try:
            h = self.ts.hdrFromFdno(fd)
        except rpm.error, e:
            if str(e) == "public key not available":
                self.logger.error(str(e))
            if str(e) == "public key not trusted":
                self.logger.error(str(e))
            if str(e) == "error reading package header":
                self.logger.error(str(e))
            h = None
        return h

    @cmdln.option("-o", "--output", dest="filename",
                  help="output file")
    def do_rpm(self, subcmd, opts, *files):
        """${cmd_name}: generate pot file for rpm packages

        ${cmd_usage}
        ${cmd_option_list}
        """

        self.ts = rpm.TransactionSet()
        self.ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES)

        pofile = po.pofile()

        def translate(name, msg):
            u = po.pounit(encoding="UTF-8")
            u.addlocation(name)
            u.source = msg
            u.target = ""
            pofile.addunit(u)

        for f in files:
            try:
                h = self._readRpmHeader(f)
                translate(h['name'], h['summary'])
                translate(h['name'], h['description'])
            except Exception, e:
                self.logger.error("%s: %s"%(f, e))
                pass

        pofile.removeduplicates(duplicatestyle="merge")

        if opts.filename:
            with open(opts.filename, 'w') as fh:
                fh.write(str(pofile))
        else:
            print pofile


if __name__ == "__main__":
    app = Packages2Po()
    sys.exit(app.main())

# vim: sw=4 et
