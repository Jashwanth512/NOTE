import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import os,sys
import pikepdf
from pikepdf import _cpphelpers
import requests
import threading
import webbrowser as wb
import socket
import datetime
import shutil
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def download_updates(file_name):
    os.makedirs(r"c:\Note_Files",exist_ok=True)
    url = "https://subjects.s3.us-east-2.amazonaws.com/"
    url = url + file_name
    downloadthread = threading.Thread(target=lambda: download(url, file_name))
    downloadthread.start()
def download(url,file_name):
    try:
        if url != None:
            req = requests.get(url, stream=True)
            if "Content-Length" in req.headers:
                total_size = req.headers["Content-Length"]
            else:
                total_size = None
            if total_size!=None:
                destination_folder=resource_path(r"c:\Note_Files\_")
                destination=destination_folder+file_name
                with open(destination, "wb") as pdf:
                    for chunk in req.iter_content(chunk_size=1024):

                        # writing one chunk at a time to pdf file
                        if chunk:
                            pdf.write(chunk)
                            current_size = os.path.getsize(destination)
                            #if total_size != None:
                            percentage = round((int(current_size) / int(total_size)) * 100)
                            if "MATHS" in file_name:
                                progress_bar1["value"] = percentage
                            elif "Iot" in file_name:
                                progress_bar2["value"] = percentage
                            elif "COA" in file_name:
                                progress_bar3["value"] = percentage
                            elif "OS" in file_name:
                                progress_bar4["value"] = percentage
                            elif "CN" in file_name:
                                progress_bar5["value"] = percentage
                            elif "DA" in file_name:
                                progress_bar6["value"] = percentage

                    kb=(int(total_size)/1000)
                    mb = kb / 1000
                    j = round(mb, 2)
                    size = str(j)
                    messagebox._show("Download Complete",file_name+" has been Updated.\nFile Size: "+size+"mb")
                    try:
                        if len(os.listdir(resource_path(r"c:\Note_Files")))==1:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect(("18.116.234.116", 3388))
                            s.send(bytes("True","utf-8"))
                    except Exception:
                        pass

                    if "MATHS" in file_name:
                        progress_bar1["value"] = 0
                    elif "Iot" in file_name:
                        progress_bar2["value"] = 0
                    elif "COA" in file_name:
                        progress_bar3["value"] = 0
                    elif "OS" in file_name:
                        progress_bar4["value"] = 0
                    elif "CN" in file_name:
                        progress_bar5["value"] = 0
                    elif "DA" in file_name:
                        progress_bar6["value"] = 0

            else:
                messagebox.showinfo("Unit info",file_name+" is not uploaded in the database,try again later")
    except requests.exceptions.ConnectionError:
        messagebox.showinfo("Internet","Please check your Internet Connection, and Try again.")
    except requests.exceptions.InvalidURL:
        messagebox.showinfo("File Not Found","File not found")
def new_version(version):
    url = "https://subjects.s3.us-east-2.amazonaws.com/"
    url = url + version
    downloadthread = threading.Thread(target=lambda: note_version(url, version))
    downloadthread.start()

def note_version(file_url,file_name):
    try:
        if file_url!=None:
            req = requests.get(file_url, stream=True)
            if "Content-Length" in req.headers:
                total_size = req.headers["Content-Length"]
            else:
                total_size = None
            if total_size==None:
                messagebox.showinfo("Note Update","At present, there is no new versions of the 'NOTE'.\nIf you want to update the units, Click on the 'Update' button below the 'Unit' button")
            else:
                messagebox.showinfo("Please Wait","It may take some time to download the new version,do not close the software.")
                destination_folder =file_name
                with open(destination_folder, "wb") as exe:
                    for chunk in req.iter_content(chunk_size=1024):

                        # writing one chunk at a time to pdf file
                        if chunk:
                            exe.write(chunk)
                messagebox.showinfo("Update","New version of 'NOTE' is downloaded")
    except requests.exceptions.ConnectionError:
        messagebox.showinfo("Internet","Please check your Internet Connection, and Try again.")
