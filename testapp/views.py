# -*- coding: UTF-8 -*-

from django.shortcuts import render


def index(request):
    stories = [{
        "headline": "About NUPP 2017",
        "id": "about",
        "type": "text",
        "style": "text-align: justify",
        "text": [
            "Many countries are currently constructing or are in the planning/designing stage of building nuclear " +
            "power plants. This is primarily to move away from the depleting fossil fuel and in an attempt to" +
            "combat climate change. However, design construction and operation of these structures poses particular" +
            "challenge with respect to handling radioactive material. The conference aims to bring together " +
            "researchers, practitioners to address the structural analysis design, risk analysis and " +
            "decommissioning technologies employed in the nuclear power plant. This will involve advanced " +
            "analysis both for strength and load model in order to establish safety level. Probabilities and risk " +
            "analysis form the basis for the safety of Nuclear Power Plant, the analysis dictate the chances for " +
            "the reactor in failing in incidents of natural or external incidents. Removal and closure of a plant " +
            "is also pivotal to the face of Nuclear Energy, in giving confidence to the public. This conference " +
            "presents the perfect opportunity for you, as it aims to provide an ideal platform for industry " +
            "leading researchers, technology developers, industrial players and supply chain partners to converge."]
    },
        {
            "headline": "Conference Themes",
            "id": "conferenceThemes",
            "type": "table",
            "text": [["Advanced Structural Analysis"],
                     ["Containment Design"],
                     ["Non - Containment Design"],
                     ["Thermal Effects"],
                     ["Non - Linear Analysis"],
                     ["Structural Integrity"],
                     ["Lifetime Behaviour"],
                     ["Risk Analysis and Reliability"],
                     ["Probabilistic Seismic Hazard"],
                     ["Risk Management"],
                     ["Decommissioning Technology"],
                     ["Characterisation techniques in nuclear decommissioning"],
                     ["Remote handling and radioactive waste management"],
                     ["Radiation detection instrumentation and imaging"],
                     ["Robotics and autonomous systems in decommissioning"],
                     ["Regulations and Licensing"]]
        },

        {
            "headline": "Organising Committee",
            "id": "organisingCommittee",
            "type": "text",
            "text": [
                "Purnendu Das", "ASRANet Ltd", "UK"],
            "style": "text-align: center"
        },

        {"headline": "International Advisory Committee",
         "id": "advisoryCommittee",
         "type": "table",
         "class": "table-striped",
         "text": [["Prof A Ayoub",
                   "City University London",
                   "UK"],

                  ["Prof P Baraldi",
                   "Politecnico di Milano",
                   "Italy"],

                  ["Prof S Bhattacharya",
                   "University of Surrey",
                   "UK"],

                  ["Mr A Brown",
                   "Nuclear Innovation and Research Office",
                   "UK", ],

                  ["Prof Y Bulut",
                   "Turgut Özal University",
                   "Turkey", ],

                  ["Dr A Camara",
                   "City University London",
                   "UK", ],

                  ["Dr M Das",
                   "ENERCON",
                   "USA", ],

                  ["Prof F D’Auria",
                   "University of Pisa",
                   "Italy", ],

                  ["Dr B Dutta",
                   "Bhabha Atomic Research Centre",
                   "India", ],

                  ["Dr Ö Erbay",
                   "MATRISeb",
                   "Turkey", ],

                  ["Dr B Erkus",
                   "Istanbul Technical University",
                   "Turkey"],

                  ["Prof Y Fahjan",
                   "Gebze Technical University",
                   "Turkey", ],

                  ["Prof D Feron",
                   "Commissariat à l’énergie atomique et aux énergies alternatives",
                   "France", ],

                  ["Dr N Fernando",
                   "RMIT University",
                   "Australia", ],

                  ["Dr W Fuchs",
                   "University of Stuttgart",
                   "Germany", ],

                  ["Dr S Gallocher",
                   "AMEC Foster Wheeler",
                   "UK", ],

                  ["Dr K Gamage",
                   "Lancaster University",
                   "UK", ],

                  ["Dr L Ibarra",
                   "University of Utah",
                   "USA", ],

                  ["Prof N Kamran",
                   "Imperial College London",
                   "UK", ],

                  ["Dr G Locatelli",
                   "University of Leeds",
                   "UK", ],

                  ["Prof B Merk",
                   "University of Liverpool",
                   "UK", ],

                  ["Prof G C Park",
                   "Seoul National University",
                   "Korea", ],

                  ["Dr E Patelli",
                   "University of Liverpool",
                   "UK", ],

                  ["Prof N Prinja",
                   "AMEC Foster Wheeler",
                   "UK", ],

                  ["Mr K Schramm",
                   "Areva GmbH",
                   "Germany", ],

                  ["Dr R M Singh",
                   "University of Surrey",
                   "UK", ],

                  ["Prof C H Song",
                   "Korea Atomic Research Insti-tute",
                   "South Korea", ],

                  ["Dr K D Tsavdaridis",
                   "University of Leeds",
                   "UK", ],

                  ["Prof A Varma",
                   "Purdue University",
                   "USA", ],

                  ["Dr M Wenman",
                   "Imperial College London",
                   "UK", ],

                  ["Prof C Xu",
                   "Shanghai Jiao Tong University",
                   "China", ],
                  ]},

        {"headline": "Key Deadlines",
         "id": "keyDeadlines",
         "type": "html",
         "text": "<div class='progress'>"
                 "<div id='datesProgress' class='progress-bar progress-bar-striped active' "
                 "role='progressbar'aria-valuenow='0' aria-valuemin='0' aria-valuemax='100' style='width: 0;'>"
                 "</div></div><!-- If changing dates also change keyDeadlines variable in script.js-->"
                 "<table id='progressTable' class='table' style='text-align: center' id='keyDeadlinesTable'><tr><td>"
                 "<p>Deadline for abstracts<br>6 Jul 2016</p></td><td><p>Notification of acceptance<br>"
                 "6 Aug 2016</p></td>"
                 "<td><p>Submission of full papers<br>4 Jan 2017</p></td><td><p>Registration closes<br>"
                 "22 Jan 2017</p></td></tr></table></div><hr class='featurette-divider'>"
         }]

    return render(request, 'index.html', {"story_list": stories, "title": "Home"})


