import sublime, sublime_plugin
import codecs
import unicodedata

class CodePointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pos = self.view.sel()[0].begin()
        c = self.view.substr(pos)

        d = [
        ("SJIS:\t\t", "".join([hex(x)[2:] for x in codecs.encode(c, "cp932")]).upper()),
        ("EUC-JP：\t", "".join([hex(x)[2:] for x in codecs.encode(c, "euc_jp", "ignore")]).upper()),
        ("UTF-8：\t\t", "".join([hex(x)[2:] for x in c.encode('utf-8')]).upper()), 
        ("Unicode：\t", hex(ord(c)).upper()[2:])
        ]

        text = "Sample：\t" + c + "\n" \
               "name：\t" + unicodedata.name(c) + "\n\n" \
        	+ "".join([x[0] + "0x" + x[1] + "\n" for x in d])

        sublime.message_dialog(text)