class OS_UPDATE:
    def os_syllabus(self=None):
        unit="OS_SYLLABUS.pdf"
        download_updates(unit)
    def os_unit1(self=None):
        unit="OS_UNIT1.pdf"
        download_updates(unit)
    def os_unit2(self=None):
        unit="OS_UNIT2.pdf"
        download_updates(unit)
    def os_unit3(self=None):
        unit="OS_UNIT3.pdf"
        download_updates(unit)
    def os_unit4(self=None):
        unit="OS_UNIT4.pdf"
        download_updates(unit)
    def os_unit5(self=None):
        unit="OS_UNIT5.pdf"
        download_updates(unit)
    def os_textbook(self=None):
        unit="OS_TEXTBOOK.pdf"
        download_updates(unit)
class CN_UPDATE:
    def cn_syllabus(self=None):
        unit="CN_SYLLABUS.pdf"
        download_updates(unit)
    def cn_unit1(self=None):
        unit="CN_UNIT1.pdf"
        download_updates(unit)
    def cn_unit2(self=None):
        unit="CN_UNIT2.pdf"
        download_updates(unit)
    def cn_unit3(self=None):
        unit="CN_UNIT3.pdf"
        download_updates(unit)
    def cn_unit4(self=None):
        unit="CN_UNIT4.pdf"
        download_updates(unit)
    def cn_unit5(self=None):
        unit="CN_UNIT5.pdf"
        download_updates(unit)
    def cn_textbook(self=None):
        unit="CN_TEXTBOOK.pdf"
        download_updates(unit)
class DA_UPDATE:
    def da_syllabus(self=None):
        unit="DA_SYLLABUS.pdf"
        download_updates(unit)
    def da_unit1(self=None):
        unit="DA_UNIT1.pdf"
        download_updates(unit)
    def da_unit2(self=None):
        unit="DA_UNIT2.pdf"
        download_updates(unit)
    def da_unit3(self=None):
        unit="DA_UNIT3.pdf"
        download_updates(unit)
    def da_unit4(self=None):
        unit="DA_UNIT4.pdf"
        download_updates(unit)
    def da_unit5(self=None):
        unit="DA_UNIT5.pdf"
        download_updates(unit)
    def da_textbook(self=None):
        unit="DA_TEXTBOOK.pdf"
        download_updates(unit)
class Iot_UPDATE:
    def Iot_syllabus(self=None):
        unit="Iot_SYLLABUS.pdf"
        download_updates(unit)
    def Iot_unit1(self=None):
        unit="Iot_UNIT1.pdf"
        download_updates(unit)
    def Iot_unit2(self=None):
        unit="Iot_UNIT2.pdf"
        download_updates(unit)
    def Iot_unit3(self=None):
        unit="Iot_UNIT3.pdf"
        download_updates(unit)
    def Iot_unit4(self=None):
        unit="Iot_UNIT4.pdf"
        download_updates(unit)
    def Iot_unit5(self=None):
        unit="Iot_UNIT5.pdf"
        download_updates(unit)
    def Iot_textbook(self=None):
        unit="Iot_TEXTBOOK.pdf"
        download_updates(unit)
class COA_UPDATE:
    def coa_syllabus(self=None):
        unit="COA_SYLLABUS.pdf"
        download_updates(unit)
    def coa_unit1(self=None):
        unit="COA_UNIT1.pdf"
        download_updates(unit)
    def coa_unit2(self=None):
        unit="COA_UNIT2.pdf"
        download_updates(unit)
    def coa_unit3(self=None):
        unit="COA_UNIT3.pdf"
        download_updates(unit)
    def coa_unit4(self=None):
        unit="COA_UNIT4.pdf"
        download_updates(unit)
    def coa_unit5(self=None):
        unit="COA_UNIT5.pdf"
        download_updates(unit)
    def coa_textbook(self=None):
        unit="COA_TEXTBOOK.pdf"
        download_updates(unit)
class MATHS_UPDATE:
    def maths_syllabus(self=None):
        unit="MATHS_SYLLABUS.pdf"
        download_updates(unit)
    def maths_unit1(self=None):
        unit="MATHS_UNIT1.pdf"
        download_updates(unit)
    def maths_unit2(self=None):
        unit="MATHS_UNIT2.pdf"
        download_updates(unit)
    def maths_unit3(self=None):
        unit="MATHS_UNIT3.pdf"
        download_updates(unit)
    def maths_unit4(self=None):
        unit="MATHS_UNIT4.pdf"
        download_updates(unit)
    def maths_unit5(self=None):
        unit="MATHS_UNIT5.pdf"
        download_updates(unit)
    def maths_textbook(self=None):
        unit="MATHS_TEXTBOOK.pdf"
        download_updates(unit)
