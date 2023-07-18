#media player
import vlc

#youtube 
import pafy                    #pip install youtube-dl.#pip install youtube-dl==2020.12.2

#links
import webbrowser

#gui
import tkinter
from tkinter import *
from tkinter import ttk

#speech to text
import speech_recognition as sr

#text to speech
import os
from gtts import gTTS 

#translate
from translate import Translator





#TEXT TO SPEECH FUNCTION gtts library os library

def readMsg(): 
    global text_lang 

    text_lang = text_area.get("1.0", "end-1c")
    
    language = 'en'
    # Passing the text and language to the engine,  
    obj = gTTS(text=text_lang, lang='en', slow=False) 
   

    # Saving the converted audio in a mp3 file named
    obj.save("welcome.mp3") 
    os.system("welcome.mp3")



def readTranslatedMsg():
    global text_lang2

    text_lang2=text_area2.get("1.0","end-1c")
    language='en'
    obj2=gTTS(text=text_lang2, lang='en', slow=False) 
    # Saving the converted audio in a mp3 file named
    obj2.save("welcome2.mp3") 
    os.system("welcome2.mp3")





#SPEECH TO TEXT FUNCTION
# Initialize the recognizer
r = sr.Recognizer()

def showMsg():

    global recog

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio=r.listen(source)
        recog=r.recognize_google(audio)

        #type(recog)
        text.insert(INSERT, recog)
        try:
            print("you have said\n",recog)
          
            print("audio recognized \n")
        
        except Exception as e:
            print("error: could not recognize"+ str(e))

     


    
  
