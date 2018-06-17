import argparse
import webbrowser
import binascii


parser = argparse.ArgumentParser(description="Hex2Text v1", epilog="Use -h for help")
parser.add_argument('-e', '--encode', dest='ES', default='', help='String need to encoded')
parser.add_argument('-d', '--decode', dest='DS', nargs='*', default='', help='String need to decode')

args = parser.parse_args()

class Translate:
    def __init__(self):
        self.ES = args.ES
        self.DS = args.DS
        if self.ES=='':
            self.open=True
            self.DS = ''.join(self.DS)
            self.DecodeString(self.DS)
            self.OpenTab(self.result)
        else:
            self.open=False
            self.EncodeString(self.ES)

    def EncodeString(self, ES):
        print (ES.encode('utf-8').hex())

    def DecodeString(self, DS):
        self.result = bytearray.fromhex(self.DS).decode()
        print (bytearray.fromhex(self.DS).decode())

    def OpenTab(self, result):
        opera_path = 'C:/Users/DELL/AppData/Local/Programs/Opera/53.0.2907.68/opera.exe %s --private'
        webbrowser.get(opera_path).open_new_tab(self.result)
        # webbrowser.open_new_tab(result)


if __name__ == '__main__':
    translate = Translate()
