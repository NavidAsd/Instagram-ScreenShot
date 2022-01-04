#region Libraries
#.
#..
#...
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import subprocess
import pyautogui
import datetime
import platform
import time
import csv
import sys
import wx
import os
#...
#..
#.
#endregion


class Instagram:
    def __init__(self,User,Pass,Target,count,screencount,width,height,aria,len,directory,last_story,click):
        self.len=len
        self.User=User
        self.Pass=Pass
        self.aria=aria
        self.click=click
        self.count=count
        self.width=width
        self.height=height
        self.directory=directory
        self.last_story=last_story
        self.screencount=screencount

        #...#
        self.option = webdriver.ChromeOptions()
        
    #region ObjectFinder       
    def WaitForObject(self,type,string):
        return WebDriverWait(self.browser,4).until(EC.presence_of_element_located((type,string)))

    def WaitForObjects(self,type,string):
        return WebDriverWait(self.browser,4).until(EC.presence_of_all_elements_located((type,string))) 
    #endregion

    def Configuration(self):
        file=open('./Files/log.txt','w+')
        file.write(str(datetime.datetime.now()))
        file.write('\n')
        file.write(f'os type: {platform.system()}')
        file.write('\n')
        file.write('data storage type: TXT(file)')
        file.write('\n')
        file.write('--------------------------------')
        file.close()
        Bot.Get_Defult_Account()

    def Configuration_initial(self):
        
        os.system('mode 75,45')
        resolution = pyautogui.size()

        resault=str(resolution).replace('Size','').replace('(','').replace(')','').replace('width=','').replace(', height=','')
        if(resault.__len__()==7 or resault.__len__()==8):
            self.width=int(resault[:4])
            self.height=int(resault[4:])
            self.width=(self.width/2)+15
            self.height-=30
        elif(resault.__len__()==6):
            self.width=int(resault[:3])
            self.height=int(resault[3:])
            self.width=(self.width/2)+20
            self.height-=30
        Bot.Configuration()

    def Get_Defult_Account(self):
        try:
            file=open('./Files/Accounts/default.txt','r')
            data=csv.reader(file,delimiter=':')
            for row in data:
                self.User=("".join(row[:1]).strip())
                self.Pass=("".join(row[1:2]).strip())
            if(self.User!=None or self.User!="" or self.User!=" " or self.Pass!=None or self.Pass!="" or self.Pass!=" "):
                Bot.Get_Target()
            else:
                print('\33[31m'+"Your Username or Password in [default.txt] is empty!"+'\33[37m')
                time.sleep(1)
                subprocess.run(['notepad.exe', './Files/Accounts/default.txt'])
                Bot.Get_Defult_Account()
        except:
            print('\33[31m'+'"default.txt" file not found in "./Files/Accounts/" path!'+'\33[37m')
            inp=input('\33[32m'+'Make the file (y/n)? ')
            if(inp=='y'or inp=='Y'or inp=='yy'or inp=='yes' or inp =='YES'):
                file=open('./Files/Accounts/default.txt','w')
                file.write('USERNAME:PASSWORD')
                file.close()
                print('\33[32m'+'After adding the data and "closing" the text file, you can use the program.'+'\33[37m')
                print()
                subprocess.run(['notepad.exe', './Files/Accounts/default.txt'])
                Bot.Get_Defult_Account()
            else:
                Bot.Exit()
                
    def Get_Target(self):
        try:
            file=open('./Files/Accounts/targets.txt','r')
            result=file.readlines()
            self.len=len(result)
            self.Target=result[self.count]
            if(self.Target!=None or self.Target!="" or self.Target!=" " or self.Target!='For Example:'):
                Bot.Satrt()                
            else:
                print('\33[31m'+"Your Targetname in [targets.txt] is empty!"+'\33[37m')
                time.sleep(1)
                subprocess.run(['notepad.exe', './Files/Accounts/targets.txt'])
                Bot.Get_Target()
        except:

            print('\33[31m'+'"targets.txt" file not found in "./Files/Accounts/" path!'+'\33[37m')
            inp=input('\33[32m'+'Make the file (y/n)? ')
            if(inp=='y'or inp=='Y'or inp=='yy' or inp=='yes' or inp =='YES'):
                file=open('./Files/Accounts/targets.txt','w')
                file.write('For Example:')
                file.write('\n')
                file.write('Username1')
                file.write('\n')
                file.write('Username2')
                file.write('\n')
                file.write('# Replace your data #')
                file.close()
                print('\33[32m'+'After adding the data and "closing" the text file, you can use the program.'+'\33[37m')
                print()
                time.sleep(1)
                subprocess.run(['notepad.exe', './Files/Accounts/targets.txt'])
                Bot.Get_Target()
            else:
                Bot.Exit()

    def Get_Target_Step2(self):
        try:
            file=open('./Files/Accounts/targets.txt','r')
            result=file.readlines()
            self.len=len(result)
            self.Target=result[self.count]
            if(self.Target!=None or self.Target!="" or self.Target!=" " or self.Target!='For Example:'):
                Bot.New_Tab()                
            else:
                print('\33[31m'+"Your Targetname in [targets.txt] is empty!"+'\33[37m')
                time.sleep(1)
                subprocess.run(['notepad.exe', './Files/Accounts/targets.txt'])
                Bot.Get_Target_Step2()
        except:

            print('\33[31m'+'"targets.txt" file not found in "./Files/Accounts/" path!'+'\33[37m')
            inp=input('\33[32m'+'Make the file? ?(y/n) ')
            if(inp=='y'or inp=='Y'or inp=='yy'):
                file=open('./Files/Accounts/targets.txt','w')
                file.write('For Example:')
                file.write('\n')
                file.write('Username1')
                file.write('\n')
                file.write('Username2')
                file.write('\n')
                file.write('# Replace your data #')
                file.close()
                print('\33[32m'+'After adding the data and "closing" the text file, you can use the program.'+'\33[37m')
                print()
                time.sleep(1)
                subprocess.run(['notepad.exe', './Files/Accounts/targets.txt'])
                Bot.Get_Target_Step2()

    def New_Tab(self):
        res=self.Target.replace('\n','')
        URL=f'https://www.instagram.com/{res}'
        self.browser.execute_script(f"window.open('{URL}');")
        window_name = self.browser.window_handles[0]
        self.browser.switch_to.window(window_name=window_name)
        self.firststory=True
        self.browser.close()
        window_name = self.browser.window_handles[0]
        self.browser.switch_to.window(window_name=window_name)
        Bot.Find_story()

    def Try_Tab(self):
        res=self.Target.replace('\n','')
        URL=f'https://www.instagram.com/{res}'
        self.browser.execute_script(f"window.open('{URL}');")
        window_name = self.browser.window_handles[0]
        self.browser.switch_to.window(window_name=window_name)
        self.browser.close()
        window_name = self.browser.window_handles[0]
        self.browser.switch_to.window(window_name=window_name)
        Bot.Find_story()

    def Satrt(self):
        try:
            URL='https://www.instagram.com/login/'
            self.option = webdriver.ChromeOptions()
            # For older ChromeDriver under version 79.0.3945.16
            self.option.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.option.add_experimental_option('useAutomationExtension', False)
            self.option.add_argument("window-size=1280,800")
            self.option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36")
            #..#
        
            self.browser = webdriver.Chrome(executable_path='./Driver/_ChromeDr_.exe',options=self.option)
            #Remove navigator.webdriver Flag using JavaScript
            self.browser.execute_script("const newProto = navigator.__proto__; delete newProto.webdriver; navigator.__proto__ = newProto;")
        
            self.browser.set_window_size(width=self.width,height=self.height)
            self.browser.set_window_position(self.width-15,0)
            self.browser.get(URL)
            self.firststory=True
            Bot.Login()

        except Exception as EX:
            print('\33[31m'+'')
            print('ERROR')
            print(EX)
            self.browser.quit()
            input('\33[32m'+'Press any key to continue...'+'\33[37m')
            Bot.Exit()
        
    def Login(self):
       
        try:
            self.WaitForObject(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        except:
            pass

        try:
            time.sleep(1)
            self.WaitForObject(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.User)
            self.WaitForObject(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.Pass,Keys.RETURN)
        except Exception as EX:
            print(EX)
        time.sleep(0.1)
        try:
            self.WaitForObject(By.XPATH,'//*[@id="slfErrorAlert"]')
            print()
            print('\33[31m'+'We Detected An Unusual Login Attempt!')
            print('\33[32m'+'Please fix the problem and run the program again.')
            print()
            time.sleep(2)
            Bot.Exit()
        except:
            pass

        try:
            self.WaitForObject(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        except:
            pass

        time.sleep(0.1)

        try:
            self.WaitForObject(By.CSS_SELECTOR,'div.OfoBO')
        except:
            Bot.Try_Tab()
        try:
            self.WaitForObject(By.CSS_SELECTOR,'div.OfoBO')
        except:
            Bot.Try_Tab()

        Bot.Find_story()
 
    def Find_story(self):
        time.sleep(1)
        #aria_disable=self.WaitForObject(By.CSS_SELECTOR,'.RR-M-').get_attribute('aria-disabled')
        self.directory = time.strftime("%Y-%m-%d", time.localtime())
        check_dir=os.path.exists(f'./Files/Screenshots/{self.directory}')
        if(check_dir==False):
            os.chdir('./Files/Screenshots')
            os.mkdir(f'{self.directory}')

        self.chtry=True
        
        try:
            self.WaitForObject(By.CLASS_NAME,'RR-M-.h5uC0').click()
            time.sleep(0.3)
            self.aria=True
            Bot.Check_Story()
        except:
            self.count+=1
            if(self.count<=self.len-1):
                Bot.Get_Target_Step2()
            else:
                print('\33[32m'+'The target.txt file accounts are finished.'+'\33[37m')
                print('\33[36m'+'Good luck!'+'\33[37m')
                time.sleep(2)
                Bot.Exit()
                                  
    def Click_ariadisable_stories(self):
        try:
            time.sleep(0.3)
            aria_label=self.WaitForObject(By.CSS_SELECTOR,'#react-root > section > div.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > header > div.Igw0E.rBNOH.CcYR1.ybXk5._4EzTm > div._8p8kF > button.wpO6b > div > svg').get_attribute('aria-label')
            if(aria_label=='Pause' or aria_label=='pause'):
                time.sleep(0.3)
                self.WaitForObject(By.CSS_SELECTOR,'._8p8kF > button:nth-child(1)').click()
            if(self.last_story == True):
                Bot.Screenshot()
            else:
                Bot.Next_Story()
        except:
            self.aria=False
            if(self.count<=self.len-1):
                Bot.Get_Target_Step2()
            else:
                print('\33[32m'+'The target.txt file accounts are finished.')
                print('\33[36m'+'Good luck!')
                time.sleep(1)
                Bot.Exit()
            
    def Screenshot(self):
        
        self.directory = time.strftime("%Y-%m-%d", time.localtime())
        check_dir=os.path.exists(f'./Files/Screenshots/{self.directory}')
        if(check_dir==False):
            os.chdir('./Files/Screenshots')
            os.mkdir(f'{self.directory}')
        time.sleep(1.7)

        app=wx.App()  
        dc=wx.Display.GetCount()
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]  
        screen = wx.ScreenDC()
        size = screen.GetSize()
        width=size[0]
        height=size[1]
        x,y,w,h =self.width+130,self.height-770,self.width-307,self.height-142

        bmp = wx.Bitmap(w,h)
        mem = wx.MemoryDC(bmp)

        for i in range(98):
            if 1:

                mem.Blit(-x,-y,w+x,h+y, screen, 0,0)

            if 0:
                mem.Blit(0, 0, x,y, screen, width,0)

            if 0:
                mem.Blit(0, 0, width, height, screen, width*2,0)

        self.screencount+=1
        countsc=1
        resault=self.Target.replace('\n','')
       
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1
        er=os._exists(f'/Files/Screenshots/{self.directory}/{resault}.jpg')
        if(er=='true' or er =='True'):
            countsc+=1

        resault=resault+f' [{countsc}]'
        bmp.SaveFile(f'./Files/Screenshots/{self.directory}/{resault}.jpg', wx.BITMAP_TYPE_JPEG)

        print('\33[32m'+f'Screenshot [{self.screencount}] was taken'+'\33[37m')    
        time.sleep(0.2)
        del mem

        self.last_story=False
        self.click=0

        if(self.count<self.len-1):
            self.count+=1
            Bot.Get_Target_Step2() 
        else:
            print()
            print()
            print('\33[32m'+'The target.txt file accounts are finished.'+'\33[37m')
            print('\33[36m'+'Good luck!')
            time.sleep(2)
            Bot.Exit()

    def Next_Story(self):

        if(self.aria):
            try:
                time.sleep(0.3)
                story_count=len(self.browser.find_elements_by_class_name('_7zQEa'))
                if(self.click < story_count-1):
                    self.WaitForObject(By.CSS_SELECTOR,'button.FhutL').click()
                    self.click+=1
                    self.WaitForObject(By.CSS_SELECTOR,'button.FhutL')
                    Bot.Click_ariadisable_stories()
                else:
                    self.last_story=True
                    Bot.Click_ariadisable_stories()
            except:
                if(self.count<=self.len-1):
                    Bot.Get_Target_Step2()
                else:
                    print('\33[32m'+'The target.txt file accounts are finished.'+'\33[37m')
                    print('\33[36m'+'Good luck!')
                    time.sleep(1)
                    Bot.Exit()  
        else:
            Bot.Get_Target_Step2()
                
    def Check_Story(self):

        while True:
            time.sleep(0.3)
            aria_label=self.WaitForObject(By.CSS_SELECTOR,'#react-root > section > div.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > header > div.Igw0E.rBNOH.CcYR1.ybXk5._4EzTm > div._8p8kF > button.wpO6b > div > svg').get_attribute('aria-label')
            if(aria_label=='Pause' or aria_label=='pause'):
                time.sleep(0.3)
                self.WaitForObject(By.CSS_SELECTOR,'._8p8kF > button:nth-child(1)').click()
            try:
                self.WaitForObject(By.CSS_SELECTOR,'._53lex').click()
            except:
                break
                   

        Bot.Click_ariadisable_stories()
            

    def Exit(self):
        try:
            time.sleep(1)
            print('\33[32m'+'EXIT..'+'\33[37m')
            self.browser.quit()
        except:
            pass
        

Bot=Instagram('','','',0,0,0,0,True,0,'',False,0)
Bot.Configuration_initial()