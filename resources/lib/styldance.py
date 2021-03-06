﻿# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re
import urllib
import urllib2 
import cookielib

__addon__           = xbmcaddon.Addon()
__addon_id__        = __addon__.getAddonInfo('id')
__addonname__       = __addon__.getAddonInfo('name')
__icon__            = __addon__.getAddonInfo('icon')
__addonpath__       = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__            = __addon__.getLocalizedString
__path__            = os.path.join(__addonpath__, 'resources', 'lib' )
__path_img__        = os.path.join(__addonpath__, 'resources', 'media' )

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:

    def start(self, selfGet):
    
        # vars
        self = selfGet
    
        list = [
            ['Fun Rádio Dance (SK)', 'http://stream.funradio.sk:8000/dance128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof23.jpg'],
            ['Fitrádio Chill out (SK)', 'http://server1.internetoveradio.sk:8802/chillout', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof12.jpg'],
            ['Fitrádio Crossfit (SK)', 'http://server1.internetoveradio.sk:8809/crossfit', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof13.jpg'],
            ['Fitrádio Pumping (SK)', 'http://server1.internetoveradio.sk:8802/pumping', 'https://i11.servimg.com/u/f11/19/40/01/67/radiof15.jpg'],
            ['Fit Family Rádio (SK)', 'http://server1.internetoveradio.sk:8803/ffr.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/fitrad11.jpg'],
            ['Rádio Kiss (SK)', 'http://stream.radiokiss.sk:8000/kissmp3_128.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiok11.jpg'],
            ['tvojeRADIO.com Dance (SK)', 'http://server1.internetoveradio.sk:8816/dance.mp3', 'https://i11.servimg.com/u/f11/19/40/01/67/radiot13.jpg'],
            ['Club Rádio (CZ)', 'http://icecast2.play.cz:8000/Clubradio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc18.jpg'],
            ['Clubbeat Rádio (CZ)', 'http://mp3stream4.abradio.cz/clubbeat128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc11.jpg'],
            ['DAB Plus Top 40 (CZ)', 'http://icecast6.play.cz/dabplus-top40.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod12.jpg'],
            ['Dance Club Rádio (CZ)', 'http://mp3stream4.abradio.cz/dance128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/dancec11.jpg'],
            ['Dance Rádio (CZ)', 'http://pool.cdn.lagardere.cz/dance-radio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod10.jpg'],
            ['Drumandbass Radio SHADOWBOX (CZ)', 'http://ice3.abradio.cz/shadowbox128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios10.jpg'],
            ['Rádio Chillout (CZ)', 'http://mp3stream4.abradio.cz/chillout128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radioc12.jpg'],
            ['Rádio Free 107 Fm (CZ)', 'http://icecast8.play.cz/freeradio128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof23.jpg'],
            ['Fajn Radio Fresh (CZ)', 'http://ice.abradio.cz/fajnfresh128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiof12.jpg'],
            ['SeeJay Rádio (CZ)', 'http://mp3stream.abradio.cz:8000/seejay128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios11.jpg'],
            ['Rádio Spin 96,2 FM (CZ)', 'http://icecast4.play.cz/spin128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radios14.jpg'],
            ['This Is Radio (CZ)', 'http://ice3.abradio.cz/this_is_radio.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiot10.jpg'],
            ['Radio N-JOY (BG)', 'http://46.10.150.243/njoy.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radion12.jpg'],
            ['Dark Asylum Radio (GB)', 'http://91.121.165.137:8020/stream/1/', 'https://i46.servimg.com/u/f46/19/40/01/67/c175141.png'],
            ['KISS FM UK (GB)', 'http://icy-e-ba-01-gos.sharp-stream.com/kissnational.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175121.png'],
            ['NonStopPlay (GB)', 'http://stream.nonstopplay.co.uk/nsp-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175133.png'],
            ['NonStopPlay Pure Dance (GB)', 'http://stream.nonstopplay.co.uk/nsppd-128k-mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/nonsto10.jpg'],
            ['181.fm Party 181 (USA)', 'http://uplink.duplexfx.com:8036', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['181.fm POWER 181 (USA)', 'http://relay.181.fm:8128', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['Radio Danz (USA)', 'http://107.182.230.133/stream?icy=http', 'https://i62.servimg.com/u/f62/19/40/01/67/radio_13.png'],
            ['B4B Radio Club Dance (F)', 'http://b4bsecours2.radioca.st/8727/', 'https://i46.servimg.com/u/f46/19/40/01/67/c17559.png'],
            ['Puls Radio Dance (F)', 'http://icecast.pulsradio.com:80/pulsHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/pulsra10.jpg'],
            ['Puls Radio Lounge (F)', 'http://icecast.pulsradio.com/relaxHD.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/lounfe10.jpg'],
            ['One Dance (I)', 'http://ice10.fluidstream.net/rn1_2.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175136.png'],
            ['Deep FM (NL)', 'http://stream.deep.radio/sd', 'https://i46.servimg.com/u/f46/19/40/01/67/c17579.png'],
            ['Antenne Bayern Fresh (D)', 'http://channels.webradio.antenne.de/fresh', 'https://i62.servimg.com/u/f62/19/40/01/67/antenn11.jpg'],
            ['Underground fm - Electro Station (PL)', 'http://fucktheradio.net:9400/stream', 'https://i46.servimg.com/u/f46/19/40/01/67/underg11.png'],
            ['Kronehit Clubland xxl (A)', 'http://onair-ha1.krone.at/kronehit-clubland.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175132.png'],
            ['Kronehit Dance (A)', 'http://onair-ha1.krone.at/kronehit-dance.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175131.png'],
            ['16bit.FM - ProBeat (RU)', 'http://16bitfm.com:8000/main_mp3_192', 'https://i46.servimg.com/u/f46/19/40/01/67/c17538.png'],
            ['San FM - Trance Channel (RU)', 'http://sanfm.ru:8000/trance', 'https://i46.servimg.com/u/f46/19/40/01/67/c17539.png'],
            ['Energy Dance (CH)', 'http://energydance.ice.infomaniak.ch/energydance-high.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175134.png'],
            ['Rouge Dance (CH)', 'http://rouge-dance.ice.infomaniak.ch/rouge-dance-128.mp3', 'https://static.radio.net/images/broadcasts/e4/3a/18770/1/c175.png'],
            ['Rouge Dance 2000 (CH)', 'http://rouge-dance2000.ice.infomaniak.ch/rouge-dance2000-128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c175135.png'],
            ['MyRadio Dance Club (UA)', 'http://music.myradio.com.ua:8000/dance128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c30010.png'],
            ['MyRadio Trance and Progressive (UA)', 'http://music.myradio.com.ua:8000/trance128.mp3', 'https://i46.servimg.com/u/f46/19/40/01/67/c30010.png']
            ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?da_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
