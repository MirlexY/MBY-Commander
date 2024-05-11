import tkinter.messagebox as messagebox
import subprocess
from tkinter import *
import customtkinter
import os
from PIL import Image
import customtkinter as ctk
from PIL import Image, ImageTk

messagebox.showinfo("⭐DİKKAT⭐", "Merhaba❗ Lütfen Daha Sonradan Problem Yaşamamak İçin Sistem Ve Regedit Yedeğinizi Alınız( Uygulamanın İçinde Bulunmaktadır ).Ve butonların ne işe yaramadığını bilmiyorsanız tıklayarak öğrenebilirsiniz.") 
def Sistemyedek():
    messagebox.showinfo("❗DİKKAT❗", "Açılan Pencerede Oluştur Açık Değilse Diskinizi Seçip Yapılandıra Basınız Çıkan Pencereden Sistem Korumasını Aç'ı Seçin Ve Tamam Deyin Sonrasında Oluştur Sekmesine Basın Yedeğinize İsim Verin İşlem Bu Kadar !")
    
def goster_popup():
    messagebox.showinfo("❗DİKKAT❗", "|Lütfen Daha Sonradan Problem Yaşamamak İçin Sistem Ve Regedit Yedeğinizi Alınız.Ve butonların ne işe yaramadığını bilmiyorsanız tıklayarak öğrenebilirsiniz.|") 
def run_bat_file(file_path):
    os.startfile(file_path)
def button_click(file_path):
    run_bat_file(file_path)





def bilgi():
    cevap = messagebox.askquestion("Onay", "İnternetiniz yavaşlıyorsa ve Winsock'u sıfırlamak istiyorsanız evet butonuna basınız. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/ağ sıfırlama.bat"])
def bilgi1():
    cevap = messagebox.askquestion("Onay", "Bu işlem, Winsock, TCP/IP, WinHTTP ve DNS önbelleğini temizler , Windows güvenlik duvarı ayarlarını sıfırlar ve gereksiz dosyaları siler.İnternetinizde problem ve yavaşlama yaşıyorsanuz evet butonuna basınız. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Ayrıntılı Ağ sıfırlama ve ip değiştirme.bat"])
def bilgi2():
    cevap = messagebox.askquestion("Onay", "Bu komut disk hatalarını denetler ve onarır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Disk hata ve onarım.bat"])
def bilgi3():
    cevap = messagebox.askquestion("Onay", "Bu komut Disk Temizleme Araçlarını çalıştırır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Disk temizleme.bat"])
def bilgi4():
    cevap = messagebox.askquestion("Onay", "Bu komut DNS önbelleğini temizler. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/DNS ÖNBELLEĞİ TEMİZLEME.bat"])
def bilgi5():
    cevap = messagebox.askquestion("Onay", "Bu komut, kullanılmayan boş alanı temizler ve kullanılan verileri geri alınamaz hale getirir. Doğru sürücüyü seçtiğinizden ve verilerin geri kurtarılmasını istemediğinizden emin olun. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/DOSYALARI PCDEN KURTARILAMYIACAK ŞEKİLDE SİLME.bat"])
def bilgi6():
    cevap = messagebox.askquestion("Onay", "Bu kod gereksiz hizmetleri kapatır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Gereksiz hizmetleri kapatma ayrıntılı.bat"])
def bilgi7():
    cevap = messagebox.askquestion("Onay", "Bu komut satırı görsel efektleri kapatma penceresini açar. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Görsel efektleri kapatma.bat"])         
def bilgi8():
    cevap = messagebox.askquestion("Onay", "Bu komut dosyası hibernate modunu kapatmak için kullanılır.Hibernation kapandığında, bilgisayarınız kapatılırken veya uyku moduna alınırken hibernate kullanılmayacaktır. Bu, bilgisayarın daha hızlı kapanmasını ve uykudan daha hızlı uyanmasını sağlar, ancak çalışma durumunu kurtarma seçeneğini kaybedersiniz. Yani, askıya almayı devre dışı bırakır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Hibernasyon Kapama(DAHA HIZLI AÇILIŞ).ba"])
def bilgi9():
    cevap = messagebox.askquestion("Onay", "Bu komut, yalnızca bilgisayarınızın donanım performansını değerlendirmek ve değerlendirme sonuçlarını sunmak için kullanılır. Değerlendirme sonuçları, donanımınızın hangi bileşenlerinin daha yavaş veya daha hızlı olduğunu anlamanıza yardımcı olabilir. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/PC PERFORMANS TESTİ.bat"])
