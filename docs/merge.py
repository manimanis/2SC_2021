# pip install pypdf2
from PyPDF2 import PdfFileMerger
import os

cur_dir = os.path.dirname(__file__)

pdfs = ['ds02-ahmed.pdf', 'ds02-ahmed-corr.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(os.path.join(cur_dir, pdf))

merger.write(os.path.join(cur_dir, "ds02-ahmed-algo.pdf"))
merger.close()