def venue(request):
    stories = [

        {
            "headline": "The Hotel",
            "type": "text",
            "style": "text-align: justify",
            "id": "theHotel",
            "text": ["Guests visiting London for business or pleasure, the Jury's Inn Croydon Hotel is perfect for "
                     "those not wishing to be in the hustle and bustle of busy London, but still close by. The Hotel "
                     "property offers cheap hotel rooms at a central location with The Whitgift Shopping centre over"
                     " the road and East Croydon Station a short 3-4 minute walk away.For those wanting to go into "
                     "Central London for a leisure day, or for business, East Croydon Station is a short 17 minute "
                     "train ride to London Victoria or London Bridge. However, there is plenty to discover in Croydon"
                     " with various Heritage sites to explore. The Queen’s Gardens are an easy 6 minute walk and "
                     "Shirley Park Golf Course is a 7 minute drive away."]

        },
        {
            "headline": "Rooms and Features",
            "type": "text",
            "style": "text-align: justify",
            "id": "rooms",
            "text": ["The Venue has 240 spacious rooms, which are able to accommodate up to three adults or two adults "
                     "and two children under twelve. With a large soft bed, an en-suite bathroom and a flat screen "
                     "TV with Freeview on offer, Jurys Inn Croydon provides both business and pleasure guests all the"
                     " essentials they need.",
                     "Further room features include free WiFi, air-con, hair-dryers and extra pillows on request."]
        },
        {
            "headline": "Accessible Rooms",
            "type": "text",
            "style": "text-align: justify",
            "id": "accessibleRooms",
            "text": ["Jurys Inn provides a number of wheelchair accessible bedrooms. These rooms have been designed to "
                     "the highest specifications to make your stay with Jurys Inn Croydon as easy and pleasurable as "
                     "possible.These bedrooms include wide doorways, floor space to manoeuvre, and accessible "
                     "bathrooms. Throughout the hotel, the Venue also provide accessible toilets in public areas and "
                     "lift access to all floors."]
        },
        {
            "headline": "Food and Drink",
            "type": "text",
            "style": "text-align: justify",
            "id": "accessibleRooms",
            "text": ["The Venue has a stylish on-site bar for those wishing to relax with glass of wine after a long "
                     "day of shopping or business.If you get hungry you can order food from the bar menu, or "
                     "alternatively, you can dine in the in-house restaurant which has a range of delicious dishes on"
                     " offer.If you would like somewhere to relax, work or surf the web, the venue has a comfortable"
                     " lounge with free WiFi throughout the hotel. Jurys Inn Croydon also provides an all-day Costa"
                     " coffee bar where you can sit with a newspaper or curl up with a good book."]
        },
    ]

    return render(request, 'venue.html', {"story_list": stories, "title": "Venue"})


