# -*- coding: utf-8 -*-
#Библиотеки, които използват python и Kodi в тази приставка
import re
import sys
import os
import urllib
import urllib2
import xbmc, xbmcplugin,xbmcgui,xbmcaddon
#Място за дефиниране на константи, които ще се използват няколкократно из отделните модули
__addon_id__= 'plugin.video.misiamoiatdom'
__Addon = xbmcaddon.Addon(__addon_id__)

MUA = 'Mozilla/5.0 (Linux; Android 5.0.2; bg-bg; SAMSUNG GT-I9195 Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Version/1.0 Chrome/18.0.1025.308 Mobile Safari/535.19' #За симулиране на заявка от мобилно устройство
UA = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' #За симулиране на заявка от  компютърен браузър


#Меню с директории в приставката
def CATEGORIES():
        addDir('Сезон 2017','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2017/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2016','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2016/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2015','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2015/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2013','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2013/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2012','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2012/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2011','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2011/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2010','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2010/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2009','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2009/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2008','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2008/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Сезон 2007','http://www.misiamoiatdom.com/%D0%BF%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%B5%D0%B7%D0%BE%D0%BD-2007/',1,'http://www.misiamoiatdom.com/images/logo.png')
        addDir('Как се прави','http://www.misiamoiatdom.com/интересно/как-се-прави',1,'http://www.misiamoiatdom.com/images/logo.png')




#Разлистване видеата на първата подадена страница
def INDEXPAGES(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', UA)
        response = urllib2.urlopen(req)
        #print 'request page url:' + url
        data=response.read()
        response.close()

        #Начало на обхождането
        br = 0 #Брояч на видеата в страницата - 24 за този сайт
        match = re.compile('href="(.+?)"><img src="(.+?)" alt="(.+?)" border').findall(data)
        for vid,thumb,title in match:
            thumbnail = 'http://www.misiamoiatdom.com' + thumb
            #print thumbnail
            #print title
            addLink(title,vid,2,thumbnail)
            br = br + 1
            print 'Items counter: ' + str(br)
        if br == 10: #тогава имаме следваща страница и конструираме нейния адрес
            getpage=re.compile('span id="pagination_selected">(.+?)</span>\r\n.*\r\n.*<a href="/(.+?)\d+"').findall(data)
            for page, baseurl in getpage:
                newpage = int(page)
                nextpage = newpage + 1
                url = 'http://www.misiamoiatdom.com/' + baseurl + str(nextpage)
                #print 'URL OF THE NEXT PAGE IS' + url
                thumbnail='DefaultFolder.png'
                addDir('следваща страница>>',url,1,thumbnail)


#Търсачка
def SHOW(url):
       url1 = 'http://www.misiamoiatdom.com' + url
       req = urllib2.Request(url1)
       req.add_header('User-Agent', UA)
       response = urllib2.urlopen(req)
       data=response.read()
       response.close()
       match = re.compile('<source src="(.+?)" type="video/mp4" />').findall(data)
       for link in match:
        matchd = re.compile('og:description" content="(.*)').findall(data)
        for desc in matchd:
         print desc
         matchi = re.compile('link href="(.+?)" rel="image_src"').findall(data)
         for thumbnail in matchi:
          matcht = re.compile('og:title" content="(.+?)"').findall(data)
          for title in matcht:
           finalurl = 'http://www.misiamoiatdom.com' + link 
        #url = 'http://misiamoiatdom.com' + link
           addLink2(title,finalurl,3,desc,thumbnail)






#Зареждане на видео
def PLAY(url):
        li = xbmcgui.ListItem(iconImage=iconimage, thumbnailImage=iconimage, path=url)
        li.setInfo('video', { 'title': name })
        try:
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, xbmcgui.ListItem(path = url))
        except:
            xbmc.executebuiltin("Notification('Грешка','Видеото липсва на сървъра!')")






#Модул за добавяне на отделно заглавие и неговите атрибути към съдържанието на показваната в Kodi директория - НЯМА НУЖДА ДА ПРОМЕНЯТЕ НИЩО ТУК
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setArt({ 'thumb': iconimage,'poster': iconimage, 'banner' : iconimage, 'fanart': iconimage })
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable" , "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink2(name,url,mode,plot,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setArt({ 'thumb': iconimage,'poster': iconimage, 'banner' : iconimage, 'fanart': iconimage })
        liz.setInfo( type="Video", infoLabels={ "Title": name, "plot": plot } )
        liz.setProperty("IsPlayable" , "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


#Модул за добавяне на отделна директория и нейните атрибути към съдържанието на показваната в Kodi директория - НЯМА НУЖДА ДА ПРОМЕНЯТЕ НИЩО ТУК
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setArt({ 'thumb': iconimage,'poster': iconimage, 'banner' : iconimage, 'fanart': iconimage })
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


#НЯМА НУЖДА ДА ПРОМЕНЯТЕ НИЩО ТУК
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param







params=get_params()
url=None
name=None
iconimage=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        name=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass


#Списък на отделните подпрограми/модули в тази приставка - трябва напълно да отговаря на кода отгоре
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
    
elif mode==1:
        print ""+url
        INDEXPAGES(url)

elif mode==2:
        print ""+url
        SHOW(url)

elif mode==3:
        print ""+url
        PLAY(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
