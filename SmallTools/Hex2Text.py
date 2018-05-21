import argparse
import webbrowser

parser = argparse.ArgumentParser(
    description="Hex2Text v1", epilog="Use -h for help")
parser.add_argument('-e', '--encode', dest='ES',
                    default='', help='String need to encoded')
parser.add_argument('-d', '--decode', dest='DS', nargs='*',
                    default='', help='String need to decode')

args = parser.parse_args()


class Translate(object):
    def __init__(self):
        self.ES = args.ES
        self.DS = args.DS
        if self.ES == '':
            self.open = True
            self.DS = ''.join(self.DS)
            self.DecodeString(self.DS)
            self.OpenTab(self.result)
        else:
            self.open = False
            self.EncodeString(self.ES)

    def EncodeString(self, ES):
        print ES.encode('hex')

    def DecodeString(self, DS):
        self.result = DS.decode('hex')
        print DS.decode('hex')

    def OpenTab(self, result):
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(result)
        # webbrowser.open_new_tab(result)


if __name__ == '__main__':
    translate = Translate()
