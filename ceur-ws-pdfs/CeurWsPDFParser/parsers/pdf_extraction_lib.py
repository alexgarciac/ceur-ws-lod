# -*- coding: utf-8 -*-
__author__ = 'Alexander'
import os, codecs, sys

path_to_pdf2txt = os.path.join("{0} {1}".format(sys.executable,os.path.dirname(__file__)), 'pdf2txt.py')

def main():
    f_name = os.path.join("pdfs", "Vol-571-paper1.pdf")
    f_name = r"C:\ITMO\itmove\papers\semPub\pdf_task\pdfs\Vol-315-paper1.pdf"
    print os.path.exists(f_name)

    files = get_html_and_txt(f_name)


    a = 1
def get_html_and_txt(input_filename):
    try:
        out_inf = {
            "html": u"",
            "txt": u"",
        }

        if not os.path.isdir(os.path.join( os.path.dirname(__file__), 'temp_dir') ):
            os.mkdir( os.path.join( os.path.dirname(__file__), 'temp_dir') )

        temp_filename =  os.path.join( os.path.dirname(__file__), 'temp_dir', "1.txt" )
        command = u"{0} -o \"{1}\" \"{2}\"".format(path_to_pdf2txt, temp_filename, input_filename)
        print(command)
        os.system(command)

        fh = codecs.open(temp_filename, 'rb')
        out_inf["txt"] = fh.read(os.path.getsize(temp_filename)).decode("UTF-8")
        fh.close()

        temp_filename =  os.path.join( os.path.dirname(__file__), 'temp_dir', "1.html" )
        command = u"{0} -o \"{1}\" \"{2}\"".format(path_to_pdf2txt, temp_filename, input_filename)
        print(command)
        os.system(command)

        fh = codecs.open(temp_filename, 'rb')
        out_inf["html"] = fh.read(os.path.getsize(temp_filename)).decode("UTF-8")
        fh.close()

    except Exception as err:
        print("get_html_and_txt -> {0}".format(err))
    finally:
        return out_inf
if __name__ == "__main__":
    main()