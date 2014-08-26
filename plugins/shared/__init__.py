#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from bottle import Bottle, HTTPError #, post, get, response # route, get, run, template, static_file, request
# from base64 import b64encode
from mimetypes import MimeTypes
from urllib import quote

class Shared(Bottle):
    def __init__(self, application, path):
        Bottle.__init__(self)
        self._application = application
        self._path = path
        self._mimeTypes = MimeTypes(['plugins/shared/mime.types'], strict=False)

        self.get('/files/')(self.shared)
        self.get('/files/<filepath:path>')(self.shared)
        self.get('/')(self.files)
        self.get('/<filepath:path>')(self.files)

    def getHTML(self):
        s = """<h2>Upload</h2>
        <form method="POST" action="#" type="multipart">
            <input type="file" value="file">
            <input type="submit" value="Send" class="button">
        </form>
        <h3><a href="/shared/files/">Browse Files -&gt;</a></h3>"""
        return s

    def files(self, filepath = '/'):
        return static_file(filepath, root='plugins/shared/www/')

    def shared(self, filepath = b''):
        ROOT = b'./plugins/shared/files'
        if os.path.isfile(os.path.join(ROOT, filepath)):
            return static_file(filepath, root=ROOT)

        if not(os.path.isdir(os.path.join(ROOT, filepath))):
            raise HTTPError(404, 'Unknown file ou directory {}.'.format(quote(filepath)))

        try:
            repName = unicode(filepath, 'utf-8')
        except:
            try:
                repName = unicode(filepath, 'latin-1')
            except:
                repName = unicode(filepath, 'utf-8', 'replace')
        if repName == '': repName = '/'
        s = """\
<h2><!--data-l10n-id="shared_index_of"-->Index of {0}</h2>
<div class="list">
    <table summary="Directory Listing" cellpadding="0" cellspacing="0"><!-- data-l10n-id="shared_dir_listing" -->
        <thead>
            <tr data-l10n-id="shared_headers">
                <th class="n">Name</th>
                <th class="m">Last Modified</th>
                <th class="s">Size</th>
                <th class="t">Type</th>
            </tr>
        </thead>
        <tbody>
""".format(repName)

# if top level => don't propose "Parent dir"
        if not(filepath):
            s = s + """\
            <tr>
                <td class="n"><a href="../" data-l10n-id="shared_parent_dir">Parent Directory</a>/</td>
                <td class="m">&nbsp;</td>
                <td class="s">- &nbsp;</td>
                <td class="t">Directory</td>
            </tr>
"""

        def fileSort(f1, f2):
            file1 = os.path.join(ROOT, filepath, f1)
            file2 = os.path.join(ROOT, filepath, f2)
            if os.path.isdir(file1) and not(os.path.isdir(file2)): return -1
            if not(os.path.isdir(file1)) and os.path.isdir(file2): return 1
            if str(f1).upper() < str(f2).upper(): return -1
            if str(f1).upper() > str(f2).upper(): return 1
            return 0

        def sizeUnit(size):
            i = 0
            while (size >= 2000):
                 size = size / 1024.0
                 i = i + 1
            if i == 1: return "{:.2f}k".format(size)
            elif i == 2: return "{:.2f}M".format(size)
            elif i == 3: return "{:.2f}G".format(size)
            elif i == 4: return "{:.2f}T".format(size)
            return str(size)

# for each file or dir (or link or whatever)
        for name in sorted(os.listdir(os.path.join(ROOT, filepath)), fileSort):
            file = os.path.join(ROOT, filepath, name)
            date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%c')
            if os.path.isdir(file):
                url, type, size = quote(b'/shared/files/' + filepath + name + b'/'), 'Directory', "-"
            elif os.path.isfile(file):
                type, comp = self._mimeTypes.guess_type(name)
                if type == None: type = 'File'
                url, size = quote(b'/shared/files/' + filepath + name), sizeUnit(os.path.getsize(file)) + 'B'
            else:
                url, type, size = quote(b'/shared/files/' + filepath + name), "-", sizeUnit(os.path.getsize(file)) + 'B'

            try:
                fileName = unicode(name, 'utf-8')
            except:
                try:
                    fileName = unicode(name, 'latin-1')
                except:
                    fileName = unicode(name, 'utf-8', 'replace')

            s = s + """\
            <tr>
                <td class="n"><a href="{0}">{1}</a></td>
                <td class="m">{2}</td>
                <td class="s">{3}</td>
                <td class="t">{4}</td>
            </tr>
""".format(url, fileName, date, size, type)
        s = s + """\
        </tbody>
    </table>
</div>
"""
        return self._application.pageTemplate(content = s)



    def getTopNav(self):
        return """<a href="/shared/files/" title="Click to see all shared files..." data-l10n-id="shared_menu">Files</a>"""
				
    def getLocales(self):
        return "/shared/{{locale}}/strings.l20n"        

def factory(application, options):
    sh = Shared(application, '/shared')
    return sh