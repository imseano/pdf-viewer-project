from pypdf import PdfReader

def main():
    print('hello world')
    reader = PdfReader('examples/Example-1.pdf')
    print(reader.get_num_pages())

    pageObj = reader.get_page(0);

    print(pageObj.extract_text());

    im = pageObj.images[0]
    
    im.image.show()


main()