def accomodation(request):
    return render(request, 'accomodation.html', {"title": "Accomodation"})


def contactus(request):
    return render(request, 'contactUs.html', {"title": "Contact Us"})


def author_instructions(request):
    stories = [
        {
            "headline": "Speaker Information",
            "type": "html",
            "id": "speakerInstructions",
            "text": "<ul><li>"
                    "Presentations should be in MS PowerPoint or PDF format. Please keep the use of video and audio to "
                    "a minimum as it could prove problematic."
                    "</li><li>"
                    "All presentations should be emailed to us a week before the conference. If authors wish to make "
                    "any changes to their presentations please let us know as soon as possible and send the relevant "
                    "files to us 24 hours before you are due to speak."
                    "</li><li>"
                    "The timeslots allocated to presenters are 20min: 15 minutes for your presentation and a further 5 "
                    "minutes for questions from the audience. The session chairs will remind you when your time has "
                    "finished. Please keep these times in mind.</ul></li><ul><li>"
                    "All speakers should be in the relevant room, in which their presentation will take place, at least"
                    " 5 minutes before their session starts.</li></ul>",},

        {
            "headline": "Author Information",
            "type": "html",
            "id": "authorInstructions",
            "text": "<ul><li>"
                    "Please submit all papers by 4 January 2017 by emailing them to us. If you are worried about making"
                    " the deadline then please contact us, so that an extension can be arranged."
                    "</li><li>"
                    "<a href='/static/paperFormat.doc'>Here is the official template</a> to use for all papers. "
                    "This template can also be used for abstracts."
                    "</li><li>"
                    "All papers should be submitted in PDF format and should not be numbered. There is no specific page"
                    " number requirement for papers, although most tend to be around the 8 page mark."
                    "</li><li>"
                    "In addition, you must also fill out and sign a Copyright Release form "
                    "<a href='/static/copyrightForm.doc'>(found here)</a> and email a "
                    "scanned copy of that to us, so that your paper can be included in the Official Conference "
                    "Proceedings.</ul></li>"
        },
        {
            "headline": "Exhibitor Information",
            "type": "html",
            "id": "exhibitorInstructions",
            "text": "<ul><li>"
                    "All exhibitors should arrive at the conference venue at least half an hour before the conference "
                    "starts on Day 1."
                    "</li><li>"
                    "All material that exhibitors wish to display should be supplied by the exhibitor and relevant "
                    "delivery and collection services to the venue arranged."
                    "</li><li>"
                    "Please let us know when delivery is scheduled, so that we can make sure to make venue staff aware."
                    "</li><li>"
                    "Should you want to bring heavy/bulky exhibits please let us know beforehand as this may not be "
                    "possible in all cases."
                    "</li><li>"
                    "All exhibition packages include a free registration, so you can take part in conference sessions. "
                    "All breaks will take place in the exhibition room(s)."
                    "</li></ul>"
        }
    ]

    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": stories, "title": "Author Instructions"})


