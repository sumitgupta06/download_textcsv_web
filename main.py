from urllib import request
# other way to import modules


def download_csv_text(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")  # split is used to seperate lines \\n would leave space after every line
    destination = r'dest.csv'
    fw = open(destination, 'w')
    for i in lines:
        fw.write(i + "\n")
    fw.close()


download_csv_text('''here comes the url of file''')