def bilgi10():
    cevap = messagebox.askquestion("Onay", "Bu komut, bilgisayarınızdaki gereksiz dosyaları siler. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/PC TEMİZLEME GEREKSİZ DOSYALAR TEMP VS.bat"])
def bilgi11():
    cevap = messagebox.askquestion("Onay", "Bu komut, bilgisayarınızdaki bellekleri test eder ve sorun varsa onarmaya çalışır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/RAM TEMİZLEME ONARMA.bat"])
def bilgi12():
    cevap = messagebox.askquestion("Onay", "u komut, Windows işletim sistemindeki sistem dosyalarının bütünlüğünü kontrol eder ve hasarlı veya bozuk olan sistem dosyalarını algılar ve otomatik olarak onarır. Bu işlem, bilgisayarın daha stabil ve performansının daha iyi olmasına yardımcı olabilir. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/SFC ONARMA.bat"])
def bilgi13():
    cevap = messagebox.askquestion("Onay", "Bu komut, bilgisayarınızdaki yüklü olan tüm uygulamaların güvenliğini artırmaya ve en son özellikleri ile düzeltmeleri elde etmenize yardımcı olur. Böylece, el ile her bir uygulamanın güncellemesini yapmak yerine tek bir komut kullanarak tüm uygulamaları güncelleyebilirsiniz. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Tüm driver ve uygulamaları günceller.bat"])
def bilgi14():
    cevap = messagebox.askquestion("Onay", "u komut, Windows Güncelleme İndirme Geçmişini temizler. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/Update geçmişi siler.bat"])
def bilgi15():
    cevap = messagebox.askquestion("Onay", "DISM komutları çalıştırılacaktır. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/UUDISM ONARMA 7Li.bat"])
def bilgi16():
    cevap = messagebox.askquestion("Onay", "GÜÇ PLANINA NİHAİ PERFORMANS MODUNU EKLER VE AKTİF EDER. | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/a"])
def bilgi17():
    cevap = messagebox.askquestion("Onay", "HPET KAPATMA. Devam etmek istiyor musunuz?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/a"])
def bilgi18():
    cevap = messagebox.askquestion("Onay", "Bu işlem, işlemcinin boşta olduğunda enerji tasarrufu önleme işlemini devre dışı bırakır (Eğer işlemci boştayken %100 CPU sorununuz varsa evet butonuna basınız). | Devam etmek istiyor musunuz ?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/%100CPU SORUNU.bat"])
def bilgi19():
    cevap = messagebox.askquestion("Onay", "eklenecek. Devam etmek istiyor musunuz?")
    if cevap == "yes":
        subprocess.Popen(["python","Batlar/a"])



       




customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(root):
        super().__init__()
       
        
        
       
        # pencereleri konfigre ettim
        root.title("WORK WORK WORK!")
        root.geometry(f"{1250}x{425}")

        #grid ayarı
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)
        root.grid_columnconfigure(6, weight=0)
      
        #sidebar frame VE widgetlar burada
        root.sidebar_frame = ctk.CTkFrame(root, width=140, corner_radius=0)
        root.sidebar_frame.grid(row=0, column=6, rowspan=7, sticky="nsew")


        for i in range(5):
            root.sidebar_frame.grid_rowconfigure(i, weight=1)
            root.sidebar_frame.grid_columnconfigure(i, weight=1)
        
        
        
        #LOGOLAR
        
        root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="MBY TOOLBOX", font=customtkinter.CTkFont(size=22, weight="bold"))
        root.logo_label.grid(row=0, column=4, padx=10, pady=(20, 10))


        root.appearance_mode_label = customtkinter.CTkLabel(root.sidebar_frame, text="Temanızı seçiniz:", anchor="w")
        root.appearance_mode_label.grid(row=5, column=4, padx=20, pady=(10, 0))
        root.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=root.change_appearance_mode_event)
        root.appearance_mode_optionemenu.grid(row=6, column=4, padx=20, pady=(10, 10))


        root.scaling_label = customtkinter.CTkLabel(root.sidebar_frame, text="Ölçeklendirme:", anchor="w")
        root.scaling_label.grid(row=7, column=4, padx=20, pady=(10, 0))
        root.scaling_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["70%","80%", "90%", "100%", "110%", "120%","130%","140%","150%"],
                                                               command=root.change_scaling_event)
        root.scaling_optionemenu.grid(row=8, column=4, padx=20, pady=(10, 20))
        

         
        root.button = customtkinter.CTkButton(root.sidebar_frame, text="Sistem Yedeğini Alma",command=Sistemyedek,fg_color="gray",text_color="white")
        root.button.grid(row=9, column=4, padx=20, pady=(10,20))
    
        for i in range(5):
            root.button.grid_rowconfigure(i,weight=1)
            root.button.grid_columnconfigure
        






        #Başlangıç Ayarları
        # Bu yukardaki sayfa labelle de ilgili
        root.appearance_mode_optionemenu.set("System")
        root.scaling_optionemenu.set("100%")
        root.title("MBY COMMANDER LAUNCHER")
        



        #Tab kısmı 
        root.tabview = customtkinter.CTkTabview(root, width=250)
        root.tabview.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        root.tabview.add("Komutlar")
        for i in range(5):
            root.tabview.tab("Komutlar").grid_columnconfigure(i, weight=1)
        
        
        root.tabview.add("Regedit")
        for i in range(5):
            root.tabview.tab("Regedit").grid_columnconfigure(i, weight=1) 
        
        root.tabview.add("Uygulamalar")
        for i in range(5):
            root.tabview.tab("Uygulamalar").grid_columnconfigure(i, weight=1) 
        
        root.tabview.add("Bilgi")
        for i in range(5):
            root.tabview.tab("Bilgi").grid_columnconfigure(i, weight=1) 
        
        root.tabview.add("Yardım")
        for i in range(5):
            root.tabview.tab("Yardım").grid_columnconfigure(i, weight=1) 
        
       
        
        yazi_etiketi = Label(root.tabview.tab("Bilgi"), text="\n  Miraç Baran YAMAN tarafından yapılmıştır  \nGithub:xxxxx\nLinkedin:xxxxxxx\n", state='disabled', font=("Arial Black", 35),fg="white")
        yazi_etiketi.grid(row=0, column=0, columnspan=5)   
        

        


    




        
          
        root.button = customtkinter.CTkButton(root.sidebar_frame,text="⚠️",command=goster_popup,width=30,fg_color="gray",text_color="brown")
        root.button.grid(row=0, column=3, padx=10, pady=(20, 10))
        
        
        
        
        
        
        metins=["Ağ Winsock Sıfırlama","Ağ Sıfırlama Ve İp Değiştirme","Disk Hata Ve Onarım","Disk Temizleme","DNS Önbelleği Temizleme","Dosyaları Tamamen Silme",
               "Gereksiz Hizmetleri Kapatma", "Görsel Efektleri Kapatma","Hibernasyon Kapatma","PC Performans Testi","Gereksiz Dosyaları Temizleme","Ram Test Ve Onarım",
              "SFC Onarma", "Her Şeyi Güncelleme","Update Geçmişini Temizleme","DISM Onarma","Nihai Performans Güç Modu","Hpet Kapatma","%100 CPU Çözümü","EKLENECEK"]
        komuts=[bilgi,bilgi1,bilgi2,bilgi3,bilgi4,bilgi5,bilgi6,bilgi7,bilgi8,bilgi9,bilgi10,bilgi11,bilgi12,bilgi13,bilgi14,bilgi15,bilgi16,bilgi17,bilgi18,bilgi19]
       
        butonlar0=[]
        ctk_images_gecici = []
        for c in range(20):
            resim2 = Image.open("Logos/bat.png")
            ctk_image = ctk.CTkImage(resim2)
            ctk_images_gecici.append(ctk_image)
            root.button = customtkinter.CTkButton(root.tabview.tab("Komutlar"),image='', text=metins[c],command=komuts[c], width=195,height=30)
            butonlar0.append(root.button)

        def basılınca2(event, button, ctk_image):
            button.configure(text="Çalıştır")
            button.configure(image=ctk_image)

        def cikinca2(event, button, text):
            button.configure(text=text)
            button.configure(image='')
        
        row = 0
        column = 0

        for i, buton in enumerate(butonlar0):
            buton.grid(row=row, column=column, padx=10, pady=10)
            buton.bind("<Enter>", lambda event, button=buton, ctk_image=ctk_images_gecici[i]: basılınca2(event, button, ctk_image))
            buton.bind("<Leave>", lambda event, button=buton, text=metins[i]: cikinca2(event, button, text))
            column+=1
            if column==4:
                row+=1
                column=0


    



        dosya=["Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a"]
        metin = ["Arka Plan Erişimini Kapat","DVR Özelliklerini Kapat","GPU Kısıtlamasını Kapat","Güç Kısıtlamasını Kapat","Ağ Performansını Optimize Et","Sistem Öncelik Optimizasyonu","Sistem Bekleme Ayarları","Bakımı Devre Dışı Bırak","Oyun Modunu Aktifleştir",
         "Windows Ayarları Optimize1","Windows Ayarları Optimize2","Animasyonları Kapat","Veri Toplamaları Kapat","OneDrive Senk. Kapat","Cortanayı KaLDIRILMIŞ","Haritaları Kapat","W10 Sağ Tık Geri Getir","Sysmain Kapat","Mouse Optimize Et","Kısayol İşaretini Kaldır"]

        butonlar = []
        ctk_images_gecici = []
        for i in range(20):
            resim2 = Image.open("Logos/cmd.png")
            ctk_image = ctk.CTkImage(resim2)
            ctk_images_gecici.append(ctk_image)
            button = ctk.CTkButton(root.tabview.tab("Regedit"), text=metin[i],image='', command=lambda file=dosya[i]: button_click(file), width=205,height=30)  
            butonlar.append(button)

        def basılınca2(event, button, ctk_image):
            button.configure(text="Çalıştır")
            button.configure(image=ctk_image)

        def cikinca2(event, button, text):
            button.configure(text=text)
            button.configure(image='') 

        row = 0
        column = 0

        for i, buton in enumerate(butonlar):
            buton.grid(row=row, column=column, padx=10, pady=10)
            buton.bind("<Enter>", lambda event, button=buton, ctk_image=ctk_images_gecici[i]: basılınca2(event, button, ctk_image))
            buton.bind("<Leave>", lambda event, button=buton, text=metin[i]: cikinca2(event, button, text))
            column += 1
            if column == 4:
                row += 1
                column = 0

                



      







        
 


     
        

       
        komutlar=["start cmd /c winget install -e --id Brave.Brave",
                  "start cmd /c winget install 7zip",
                  "start cmd /c winget install Google.Chrome",
                  "start cmd /c winget install -e --id AnyDeskSoftwareGmbH.AnyDesk",
                  "start cmd /c winget install -e --id Klocman.BulkCrapUninstaller",
                  "start cmd /c winget install -e --id BleachBit.BleachBit",
                  "start cmd /c winget install -e --id Discord.Discord",
                  "start cmd /c winget install -e --id TheDocumentFoundation.LibreOffice",
                  "start cmd /c winget install -e --id LibreWolf.LibreWolf",
                  "start cmd /c winget install Malwarebytes",
                  "start cmd /c winget install -e --id Notepad++.Notepad++",
                  "start cmd /c winget install -e --id ONLYOFFICE.DesktopEditors",
                  "start cmd /c winget install -e --id ProtonTechnologies.ProtonVPN",
                  "start cmd /c winget install -e --id RevoUninstaller.RevoUninstaller",
                  "start cmd /c winget install -e --id Valve.Steam",
                  "start cmd /c winget install -e --id Rufus.Rufus",
                  "start cmd /c winget install -e --id Oracle.VirtualBox",
                  "start cmd /c winget install -e --id VideoLAN.VLC",
                  "start cmd /c winget install -e --id RARLab.WinRAR",
                  "start cmd /c winget install -e --id Adobe.Acrobat.Reader.64-bit",
                  "start cmd /c winget install -e --id Notion.Notion",
                  "start cmd /c winget install -e --id EpicGames.EpicGamesLauncher",
                  "start cmd /c winget install -e --id BandicamCompany.Bandicam",
                  "start cmd /c winget install -e --id CPUID.HWMonitor",
                  "start cmd /c winget install -e --id Spotify.Spotify"] 
        resimler=["Logos/brave.png","Logos/7zip.png","Logos/chrome.png","Logos/anydesk.png","Logos/bcu.png","Logos/bleachbit.png","Logos/discord.png","Logos/libreoffice.png","Logos/librewolf.png","Logos/malwarebytes.png","Logos/notepad.png","Logos/onlyoffice.jpeg","Logos/protonvpn.png","Logos/revo.png","Logos/steam.png",
                  "Logos/rufus.png","Logos/virtualbox.png","Logos/vlc.png","Logos/winrar.png","Logos/adobe.png",
                  "Logos/notion.png",
                  "Logos/epic.png",
                  "Logos/bandicam.png",
                  "Logos/hwmonitor.png",
                  "Logos/spotify.png"] 
        metinler=["Brave","7Zip", "Google Chrome","Anydesk","BCU Uninstaller","Bleachbit","Discord","Libreoffice","Librewolf","Malwarebytes","Notepad++","Onlyoffice","ProtonVPN","Revo Uninstaller","Steam","Rufus","Virtualbox","VLC Oynatıcı","Winrar","Adobe Acrobat",
                  "Notion","Epic Games Launcher","Bandicam","HWMonitor","Spotify"]  

        def runkomut(komut):
            def run():
                os.system(komut)
            return run

        def basılınca(event, button, ctk_image):
            button.configure(text="Yükle")
            button.configure(image=ctk_image)

        def cikinca(event, button, text, ctk_image):
            button.configure(text=text)
            button.configure(image=ctk_image)

        butonlar2 = []
        ctk_images = []
        ctk_images_gecici = []
        for i in range(25):
            resim = Image.open(resimler[i])
            ctk_image = ctk.CTkImage(resim)
            ctk_images.append(ctk_image)
            ctk_images_gecici.append(ctk.CTkImage(Image.open("Logos/install.png")))
            buton = ctk.CTkButton(root.tabview.tab("Uygulamalar"), text=metinler[i], image=ctk_image, command=runkomut(komutlar[i]), anchor="w", width=165, height=45)
            butonlar2.append(buton)

        row = 0
        column = 0
                    
        for i, buton in enumerate(butonlar2):
            buton.grid(row=row, column=column, padx=10, pady=10)
            buton.bind("<Enter>", lambda event, button=buton, ctk_image=ctk_images_gecici[i]: basılınca(event, button, ctk_image))
            buton.bind("<Leave>", lambda event, button=buton, text=metinler[i], ctk_image=ctk_images[i]: cikinca(event, button, text, ctk_image))
            column+=1
            if column==5:
                row+=1
                column=0

                
            
            







        dosya=["Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a","Batlar/a"]
        metin = ["Yazdırma Birikticisi","Windows Resim Alma (WIA)","Windows Mobil Etkin Nokta Hizmeti","Windows Kamera Hizmeti","Windows Biyometrik Hizmeti","Telefon Hizmeti","Coğrafi Konum Hizmeti","SysMain","Windows Search Hizmeti",
                 "ekle","ekle","ekle" ]

        butonlar = []
        ctk_images_gecici = []
        for i in range(12):
            resim2 = Image.open("Logos/cmd.png")
            ctk_image = ctk.CTkImage(resim2)
            ctk_images_gecici.append(ctk_image)
            button = ctk.CTkButton(root.tabview.tab("Yardım"), text=metin[i],image='', command=lambda file=dosya[i]: button_click(file), width=205,height=40)  
            butonlar.append(button)

        def basılınca2(event, button, ctk_image):
            button.configure(text="Hizmeti Aç")
            button.configure(image=ctk_image)

        def cikinca2(event, button, text):
            button.configure(text=text)
            button.configure(image='') 

        row = 0
        column = 0

        for i, buton in enumerate(butonlar):
            buton.grid(row=row, column=column, padx=10, pady=10)
            buton.bind("<Enter>", lambda event, button=buton, ctk_image=ctk_images_gecici[i]: basılınca2(event, button, ctk_image))
            buton.bind("<Leave>", lambda event, button=buton, text=metin[i]: cikinca2(event, button, text))
            column += 1
            if column == 4:
                row += 1
                column = 0

                
                 
            
            
        
        
        
        applications_tab=root.tabview.tab("Uygulamalar")
        for i in range(5):
            applications_tab.columnconfigure(i, weight=1)
            applications_tab.rowconfigure(i, weight=1)
                

        applications_tab2=root.tabview.tab("Regedit")
        for i in range(5):
            applications_tab2.columnconfigure(i, weight=1)
            applications_tab2.rowconfigure(i, weight=1)

        
        applications_tab3=root.tabview.tab("Komutlar")
        for i in range(5):
            applications_tab3.columnconfigure(i, weight=1)
            applications_tab3.rowconfigure(i, weight=1)

    
        applications_tab4=root.tabview.tab("Bilgi")
        for i in range(5):
            applications_tab4.columnconfigure(i, weight=1)
            applications_tab4.rowconfigure(i, weight=1)


        applications_tab5=root.tabview.tab("Yardım")
        for i in range(5):
            applications_tab5.columnconfigure(i, weight=1)
            applications_tab5.rowconfigure(i, weight=1)







       
        
   
    def change_appearance_mode_event(root, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(root, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(root):
        print("sidebar_button click")
  
    
root = App()
root.mainloop()