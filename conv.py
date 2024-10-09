from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
import tkinter.filedialog as filedialog 
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from PyPDF2 import PdfWriter, PdfReader, PdfMerger
import img2pdf 
from PIL import Image 
import os












# Convert Image to PDF function
def pdfconvert(pdf_path, img_path):
    image = Image.open(img_path) 
    pdf_bytes = img2pdf.convert(image.filename) 
    with open(pdf_path, "wb") as file:
        file.write(pdf_bytes)
    image.close()













# Convert PDF functions
def get_img_func():
    root.img_file_name = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file", 
                                                            filetypes=(("JPG files", "*.JPG"), 
                                                                       ("PNG files", "*.PNG"), 
                                                                       ("all files", "*.*")))
    tempname1 = os.path.basename(root.img_file_name)
    get_file_button.config(text=tempname1, state="disabled")
    return root.img_file_name

def convert():
    if not root.img_file_name:
        messagebox.showerror("Error", "No image selected.")
        return
    root.location = tkinter.filedialog.asksaveasfilename(initialdir="/", title="Save PDF as", filetypes=(("PDF files", "*.PDF"), ("all files", "*.*")))
    if not root.location:
        return
    root.location += '.pdf'
    tempname = os.path.basename(root.location)
    convert_button.config(text=tempname, state="disabled")
    pdfconvert(root.location, root.img_file_name)
    messagebox.showinfo('Message', f'Your PDF file "{tempname}" has been saved successfully!')








# Split PDF functions
def splitpdf(inpdf, outpdf, name, start_page, end_page):
    try:
        inputpdf = PdfReader(inpdf)
        total_pages = len(inputpdf.pages)  # Using len to get the total pages
        
        if start_page < 1 or end_page > total_pages:
            messagebox.showerror("Error", "Invalid page range.")
            return
        
        for i in range(start_page-1, end_page):
            output = PdfWriter()
            output.add_page(inputpdf.pages[i])
            page_filename = os.path.join(outpdf, f"{name}_page_{i+1}.pdf")
            with open(page_filename, "wb") as outputStream:
                output.write(outputStream)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Get file for splitting
def get_Split_file_func():
    root.get_split_filename = filedialog.askopenfilename(initialdir="/", title="Select PDF file", 
                                                         filetypes=(("PDF files", "*.PDF"), ("all files", "*.*")))
    if root.get_split_filename:
        tempname1 = os.path.basename(root.get_split_filename)
        split_file_get_button.config(text=tempname1, state="disabled")
    return root.get_split_filename

# Perform splitting
def split():
    if not root.get_split_filename:
        messagebox.showerror("Error", "No PDF file selected for splitting.")
        return
    start_page = int(split_start_page.get())
    end_page = int(split_end_page.get())
    root.location = filedialog.askdirectory(title="Select Folder to Save Split PDFs")
    if not root.location:
        return
    tempname = os.path.splitext(os.path.basename(root.get_split_filename))[0]
    split_folder = os.path.join(root.location, tempname)
    
    # Create folder if it doesn't exist
    if not os.path.exists(split_folder):
        os.makedirs(split_folder)
    
    splitpdf(root.get_split_filename, split_folder, tempname, start_page, end_page)
    messagebox.showinfo('Message', f'Your PDF file has been split and saved in: {split_folder}')













# Merge PDF functions
def PDFmerge(pdfs, output):  
    pdfMerger = PdfMerger()
    for pdf in pdfs: 
        pdfMerger.append(pdf) 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 

def get_first_pdf_fn():
    root.first_pdf_file = filedialog.askopenfilename(initialdir="/", title="Select first PDF", 
                                                     filetypes=(("PDF files", "*.PDF"), ("all files", "*.*")))
    tempname1 = os.path.basename(root.first_pdf_file)
    get_first_pdf_btn.config(text=tempname1, state="disabled")
    return root.first_pdf_file

def get_second_pdf_fn():
    root.second_pdf_file = filedialog.askopenfilename(initialdir="/", title="Select second PDF", 
                                                      filetypes=(("PDF files", "*.PDF"), ("all files", "*.*")))
    tempname2 = os.path.basename(root.second_pdf_file)
    get_second_pdf_btn.config(text=tempname2, state="disabled")
    return root.second_pdf_file