def STT_window():
   
    global text

    r1=tkinter.Toplevel()

    r1.geometry("900x400+200+200")
    r1.state('zoomed')
    r1.title("SPEECH TO TEXT")
    r1.configure(bg="#BFBFEF")
    Label(r1,text="SPEECH TO TEXT",font="arial 18 bold",fg="black").place(x=105,y=30)
    Label(r1,text="Your speech will be displayed below",font="arial 20 bold",fg="black").place(x=10,y=110)
    
    #TOPFRAME
    Topframe=Frame(r1,bg="white",width =1500,height=100)
    Topframe.place(x=0,y=0)

    #STT_TEXTBOX=Text(r1,font="arial 20",bg="white",relief=GROOVE,wrap=WORD)
    #STT_TEXTBOX.place(x=10,y=150,width=500,height=250)


    #logo
    Logo=PhotoImage(file='purplemic3.png')
    Label(Topframe,image=Logo,bg="white").place(x=10,y=5)
    Label(Topframe,text="SPEECH TO TEXT",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

    #TEXT BOX
    text = Text(r1, font=12, height=26, width=45)
    #text.insert(INSERT, recog)
    text.place(x=10, y=150)
     
    #add image to button 
    #setting buttons as images
    photostt=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\speechtotext.png")

    # Resizing image to fit on button
    photoimage= photostt.subsample(3, 3)
    
    recordbutton = Button(r1,text='SPEECH TO TEXT', command=showMsg,image=photoimage,bg="white")
    recordbutton.place(x=520,y=170)

    def delete():
        text.delete("1.0","end")

   
    #clear button
    clearbtn=Button(r1,text="CLEAR",command=delete,bg="white")
    clearbtn.place(x=520,y=220,height=20,width=150)

    #icon image
    r1.iconbitmap('mic2.ico')
    
    #creating a frame to diplay videos

    
    Vidframe=Frame(r1,bg="white",width =500,height=500)
    Vidframe.place(x=750,y=140)
    Label(r1,text="RELATED VIDEOS",font="arial 20 bold",bg="white",fg="black").place(x=750,y=101)
    
    #for playbackk of videos on screen

    def playvideo1():
    #play video from youtube url
     url1 = "https://www.youtube.com/watch?v=u288zZf2C6k"
     video1 = pafy.new(url1)
     #get the best quality of the vide
     best1 = video1.getbest()
     #play using vlc media library
     media1 = vlc.MediaPlayer(best1.url)
     #media1 = vlc.MediaPlayer(best1.url)
     media1.play()

    def playvideo2():
      #play video from youtube url
      url2 = "https://www.youtube.com/watch?v=RuGmc662HDg&list=PLF9mJC4RrjIhS4MMm0x72-qWEn1LRvPuW"

      video2 = pafy.new(url2)
      #get the best quality of the video
      best2 = video2.getbest()
      #play using vlc media library
      media2 = vlc.MediaPlayer(best2.url)
      media2.play()

    def playvideo3():
      #play video from youtube url
     url3 = "https://www.youtube.com/watch?v=juKd26qkNAw"
        #get the best quality of the video
     video3 = pafy.new(url3)
     best3 = video3.getbest()
     #play using vlc media library
     media3 = vlc.MediaPlayer(best3.url)
     media3.play()

    def playvideo4():
     #play video from youtube url
     url4 = "https://www.youtube.com/watch?v=8YV8KmfBbBM"
     video4 = pafy.new(url4)
     #get the best quality of the video
     best4 = video4.getbest()
     #play using vlc media library
     media4 = vlc.MediaPlayer(best4.url)
     media4.play()

    def playvideo5():
     #play video from youtube url
     url5 = "https://www.youtube.com/watch?v=ujDtm0hZyII"
     video5 = pafy.new(url5)
     #get the best quality of the video
     best5 = video5.getbest()
     #play using vlc media library
     media5 = vlc.MediaPlayer(best5.url)
     media5.play()

    

    #setting buttons as images
    photo1=PhotoImage(file="spanish_thumbnail.png")
    
    photoimage1=photo1.subsample(7,7)
    playvideo_btn1=tkinter.Button(Vidframe,image=photoimage1,command=playvideo1)
    vbtn1=Label(Vidframe,text="Learn Spanish Lesson 1 - Greetings ",font="arial 12 bold",fg="black")
    vbtn1.place(x=200,y=20)
    playvideo_btn1.place(x=10,y=10)

    #setting buttons as images
    photo2=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\gl.png")

    #  Resizing image to fit on button
    photoimage2 = photo2.subsample(7, 7)
    playvideo_btn2=Button(Vidframe,text="GERMAN LESSONS",command=playvideo2,image=photoimage2)
    vbtn2=Label(Vidframe,text="Begrüßungen German for beginners",font="arial 12 bold",fg="black")
    vbtn2.place(x=200,y=120)
    playvideo_btn2.place(x=10,y=110)

     #setting buttons as images
    photo3=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\eng.png") 

    # Resizing image to fit on button
    photoimage3 = photo3.subsample(5, 7)
    playvideo_btn3=Button(Vidframe,text="ENGLISH LESSON",command=playvideo3,image=photoimage3)
    vbtn2=Label(Vidframe,text=" ALL the English Basics You Need",font="arial 12 bold",fg="black")
    vbtn2.place(x=200,y=220)
    playvideo_btn3.place(x=10,y=210)

    #setting buttons as images
    photo5=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\fra.png")

    # Resizing image to fit on button
    photoimage5= photo5.subsample(7, 7)
    playvideo_btn5=Button(Vidframe,text="FRENCH LESSONS",command=playvideo5,image=photoimage5)
    vbtn2=Label(Vidframe,text="ALL the French Basics You Need",font="arial 12 bold",fg="black")
    vbtn2.place(x=200,y=320)
    playvideo_btn5.place(x=10,y=310)

    #setting buttons as images
    photo4=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\jap.png")

    # Resizing image to fit on button
    photoimage4 = photo4.subsample(5, 7)
    playvideo_btn4=Button(Vidframe,text="JAPANESE LESSONS",command=playvideo4,image=photoimage4) 
    vbtn2=Label(Vidframe,text="ALL the Japanese Basics You Need",font="arial 12 bold",fg="black")
    vbtn2.place(x=200,y=420)
    playvideo_btn4.place(x=10,y=410)

    


    r1.mainloop()




bgt=None


def TSS_WINDOW():

    global text_area
    global text_area2
    global root
    global canvastss
    root = tkinter.Toplevel()  

    root.geometry('900x400+200+200')  
    root.title("TEXT TO SPEECH")
    #root.resizable(False,False)
    root.configure(bg="#BFBFEF")
    root.state('zoomed')

 
    Label(root,text="Enter the text",font="arial 20 bold",fg="black").place(x=10,y=110)

    #TEXT BOX
    text_area=Text(root,font="arial 20",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=10,y=150,width=500,height=200)
     

     #textbox 2 for translated text
    text_area2=Text(root,font="arial 20",bg="white",relief=GROOVE,wrap=WORD)
    #text_area2.insert(INSERT, translation)
    text_area2.place(x=10,y=410,width=500,height=200)

    #COMBOBOX to show languages

    global select_lang

    sl=tkinter.StringVar()
    select_lang=ttk.Combobox(root,width=28,textvariable=sl,state="readonly")
    select_lang['values']=('English','German','Hindi','Spanish')
    select_lang.set("select a language")
    select_lang.place(x=15,y=360)
    
    #BUTTON TO TRANSLATE THE TEXT

    tbtn=Button(root,text="TRANSLATE",bg="white", font="arial 14 bold",command=Translate_text)
    tbtn.place(x=250,y=360)



     
    #button tss
    #adding image to a button
    phototts=tkinter.PhotoImage(file="texttospeech.png")

    # Resizing image to fit on button
    photoimage= phototts.subsample(2, 2)

    #BUTTON FOR TEXT TO SPPEECH
    btn=Button(root,text="Text to Speech",bg="white",image=photoimage, font="arial 14 bold",command=readMsg)
    btn.place(x=550,y=280)
    
    #BUTTON FOR TEXT TO SPEECH2
    BTN2=Button(root,text="Translated Text to Speech",bg="white",font="arial 14 bold",command=readTranslatedMsg)
    BTN2.place(x=550,y=340)

    #TOPFRAME
    Topframe=Frame(root,bg="white",width =1500,height=100)
    Topframe.place(x=0,y=0)
    Label(Topframe,text="TEXT TO SPEECH",font="arial 25 bold",bg="#FFFFF6",fg="black").place(x=110,y=30)
   
    #icon
    root.iconbitmap('mic2.ico')
    
    Logo1=PhotoImage(file=r'purplemic3.png')
    Label(Topframe,image=Logo1,bg="white").place(x=15,y=5)

   


    #hyperlinks to various websites

    #Define a callback function TO open the websites
    def callback(url):

     webbrowser.open_new_tab(url)

    #create a frame to add the hyperlinks
    frame2=Frame(root,bg='white',width=900,height =200)
    frame2.place(x=1000,y=110)

    text= Label(frame2, text= "Related Websites",bg="white", font= ('Helvetica bold', 14))
    text.pack(pady=10)

    #scroll bar
    sb = Scrollbar(frame2)
    sb.pack(side=RIGHT,fill='y')
    # here command represents the method to be executed yview
    #myscrollbar.config(command=frame2.yview)


    #Create a Label to display the link
    link1 = Label(frame2, text="www.learnlanguagefast.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link1.pack(padx=10,pady=5)
    link1.bind("<Button-1>", lambda e:
    callback("https://www.fluentu.com/blog/fastest-way-to-learn-a-new-language/"))
    
    #Create a Label to display the link
    link2 = Label(frame2 ,text="free language lessons",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link2.pack(padx=10,pady=5)
    link2.bind("<Button-1>", lambda e:
    callback("https://www.openculture.com/freelanguagelessons"))
    
    #Create a Label to display the link
    link3 = Label(frame2 ,text="www.tutorialspoint.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link3.pack(padx=10,pady=5)
    link3.bind("<Button-1>", lambda e:
    callback("http://www.tutorialspoint.com"))

    #Create a Label to display the link
    link4 = Label(frame2, text="www.duolingo.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link4.pack(padx=10,pady=5)
    link4.bind("<Button-1>", lambda e:
    callback("https://englishtest.duolingo.com/applicants"))

    #Create a Label to display the link
    link5 = Label(frame2, text="www.studyingeman.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link5.pack(padx=10,pady=5)
    link5.bind("<Button-1>", lambda e:
    callback("https://www.studying-in-germany.org/learn-german/"))

    link6= Label(frame2, text="www.dulingogerman.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link6.pack(padx=10,pady=5)
    link6.bind("<Button-1>", lambda e:
    callback("https://www.duolingo.com/course/fr/en/Learn-French/"))

    link7 = Label(frame2, text="www.learnjapanese.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link7.pack(padx=10,pady=5)
    link7.bind("<Button-1>", lambda e:
    callback("https://mochidemy.com/kana/?gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HBVS6CBB1ELzUeYdAJVGqBF2X0lVNjDg5IPfjclUUBWOEzLuwavfuEaAg5hEALw_wcB"))

    link8 = Label(frame2, text="www.learnhinduolingo.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link8.pack(padx=10,pady=5)
    link8.bind("<Button-1>", lambda e:
    callback("https://www.duolingo.com/course/hi/en/Learn-Hindi"))

    link9 = Label(frame2, text="www.howtolearnalanguage.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link9.pack(padx=10,pady=5)
    link9.bind("<Button-1>", lambda e:
    callback("https://www.futurelearn.com/info/blog/how-to-learn-a-language"))

    link10 = Label(frame2, text="www.everythinghhere.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link10.pack(padx=10,pady=5)
    link10.bind("<Button-1>", lambda e:
    callback("https://www.loecsen.com/en/learn-japanese"))

    ##Create a Label to display the link
    link11 = Label(frame2, text="www.hello.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link11.pack(padx=10,pady=5)
    link11.bind("<Button-1>", lambda e:
    callback("https://www.fluentu.com/blog/fastest-way-to-learn-a-new-language/"))

  ##Create a Label to display the link

    link12 = Label(frame2, text="www.hello2.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link12.pack(padx=10,pady=5)
    link12.bind("<Button-1>", lambda e:
    callback("https://www.fluentu.com/blog/fastest-way-to-learn-a-new-language/"))

    ##Create a Label to display the link
    link11 = Label(frame2, text="www.tipstolearnnewlanguages.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link11.pack(padx=10,pady=5)
    link11.bind("<Button-1>", lambda e:
    callback("https://www.bbc.com/worklife/article/20150302-secrets-to-learning-a-language"))

    ##Create a Label to display the link
    link11 = Label(frame2, text="www.learnanylanguagesfast.com",font=('Helveticabold', 12), bg="white",fg="blue", cursor="hand2")
    link11.pack(padx=10,pady=5)
    link11.bind("<Button-1>", lambda e:
    callback("https://preply.com/en/blog/10-tips-learn-languages-fast/"))



    #icon
    #master1=root
    #i2=PhotoImage(file='mic4.png')
    #r1.iconphoto(False,i2)
    ##l2=PhotoImage(file='s5.png')
    #Label(master1,Topframe,image=l2,bg="white").place(x=10,y=5)
   
    root.mainloop()

#TO TRANSLATE TEXT
def Translate_text():
    global translation

    if select_lang.get()=="English":
        translator= Translator(to_lang="English")
    elif select_lang.get()=="German":
        translator=Translator(to_lang="German")
    elif select_lang.get()=="Hindi":
        translator=Translator(to_lang="Hindi")
    elif select_lang.get()=="Spanish":
        translator=Translator(to_lang="Spanish")
    else:
        translator=Translator(to_lang="English")
   
    translation = translator.translate(text_area.get("1.0", "end-1c"))
    print (translation)
    text_area2.insert(INSERT, translation)

    

#HOMEWINDOW GUI

r3=tkinter.Tk()
r3.geometry("900x400+200+200")
r3.state('zoomed')
r3.title("HOME PAGE")
r3.configure(bg="#305065")

frame1=Frame(r3,bg='navy blue',width=800,height =200)
#frame1.place(x=10,y=120)



# to set image as background
# Add image file
bg = PhotoImage(file = "backgroundimg.png")
  
# Create Canvas
canvas1 = Canvas( r3, width = 800,height = 1000)
#canvas1.place(x=5,y=120)
canvas1.pack(fill="both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#white topframe
Topframe=Frame(canvas1,bg='#FFFFF6',width=1500,height =90)
Topframe.place(x=0,y=0)
Label(Topframe,text="TRANSLATION APP",font="arial 25 bold",bg="#FFFFF6",fg="black").place(x=110,y=30)

#setting buttons as images
photostt=PhotoImage(file = r"C:\Users\Admin\OneDrive\Desktop\clg\speechtotext.png")

# Resizing image to fit on button
photoimage= photostt.subsample(7, 7)
btn2=Button(canvas1,text="SPEECH TO TEXT",command=STT_window,image=photostt)
btn2.place(x=650,y=200)

#setting buttons as image
phototts=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\clg\texttospeech.png")

btn1=Button(canvas1,text="TEXT TO SPEECH",command=TSS_WINDOW,image=phototts)
#btn1.pack(padx=20,pady=20)#btn1.pack()
btn1.place(x=650,y=370)
  
frame1.picture = PhotoImage(file="C:\\Users\\Admin\\OneDrive\\Desktop\\clg\\gui.png")
frame1.label = Label(r3, image=frame1.picture)
#frame1.label.pack(side=LEFT)


#icon

iconimage=PhotoImage(file='mic2.png')
r3.iconphoto(False,iconimage)
Logo=PhotoImage(file='purplemic3.png')
Label(Topframe,image=Logo,bg="white").place(x=15,y=5)







r3.mainloop()

