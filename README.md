# bayreuth
## Job Application

### Initial email
> Sehr geehrter Herr Dubrava,
> 
> wie bereits angekündigt, möchten wir Ihnen die Möglichkeit geben, sich auf das Gespräch vorzubereiten. Den groben Rahmen bildet bitte ihre Bearbeitung der folgenden Aufgaben. Ihre Resultate werden Gegenstand des Interviews sein. Bitte bereiten Sie diese so auf, dass Sie sie während des Gesprächs präsentieren und erläutern können. 
> 
> 1. Bitte schauen Sie sich die Seite von Flourish an. Wie bewerten Sie das Tool für den Einsatz in der Lehre in einem Bachelor-Kurs Data Science für Humangeograph*innen? (Info: Die Studierenden haben statistische Vorkenntnisse und Kenntnisse in Kartographie, aber keine Kenntnisse in Programmiersprachen). https://flourish.studio/
> 2. Performen Sie ein einfaches Webscraping in R mit einer Seite ihrer Wahl (die Seite sollte was mit Geographie im weitesten Sinne zu tun haben) und zaubern Sie daraus eine Visualisierung. 
> 3. Bitte importieren Sie in ein entsprechendes R-Paket ihrer Wahl Daten zu den tödlichen Erdbeben auf Wikipedia. Bitte formen sie diese zu einem tibble und erstellen mit den erhaltenen Daten eine Karte, welche die Lage und die Stärke der Erdbeben angibt: https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900 
> 4. Betrachten Sie die Seite http://www.reflectories.de und skizzieren Sie Ideen, wie sie diese Inhalte technisch weiterentwickeln könnten. 
> 
> Wir freuen uns auf Ihre Ideen im Gespräch.
> 
> Mit freundlichen Grüßen,
> Stefan Ouma und Gabriele Schrüfer

----

### My attempts to answer the questions
1. Take a look at Flourish's page. https://flourish.studio/ How do you rate the tool for use in teaching in a B.Sc. course Data Science for Human Geographers?</br>
   Info: The students have previous statistical knowledge and knowledge of cartography, but no knowledge of programming languages).</br>

2. Simple web scraping of a page (related to geography) and its visualization.</br>
   *Used Data:*
     - Wikipedia Article "Liste der Großstädte in Deutschland",</br>https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland

   *Used Software:*
     - Python3 (requests, beautifulsoup, pandas, geopy, matplotlib)
	 - PyCharm 2019.2.3 (Community Edition)
	 - Notepad++
   
   *Output:* [scatter_plot.PNG](https://imgur.com/a/WC15HNv)
   
3. Import data from Wikipedia article into an appropriate package of your choice. Create a map that shows the location and magnitude of the earthquakes.</br>
   *Used Data:*
     - Natural Earth 1:110m Cultural Vectors,</br>https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/110m_cultural.zip
     - Wikipedia Article "List of deadly earthquakes since 1900",</br>https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900
	 - Earthquake Magnitude Classes: http://www.geo.mtu.edu/UPSeis/magnitude.html

   *Used Software:*
     - Python3 (requests, beautifulsoup, pandas)
	 - PyCharm 2019.2.3 (Community Edition)
	 - Notepad++
	 - QGIS 3.10 LTR
   
   *Output:* [map.PNG](https://imgur.com/a/lTmBBo5)

4. Check the web page http://www.reflectories.de and outline ideas on how technically this content could be developed.</br>