def merge():
    if not (root.first_pdf_file and root.second_pdf_file):
        messagebox.showerror("Error", "Select both PDF files for merging.")
        return
    pdfs = [root.first_pdf_file, root.second_pdf_file]
    root.filename = filedialog.asksaveasfilename(initialdir="/", title="Save merged PDF as", 
                                                 filetypes=(("PDF files", "*.PDF"), ("all files", "*.*")))
    if not root.filename:
        return
    root.filename += '.pdf'
    tempname = os.path.basename(root.filename)
    merge_button.config(text=tempname, state="disabled")
    PDFmerge(pdfs=pdfs, output=root.filename)
    messagebox.showinfo('Message', f'Your PDF files have been merged successfully as "{tempname}".')























# Main UI
root = Tk()
style = ttk.Style(root)
root.configure(bg='white')
root.geometry('500x400')
root.title("PDF Converter v1.0")

option = IntVar()






# Frames for each feature
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)






# Frame selectors
def select1():
    f2.grid_forget()
    f3.grid_forget()
    f1.grid(row=1, column=0, padx=20, pady=20)

def select2():
    f1.grid_forget()
    f3.grid_forget()
    f2.grid(row=1, column=0, padx=20, pady=20)

def select3():
    f1.grid_forget()
    f2.grid_forget()
    f3.grid(row=1, column=0, padx=20, pady=20)




def reset_btn_fn():
    get_file_button.config(text='Load Image', state="normal")
    convert_button.config(text='Convert to PDF', state="normal")
    split_file_get_button.config(text='Load PDF', state="normal")
    split_main_button.config(text='Split', state="normal")
    get_first_pdf_btn.config(text='Load PDF 1', state="normal")
    get_second_pdf_btn.config(text='Load PDF 2', state="normal")
    merge_button.config(text='Join PDF', state="normal")

    root.update()
    messagebox.showinfo('Message', '         Reseted now...\n\nDeveloped by Swapnil visit again!')

actionBtn = ttk.Button(root, text="Reset", width=15, command=reset_btn_fn)
actionBtn.place(x=155, y=240)





# Radiobuttons for each option
Radiobutton(root, bg='#ffffff', text="Convert", variable=option, value=1, command=select1, padx=30, pady=50).grid(column=0, row=0)
Radiobutton(root, bg='#ffffff', text="Split", variable=option, value=2, command=select2, padx=30, pady=50).grid(column=1, row=0)
Radiobutton(root, bg='#ffffff', text="Join", variable=option, value=3, command=select3, padx=30, pady=50).grid(column=2, row=0)








# Frame 1: Convert (Image to PDF)
Label(f1, text="Select Image to Convert to PDF").grid(row=0, column=0)
get_file_button = Button(f1, text="Select Image", command=get_img_func)
get_file_button.grid(row=1, column=0)
convert_button = Button(f1, text="Convert to PDF", command=convert)
convert_button.grid(row=2, column=0)








# Frame 2: Split PDF
Label(f2, text="Select PDF to Split").grid(row=0, column=0)
split_file_get_button = Button(f2, text="Select PDF", command=get_Split_file_func)
split_file_get_button.grid(row=1, column=0)

Label(f2, text="Enter Start Page").grid(row=2, column=0)
split_start_page = Entry(f2)
split_start_page.grid(row=3, column=0)

Label(f2, text="Enter End Page").grid(row=4, column=0)
split_end_page = Entry(f2)
split_end_page.grid(row=5, column=0)

split_main_button = Button(f2, text="Split PDF", command=split)
split_main_button.grid(row=6, column=0)










# Frame 3: Merge PDFs
Label(f3, text="Select First PDF").grid(row=0, column=0)
get_first_pdf_btn = Button(f3, text="Select First PDF", command=get_first_pdf_fn)
get_first_pdf_btn.grid(row=1, column=0)

Label(f3, text="Select Second PDF").grid(row=2, column=0)
get_second_pdf_btn = Button(f3, text="Select Second PDF", command=get_second_pdf_fn)
get_second_pdf_btn.grid(row=3, column=0)

merge_button = Button(f3, text="Merge PDFs", command=merge)
merge_button.grid(row=4, column=0)















select1()

root.mainloop()