def note_update():
    version="NOTE.exe"
    new_version(version)
###DOWNLOADING UPDATE CODE COMPLETED###



###OPENING THE DOWNLOADED PDFs###
    ##G-Learn Webpage##
def gitam():
    url="https://login.gitam.edu/Login.aspx"
    wb.open_new_tab(url)

##GITAM RESULTS WEBPAGE##
def gitam_results():
    url="https://doeresults.gitam.edu/onlineresults/pages/newgrdcrdinput1.aspx"
    wb.open_new_tab(url)
def pass_pdf(pdf_file):
    pdf_file_name=r"C:\Note_Files\_"+pdf_file
    print(pdf_file_name)
    downloadthread = threading.Thread(target=lambda:open_pass_pdf(pdf_file_name))
    downloadthread.start()
def open_pass_pdf(pdf_file):
    try:
        pdf = pikepdf.open(pdf_file,password="thisismysoftware", allow_overwriting_input=True)
        try:
            pdf.save(r"C:\Note_Files\_FROM_NOTE.pdf")
            os.system(r"C:\Note_Files\_FROM_NOTE.pdf")
        except PermissionError:
            try:
                pdf.save(r"C:\Note_Files\_FROM_NOTE1.pdf")
                os.system(r"C:\Note_Files\_FROM_NOTE1.pdf")
            except PermissionError:
                messagebox.showinfo("Close PDF","Close any one of the PDFs and Try Opening again.")
        try:
            os.remove(r"C:\Note_Files\_FROM_NOTE.pdf")
        except Exception:
            pass
        try:
            os.remove(r"C:\Note_Files\_FROM_NOTE1.pdf")
        except Exception:
            pass
    except FileNotFoundError:
        messagebox.showinfo("Unit Info","Please Update the unit and try again")
    except pikepdf._qpdf.PdfError:
        messagebox.showinfo("Damaged File","This file is damaged,Update again and Open again")
class OS_class:
    def syllabus(self=None):
        pdf_name="OS_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name="OS_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name ="OS_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "OS_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "OS_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "OS_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="OS_textbook.pdf"
        pass_pdf(pdf_name)

class CN_class:
    def syllabus(self=None):
        pdf_name = "CN_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name = "CN_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name = "CN_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "CN_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "CN_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "CN_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="CN_textbook.pdf"
        pass_pdf(pdf_name)


class DA_class:
    def syllabus(self=None):
        pdf_name = "DA_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name = "DA_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name = "DA_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "DA_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "DA_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "DA_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="DA_textbook.pdf"
        pass_pdf(pdf_name)
class MATHS_class:
    def syllabus(self=None):
        pdf_name = "MATHS_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name = "MATHS_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name = "MATHS_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "MATHS_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "MATHS_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "MATHS_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="MATHS_textbook.pdf"
        pass_pdf(pdf_name)

class COA_class:
    def syllabus(self=None):
        pdf_name = "COA_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name = "COA_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name = "COA_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "COA_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "COA_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "COA_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="COA_textbook.pdf"
        pass_pdf(pdf_name)
class Iot_class:
    def syllabus(self=None):
        pdf_name = "Iot_SYLLABUS.pdf"
        pass_pdf(pdf_name)
    def unit1(self=None):
        pdf_name = "Iot_UNIT1.pdf"
        pass_pdf(pdf_name)
    def unit2(self=None):
        pdf_name = "Iot_UNIT2.pdf"
        pass_pdf(pdf_name)
    def unit3(self=None):
        pdf_name = "Iot_UNIT3.pdf"
        pass_pdf(pdf_name)
    def unit4(self=None):
        pdf_name = "Iot_UNIT4.pdf"
        pass_pdf(pdf_name)
    def unit5(self=None):
        pdf_name = "Iot_UNIT5.pdf"
        pass_pdf(pdf_name)
    def text_books(self=None):
        pdf_name="Iot_textbook.pdf"
        pass_pdf(pdf_name)


