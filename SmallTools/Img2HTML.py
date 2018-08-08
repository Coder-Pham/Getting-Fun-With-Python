from PIL import Image
import time

def hexcode(r, g, b):
    return '%02x%02x%02x' % (r, g, b)


if __name__ == '__main__':
    File = input('Enter Image file name: ')
    
    # Count time
    print('Processing Image, please wait !')
    second = time.time()

    img = Image.open(File)
    img.rotate(90)
    width, height = img.size

    content = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Image2HTML</title>
</head>

<body>
    <style>
        table tr td {
            display: table-cell;
            margin: 0cm;
            padding: 0cm;
        }

        table {
            border-spacing: 0;
            border: 0cm;
        }
    </style>

    <table cellpadding='0' cellspacing='0' >
    '''

    for x in range(width):
        content += '<tr>'        # New row
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Add 1 pixel with td
            content += '<td width=1 height=1 bgcolor="#' + \
                hexcode(r, g, b) + '"></td>\n'
        content += '</tr>\n'

    content += '</table></body></html>'

    with open('Img2HTML.html', 'w') as result:
        result.write(content)

    print('Done with {:0.2f}s'.format(time.time() - second))