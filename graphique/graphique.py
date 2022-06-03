from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2 as cv
import numpy as np
import threading
import webbrowser
import sys

sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")
from read_write_histogram.histogram import histogram
from  read_write_histogram.readPGM import readPGM
from  read_write_histogram.writePGM import writePGM
from histogram_manipulation.egalisationh import egalisation,modif_image
from histogram_manipulation.modificationcontraste import contraste
from Thresholding.auto_threshholding import otsu
from Thresholding.manual_thresholding import manual_threshholding
from filtre_moyen_filtre_median.bruit import bruit
from filtre_moyen_filtre_median.filtre import medianFiltre, moyennefilter, hautfilter
from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this
from Thresholding.fermeture import fermeture
from Thresholding.ouverture import ouverture

tk = Tk()
windowWidth = tk.winfo_reqwidth()
windowHeight = tk.winfo_reqheight()
positionRight = int(tk.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(tk.winfo_screenheight()/3 - windowHeight/1)
tk.geometry(f"800x510+{positionRight}+{positionDown}")
tk.resizable(width=False, height=False)


tk.title("Image Processing Tool")
F1 = Frame(tk)
F1.grid(row=0, column=0,pady=25, padx=25)
l1 = Label(F1, text="Original Image", font="bold")
l1.grid(row=0, column=0)
L1 = Label(F1, text="Original Image",height="25",width="52",bd=0.5, relief="solid")
L1.grid(row=1, column=0, pady=10, padx=15)
l2 = Label(F1, text="Modified Image", font="bold")
l2.grid(row=0, column=1)
L2 = Label(F1, text="Modified Image",height="25",width="52",bd=0.5, relief="solid")
L2.grid(row=1, column=1)
F2 = None
F3 = None

def select_image():
    global tkimage
    global original
    global selectedimage_path
    global img_modif

    global img
    global lx
    global ly

    selectedimage_path = filedialog.askopenfilename(initialdir = "Desktop")
    if not selectedimage_path:
        return
    print(selectedimage_path)
    try:
        original = cv.imread(selectedimage_path)
        if (selectedimage_path.count("ppm") !=1):
            img,lx,ly=readPGM(selectedimage_path)
            img_modif = img
        
        im = Image.fromarray(original)
        im.thumbnail((360, 360))
        tkimage = ImageTk.PhotoImage(im)

        L1 = Label(F1, image = None) 
        L1.config(image = tkimage)
        
        L2 = Label(F1, image = None)
        L2.config(image = tkimage)

        L1.grid(row=1, column=0)
        L2.grid(row=1, column=1)
        saveBTN.config(state="normal",cursor="hand2")
        tk.geometry("1200x510")
    except:
        return

def save_image():
    perm = filedialog.asksaveasfilename(initialdir ="Desktop")
    if not perm:
        return
    writePGM(img_modif, perm,lx,ly, "P2")
    save_image = Label(F1, text="Save image", font="bold")
    save_image.grid(row=2, column=1,pady=27)
    save_image.after(2000, save_image.destroy)

def histoeg_image():
    saveBTN.config(state="disabled",cursor="")
    img_modif=modif_image(img,lx,ly)
    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def dilatationcl_image():
    saveBTN.config(state="disabled",cursor="")
    img_modif=contraste(img,lx,ly,[70,50],[120,100])
    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def dilatationsm_image():
    saveBTN.config(state="disabled",cursor="")
    img_modif=contraste(img,lx,ly,[50,200],[200,240])
    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def dilatationzm_image():
    saveBTN.config(state="disabled",cursor="")
    img_modif=contraste(img,lx,ly,[110,50],[140,205])
    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def manualth_image():
    saveBTN.config(state="disabled",cursor="")
    img_modif=manual_threshholding(original, 150, 150, 150)
    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def autoth_image():
    saveBTN.config(state="disabled",cursor="")
    if (selectedimage_path.count("ppm") ==1):
        [th0, th1, th2] = otsu(original)
        img_modif=manual_threshholding(original, th2, th1, th0 )
    else:
        th = otsu(img)
        img_modif = manual_threshholding(img, s=th)

    im = Image.fromarray(img_modif)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)
    saveBTN.config(state="normal",cursor="hand2")