def travel(request):
    stories = [
        {
            "headline": "Getting to Croydon",
            "type": "html",
            "id": "gMap",
            "text": "<div id='map' class='col-md-12 embed-responsive embed-responsive-16by9' style='align-content: center'>"
                    "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11509.527080716594!2d-0.0988748"
                    "7574740741!3d51.375872035920246!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48760732360e4"
                    "ef1%3A0xe1e157f691ba9d21!2sJurys+Inn+Croydon!5e0!3m2!1sen!2suk!4v1454420608615'width='800'"
                    " height='450' frameborder='0' style='border:0' allowfullscreen></iframe></div>"
        },
        {
            "headline": "Underground",
            "type": "text",
            "style": "text-align: justify",
            "id": "underground",
            "text": ["Croydon is not served by the Underground network. However the old East London Line has been "
                     "integrated into the new London Overground network, linking West Croydon Station to Dalston "
                     "Junction via New Cross, Docklands, and Whitechapel. This service, which started in June 2010, "
                     "uses new rolling stock with longitudinal seating layouts similar to those used on Underground "
                     "trains allowing for more standing room. It is operated by Transport for London as part of the "
                     "London Overground scheme."]
        },
        {
            "headline": "Tram",
            "type": "text",
            "style": "text-align: justify",
            "id": "tram",
            "text": ["A tramlink tram bound for Croydon Tramlink, opened in 2000, is the first modern tram system to "
                     "operate in Greater London. Trams at the moment have destinations at Beckenham, Wimbledon, Elmers "
                     "End and New Addington with all lines traveling through Croydon on the Croydon Loop. It can also be"
                     " used to reach the Underground in Wimbledon."]
        },
        {
            "headline": "Train",
            "type": "text",
            "style": "text-align: justify",
            "id": "train",
            "text": ["East Croydon station is the second busiest station in London and the main station for Croydon. "
                     "Fast trains run into the centre of London terminating at Victoria or London Bridge stations in "
                     "about 15-20 minutes. There are direct service connections to London Gatwick and London Luton "
                     "airports. Journey times from East Croydon to London Gatwick airport range from 15 to 36 minutes,"
                     " with an average of 13 services per hour during the day. The journey time from East Croydon to"
                     " London Luton airport is approximately 66 minutes, with an average of 4 services per hour during"
                     " the day. The train service for London Luton airport also stops at London St Pancras (average "
                     "journey time approximately 40 minutes), providing interconnections for Eurostar services to Lille,"
                     " Paris and Brussels, as well as national services to the north of England & Scotland. "
                     "There are no direct train services to London Heathrow airport. Typical fastest journey time would"
                     " be approximately 90 minutes and involve at least two changes. All services from London Victoria"
                     " that head to the south coast stop here. Journey times from East Croydon to Brighton range from "
                     "36 to 60 minutes, with an average of 9 services per hour during the day. Services are provided by"
                     " Southern and First Capital Connect. West Croydon station—which features in the famous story"
                     " 'Casting the Runes' by ghost story master M.R. James—is an interchange station for train, "
                     "tram and bus. Trains run into the centre of London terminating at Victoria or London Bridge "
                     "stations in about 20-40 minutes. Services leaving London generally terminate at Sutton but some"
                     " continue to Guildford, Dorking and Epsom Downs."]
        },
        {
            "headline": "Bus",
            "type": "text",
            "style": "text-align: justify",
            "id": "bus",
            "text": ["Croydon is well served by the London bus network, with a major bus station at West Croydon "
                     "and a new one opening on the eastern side of Croydon next to the Croydon clocktower and Park "
                     "Place shopping centre soon. Bus services in the centre of Croydon include, but are not limited "
                     "to: Towards central London: bus routes 50, 60, 109, 250, 468, X68 (a peak time express service)."
                     " Other routes: 75, 119 (Purley Way (Croydon Airport) - Bromley), 157, 197, 264, 289, 312 (South "
                     "Croydon Bus Garage - Peckham, via Central Croydon, Addiscombe), 407, 410, 450, 455, 466 (not too"
                     " reliable), and X26 (West/East Croydon - Sutton - Kingston - Heathrow Central (Express))."]
        }]
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": stories, "title": "Travel"})


def cookies(request):
    return render(request, 'cookies.html')


def robots(request):
    return render(request, 'robots.txt')