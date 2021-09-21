from PyPDF2 import PdfFileMerger
import os

cur_dir = os.path.dirname(__file__)

pdfs = ['qcm03-01.pdf', 'qcm03-02.pdf', 'qcm03-03.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(os.path.join(cur_dir, pdf))

merger.write(os.path.join(cur_dir, "qcm03.pdf"))
merger.close()