class Frames:
    def maths(self):
        try:
            self.iot_frame.pack_forget()
        except Exception:
            pass
        try:
            self.os_frame.pack_forget()
        except Exception:
            pass
        try:
            self.csa_frame.pack_forget()
        except Exception:
            pass
        try:
            self.cn_frame.pack_forget()
        except Exception:
            pass
        try:
            self.da_frame.pack_forget()
        except Exception:
            pass
        self.maths_frame=tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.maths_frame, image=test, bg="#232425")
        label1.image = test

        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label=tk.Label(self.maths_frame,bg="#232425")
        self.title=tk.Label(self.title_label,text="Mathematics",fg="white",font=("Times",24),bg="#232425").pack(side="left")
        self.title_label.pack(fill="x")
        self.maths_frame.pack(fill="both",expand=True)
        ##Progress_bar
        progress_bar_label = tk.Label(self.maths_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar1
        progress_bar1 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar1.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR
        label_syllabus = tk.Label(self.maths_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=MATHS_class.syllabus,text="SYLLABUS", pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=MATHS_UPDATE.maths_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")
        label1=tk.Label(self.maths_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=MATHS_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",padx=10,pady=5,command=MATHS_UPDATE.maths_unit1,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.maths_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=MATHS_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",padx=10,pady=5,command=MATHS_UPDATE.maths_unit2,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.maths_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=MATHS_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",padx=10,pady=5,command=MATHS_UPDATE.maths_unit3,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.maths_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=MATHS_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",padx=10,pady=5,command=MATHS_UPDATE.maths_unit4,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.maths_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=MATHS_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",padx=10,pady=5,command=MATHS_UPDATE.maths_unit5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.maths_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book",padx=5, pady=5, command=MATHS_class.text_books, font=("Times", 10),
                          bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=MATHS_UPDATE.maths_textbook,
                            font=("Times", 10)).pack(side="right")
        self.maths.config(state="disabled")
        self.Iot.config(state="normal")
        self.CSA.config(state="normal")
        self.OS.config(state="normal")
        self.DA.config(state="normal")
        self.CN.config(state="normal")
    def iot(self):
        try:
            self.maths_frame.pack_forget()
        except Exception:
            pass
        try:
            self.os_frame.pack_forget()
        except Exception:
            pass
        try:
            self.csa_frame.pack_forget()
        except Exception:
            pass
        try:
            self.cn_frame.pack_forget()
        except Exception:
            pass
        try:
            self.da_frame.pack_forget()
        except Exception:
            pass
        self.iot_frame = tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.iot_frame, image=test, bg="#232425")
        label1.image = test
        ##Progress_bar
        progress_bar_label = tk.Label(self.iot_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar2
        progress_bar2 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar2.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR
        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label = tk.Label(self.iot_frame,bg="#232425")
        self.title = tk.Label(self.title_label, text="Internet Of Things", fg="white",font=("Times",24),bg="#232425").pack(side="left")
        self.title_label.pack(fill="x")
        self.iot_frame.pack(fill="both", expand=True)
        label_syllabus = tk.Label(self.iot_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=Iot_class.syllabus,text="SYLLABUS", pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=Iot_UPDATE.Iot_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")
        label1=tk.Label(self.iot_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=Iot_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",command=Iot_UPDATE.Iot_unit1,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.iot_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=Iot_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",command=Iot_UPDATE.Iot_unit2,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.iot_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=Iot_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",command=Iot_UPDATE.Iot_unit3,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.iot_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=Iot_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",command=Iot_UPDATE.Iot_unit4,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.iot_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=Iot_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",command=Iot_UPDATE.Iot_unit5,padx=10,pady=5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.iot_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book", padx=5, pady=5, command=Iot_class.text_books,
                              font=("Times", 10),
                              bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=Iot_UPDATE.Iot_textbook,
                                     font=("Times", 10)).pack(side="right")
        self.maths.config(state="normal")
        self.Iot.config(state="disabled")
        self.CSA.config(state="normal")
        self.OS.config(state="normal")
        self.DA.config(state="normal")
        self.CN.config(state="normal")
    def csa(self):
        try:
            self.iot_frame.pack_forget()
        except Exception:
            pass
        try:
            self.os_frame.pack_forget()
        except Exception:
            pass
        try:
            self.maths_frame.pack_forget()
        except Exception:
            pass
        try:
            self.cn_frame.pack_forget()
        except Exception:
            pass
        try:
            self.da_frame.pack_forget()
        except Exception:
            pass
        self.csa_frame = tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.csa_frame, image=test, bg="#232425")
        label1.image = test

        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label = tk.Label(self.csa_frame,bg="#232425")
        self.title = tk.Label(self.title_label, text="Computer Organization and Architecture", fg="white",font=("Times",24),bg="#232425").pack(
            side="left")
        self.title_label.pack(fill="x")
        self.csa_frame.pack(fill="both", expand=True)
        ##Progress_bar
        progress_bar_label = tk.Label(self.csa_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar3
        progress_bar3 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar3.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR
        label_syllabus = tk.Label(self.csa_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=COA_class.syllabus,text="SYLLABUS",pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=COA_UPDATE.coa_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")

        label1=tk.Label(self.csa_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=COA_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",command=COA_UPDATE.coa_unit1,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.csa_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=COA_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",command=COA_UPDATE.coa_unit2,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.csa_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=COA_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",command=COA_UPDATE.coa_unit3,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.csa_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=COA_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",command=COA_UPDATE.coa_unit4,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.csa_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=COA_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",command=COA_UPDATE.coa_unit5,padx=10,pady=5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.csa_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book", padx=5, pady=5,  command=COA_class.text_books,
                              font=("Times", 10),
                              bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=COA_UPDATE.coa_textbook,
                                     font=("Times", 10)).pack(side="right")
        self.maths.config(state="normal")
        self.Iot.config(state="normal")
        self.CSA.config(state="disabled")
        self.OS.config(state="normal")
        self.DA.config(state="normal")
        self.CN.config(state="normal")
    def os(self):
        try:
            self.iot_frame.pack_forget()
        except Exception:
            pass
        try:
            self.maths_frame.pack_forget()
        except Exception:
            pass
        try:
            self.csa_frame.pack_forget()
        except Exception:
            pass
        try:
            self.cn_frame.pack_forget()
        except Exception:
            pass
        try:
            self.da_frame.pack_forget()
        except Exception:
            pass
        self.os_frame=tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.os_frame, image=test, bg="#232425")
        label1.image = test
        ##Progress_bar
        progress_bar_label = tk.Label(self.os_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar4
        progress_bar4 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar4.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR

        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label = tk.Label(self.os_frame,bg="#232425")
        self.title = tk.Label(self.title_label, text="Operating Systems", fg="white",font=("Times",24),bg="#232425").pack(
            side="left")
        self.title_label.pack(fill="x")
        self.os_frame.pack(fill="both",expand=True)
        label_syllabus = tk.Label(self.os_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=OS_class.syllabus,text="SYLLABUS", pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=OS_UPDATE.os_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")
        label1=tk.Label(self.os_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=OS_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",command=OS_UPDATE.os_unit1,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.os_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=OS_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",command=OS_UPDATE.os_unit2,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.os_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=OS_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",command=OS_UPDATE.os_unit3,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.os_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=OS_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",command=OS_UPDATE.os_unit4,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.os_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=OS_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",command=OS_UPDATE.os_unit5,padx=10,pady=5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.os_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book", padx=5, pady=5, command=OS_class.text_books,
                              font=("Times", 10),
                              bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=OS_UPDATE.os_textbook,
                                     font=("Times", 10)).pack(side="right")

        self.maths.config(state="normal")
        self.Iot.config(state="normal")
        self.CSA.config(state="normal")
        self.OS.config(state="disabled")

        self.DA.config(state="normal")
        self.CN.config(state="normal")
    def cn(self):
        try:
            self.iot_frame.pack_forget()
        except Exception:
            pass
        try:
            self.os_frame.pack_forget()
        except Exception:
            pass
        try:
            self.csa_frame.pack_forget()
        except Exception:
            pass
        try:
            self.maths_frame.pack_forget()
        except Exception:
            pass

        try:
            self.da_frame.pack_forget()
        except Exception:
            pass
        self.cn_frame = tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.cn_frame, image=test, bg="#232425")
        label1.image = test

        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label = tk.Label(self.cn_frame,bg="#232425")
        self.title = tk.Label(self.title_label, text="Computer Networks", fg="white",font=("Times",24),bg="#232425").pack(
            side="left")
        self.title_label.pack(fill="x")
        self.cn_frame.pack(fill="both", expand=True)
        ##Progress_bar
        progress_bar_label = tk.Label(self.cn_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar5
        progress_bar5 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar5.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR
        label_syllabus = tk.Label(self.cn_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=CN_class.syllabus,text="SYLLABUS", pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=CN_UPDATE.cn_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")
        label1=tk.Label(self.cn_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=CN_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",command=CN_UPDATE.cn_unit1,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.cn_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=CN_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",command=CN_UPDATE.cn_unit2,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.cn_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=CN_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",command=CN_UPDATE.cn_unit3,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.cn_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=CN_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",command=CN_UPDATE.cn_unit4,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.cn_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=CN_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",command=CN_UPDATE.cn_unit5,padx=10,pady=5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.cn_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book", padx=5, pady=5,  command=CN_class.text_books,
                              font=("Times", 10),
                              bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=CN_UPDATE.cn_textbook,
                                     font=("Times", 10)).pack(side="right")

        self.maths.config(state="normal")
        self.Iot.config(state="normal")
        self.CSA.config(state="normal")
        self.OS.config(state="normal")

        self.DA.config(state="normal")
        self.CN.config(state="disabled")
    def da(self):
        try:
            self.iot_frame.pack_forget()
        except Exception:
            pass
        try:
            self.os_frame.pack_forget()
        except Exception:
            pass
        try:
            self.csa_frame.pack_forget()
        except Exception:
            pass
        try:
            self.cn_frame.pack_forget()
        except Exception:
            pass
        try:
            self.maths_frame.pack_forget()
        except Exception:
            pass
        self.da_frame = tk.Frame(self.right_frame,bg="#232425")
        image1 = Image.open(resource_path("NOTE.png"))
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(self.da_frame, image=test, bg="#232425")
        label1.image = test

        # Position image
        label1.place(relwidth=1, relheight=1)
        self.title_label = tk.Label(self.da_frame,bg="#232425")
        self.title = tk.Label(self.title_label, text="Design and Analysis of Algorithms", fg="white",font=("Times",24),bg="#232425").pack(
            side="left")
        self.title_label.pack(fill="x")
        self.da_frame.pack(fill="both", expand=True)
        ##Progress_bar

        progress_bar_label = tk.Label(self.da_frame, bg="#232425", width=10)
        progress_bar_label.pack(side="right", fill="y")
        download_label = tk.Label(progress_bar_label, bg="#232425", text="Download\nstatus", fg="white").pack(padx=5)
        global progress_bar6
        progress_bar6 = ttk.Progressbar(progress_bar_label, orient=tk.VERTICAL, length=100, mode="determinate")
        progress_bar6.pack(fill="y", expand=True)
        ##END OF PROGRESS BAR
        label_syllabus = tk.Label(self.da_frame, bd=0, bg="#232425")
        label_syllabus.pack(pady=5)
        Syllabus = tk.Button(label_syllabus, command=DA_class.syllabus,text="SYLLABUS", pady=5, font=("Times", 10), bg="#322e2f",
                             activebackground="#322e2f", activeforeground="white", fg="white").pack(side="left")
        update_Syllabus = tk.Button(label_syllabus, command=DA_UPDATE.da_syllabus,text="Update", padx=10, pady=5,
                                    font=("Times", 10)).pack(side="right")
        label1=tk.Label(self.da_frame,bd=0,bg="#232425")
        label1.pack(pady=5)
        unit1=tk.Button(label1,text="UNIT1",padx=14,pady=5,command=DA_class.unit1,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update1= tk.Button(label1, text="Update",command=DA_UPDATE.da_unit1,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label2 = tk.Label(self.da_frame, bd=0,bg="#232425")
        label2.pack(pady=5)
        unit2 = tk.Button(label2, text="UNIT2",padx=14,pady=5,command=DA_class.unit2,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update2 = tk.Button(label2, text="Update",command=DA_UPDATE.da_unit2,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label3 = tk.Label(self.da_frame, bd=0,bg="#232425")
        label3.pack(pady=5)
        unit3 = tk.Button(label3, text="UNIT3",padx=14,pady=5,command=DA_class.unit3,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update3 = tk.Button(label3, text="Update",command=DA_UPDATE.da_unit3,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label4 = tk.Label(self.da_frame, bd=0,bg="#232425")
        label4.pack(pady=5)
        unit4 = tk.Button(label4, text="UNIT4",padx=14,pady=5,command=DA_class.unit4,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update4 = tk.Button(label4, text="Update",command=DA_UPDATE.da_unit4,padx=10,pady=5,font=("Times",10)).pack(side="right")

        label5 = tk.Label(self.da_frame, bd=0,bg="#232425")
        label5.pack(pady=5)
        unit5 = tk.Button(label5, text="UNIT5",padx=14,pady=5,command=DA_class.unit5,font=("Times",10),bg="#322e2f",activebackground="#322e2f",activeforeground="white",fg="white").pack(side="left")
        update5 = tk.Button(label5, text="Update",command=DA_UPDATE.da_unit5,padx=10,pady=5,font=("Times",10)).pack(side="right")
        label_book = tk.Label(self.da_frame, bd=0, bg="#232425")
        label_book.pack(pady=5)
        Text_book = tk.Button(label_book, text="Text Book", padx=5, pady=5,  command=DA_class.text_books,
                              font=("Times", 10),
                              bg="#322e2f", activebackground="#322e2f", activeforeground="white", fg="white").pack(
            side="left")
        Text_book_update = tk.Button(label_book, text="Update", padx=10, pady=5, command=DA_UPDATE.da_textbook,
                                     font=("Times", 10)).pack(side="right")

        self.maths.config(state="normal")
        self.Iot.config(state="normal")
        self.CSA.config(state="normal")
        self.OS.config(state="normal")
        self.DA.config(state="disabled")
        self.CN.config(state="normal")
    def remove_filess(self):
        shutil.rmtree(r"c:\Note_Files")
    def main_window(self):
        splash_screen.destroy()
        root=tk.Tk()
        root.geometry("1200x500")
        frame=tk.Frame(root,bg="#232425")
        self.left_frame=tk.Frame(frame,bg="#2C3E50",width=300)
        self.maths=tk.Button(self.left_frame,text="Mathematics",padx=40,bg="#2C3E50",fg="white",font=("Times",18,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0,command=frame_class.maths)
        self.maths.pack(padx=50,pady=10)
        self.Iot=tk.Button(self.left_frame,text="Internet of\nThings",bg="#2C3E50",fg="white",font=("Times",16,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0,padx=48,command=frame_class.iot)
        self.Iot.pack(padx=30,pady=10)
        self.CSA=tk.Button(self.left_frame,text="Computer Organization\nand Architecture",padx=13,command=frame_class.csa,bg="#2C3E50",fg="white",font=("Times",14,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0)
        self.CSA.pack(padx=30,pady=10)
        self.OS=tk.Button(self.left_frame,text="Operating Systems",padx=25,command=frame_class.os,bg="#2C3E50",fg="white",font=("Times",17,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0)
        self.OS.pack(padx=30,pady=10)
        self.DA=tk.Button(self.left_frame,text="Design and Analysis\nof Algorithm",padx=21,command=frame_class.da,bg="#2C3E50",fg="white",font=("Times",15,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0)
        self.DA.pack(padx=30,pady=10)
        self.CN=tk.Button(self.left_frame,text="Computer Networks",padx=20,command=frame_class.cn,bg="#2C3E50",fg="white",font=("Times",16,"bold"),activebackground="#2C3E50",cursor='hand2',activeforeground="white",bd=0)
        self.CN.pack(padx=30,pady=10)
        self.remove_files = tk.Button(self.left_frame, text="Remove All Files", padx=19,command=self.remove_filess,
                            bg="#2C3E50", fg="white", font=("Times", 16, "bold"), activebackground="#2C3E50",
                            cursor='hand2', activeforeground="white", bd=0)
        self.remove_files.pack(padx=30, pady=10)
        self.left_frame.pack(fill="y",side="left")
        self.right_frame=tk.Frame(frame,bg="#f5f0e1")
        self.right_frame_wallpaper=tk.PhotoImage(master=self.right_frame,file=resource_path("NOTE2.png"))
        label = tk.Label(self.right_frame, image=self.right_frame_wallpaper, bg="#d2601a")
        label.place(relwidth=1,relheight=1)
        self.right_frame.pack(fill="both",expand=True)
        frame.pack(fill="both",expand=True)
        root.resizable(0,0)
        root.title("NOTE")
        root.iconbitmap(resource_path("note22.ico"))
        root.mainloop()
frame_class=Frames()
splash_screen=tk.Tk()
splash_screen.geometry("1200x500")
splash_screen.iconbitmap(resource_path("note22.ico"))
splash_screen.title("NOTE")
splash_screen.resizable(0,0)
splash_screen.config(bg="#242526")
img=tk.PhotoImage(master=splash_screen,file=resource_path("NOTE2.png"))
splash_label=tk.Label(splash_screen,bg="#242526",image=img).place(relwidth=1,relheight=1)
splash_screen.after(4000,frame_class.main_window)
tk.mainloop()