def f_bruit_btn():
    imgbruit=bruit(img,lx,ly)
    imgtk3 = ImageTk.PhotoImage(image=Image.fromarray(imgbruit)) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_filter_moyen_btn():
    img_filter_moyen=moyennefilter(img,lx,ly,5)
    im = Image.fromarray(img_filter_moyen)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_filter_median_btn():
    img_filter_median=medianFiltre(img,lx,ly,5)
    im = Image.fromarray(img_filter_median)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_filter_haut_btn():
    img_filter=hautfilter(img,lx,ly)
    im = Image.fromarray(img_filter)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_erosion_btn():
    img_e = erode_this(np.copy(img), erosion_level=3)
    im = Image.fromarray(img_e)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_dilatation_btn():
    img_d = dilate_this(np.copy(img), dilation_level=3)
    im = Image.fromarray(img_d)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_fermeture_btn():
    img_f = fermeture(np.copy(img), 9)
    im = Image.fromarray(img_f)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def f_ouverture_btn():
    img_f = ouverture(np.copy(img), 9)
    im = Image.fromarray(img_f)
    im.thumbnail((360, 360))
    imgtk3 = ImageTk.PhotoImage(image=im)
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

def trgt2():
    threading.Thread(target=select_image).start()
def trgt3():
    threading.Thread(target=save_image).start()
def histoeg():
    threading.Thread(target=histoeg_image).start()
def dilatationcl():
    threading.Thread(target=dilatationcl_image).start()
def dilatationsm():
    threading.Thread(target=dilatationsm_image).start()
def dilatationzm():
    threading.Thread(target=dilatationzm_image).start()

def manualth():
    threading.Thread(target=manualth_image).start()
def autoth():
    threading.Thread(target=autoth_image).start()

B1 = Button(tk, text = "Select Image", command=trgt2)
B1.config(cursor="hand2")
B1.place(x=180,y=450)

bruit_btn = Button(tk,text="bruit", width = 18,command=f_bruit_btn)
bruit_btn.config(cursor="hand2")
bruit_btn.place(x=800,y=56)

filter_moyen_btn = Button(tk,text="filter moyen", width = 18,command=f_filter_moyen_btn)
filter_moyen_btn.config(cursor="hand2")
filter_moyen_btn.place(x=800,y=90)

filter_median_btn = Button(tk,text="filter median", width = 18,command=f_filter_median_btn)
filter_median_btn.config(cursor="hand2")
filter_median_btn.place(x=800,y=124)

filter_median_btn = Button(tk,text="filter passe haut", width = 18,command=f_filter_haut_btn)
filter_median_btn.config(cursor="hand2")
filter_median_btn.place(x=800,y=158)

histoeg_btn = Button(tk,text="Histogramme Eg", width = 18, command=histoeg)
histoeg_btn.config(cursor="hand2")
histoeg_btn.place(x=800,y=192)

dilatationcl_btn = Button(tk,text="Dilatation Zone Clair", width = 18, command=dilatationcl)
dilatationcl_btn.config(cursor="hand2")
dilatationcl_btn.place(x=800,y=226)

dilatationsm_btn = Button(tk,text="Dilatation Zone Sombre", width = 18, command=dilatationsm)
dilatationsm_btn.config(cursor="hand2")
dilatationsm_btn.place(x=800,y=260)

dilatationzm_btn = Button(tk,text="Dilatation Zone Milieu", width = 18, command=dilatationzm)
dilatationzm_btn.config(cursor="hand2")
dilatationzm_btn.place(x=800,y=294)

manualth_btn = Button(tk,text="Manual Threshholding", width = 18, command=manualth)
manualth_btn.config(cursor="hand2")
manualth_btn.place(x=950,y=56)

autoth_btn = Button(tk,text="Auto Threshholding", width = 18, command=autoth)
autoth_btn.config(cursor="hand2")
autoth_btn.place(x=950,y=90)

filter_erosion_btn = Button(tk,text="erosion", width = 18,command=f_erosion_btn)
filter_erosion_btn.config(cursor="hand2")
filter_erosion_btn.place(x=950,y=124)

filter_dilatation_btn = Button(tk,text="dilatation", width = 18,command=f_dilatation_btn)
filter_dilatation_btn.config(cursor="hand2")
filter_dilatation_btn.place(x=950,y=158)

filter_fermeture_btn = Button(tk,text="fermeture", width = 18,command=f_fermeture_btn)
filter_fermeture_btn.config(cursor="hand2")
filter_fermeture_btn.place(x=950,y=192)

filter_ouverture_btn = Button(tk,text="ouverture", width = 18,command=f_ouverture_btn)
filter_ouverture_btn.config(cursor="hand2")
filter_ouverture_btn.place(x=950,y=226)


saveBTN = Button(tk, text = "Save Image", command=trgt3)
saveBTN.config(state="disabled")
saveBTN.place(x=565,y=450)

def callback(url):
    webbrowser.open_new(url)

me = Label(tk, text="Developers: Maissa Gallah - Chadha Siala", fg="#6E7371",cursor="hand2",font="Verdana 7 bold")
me.place(x=280,y=485)
tk.mainloop()