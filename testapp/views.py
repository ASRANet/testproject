from django.shortcuts import render


def index(request):
    stories = [{
        "headline": "About NUPP 2017",
        "text": "Many countries are currently constructing or are in the planning/designing stage of building nuclear" +
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
                "leading researchers, technology developers, industrial players and supply chain partners to converge."
    },
        {
            "headline": "Conference Themes",
            "text": ""
        }]
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": stories})


def venue(request):
    return render(request, 'venue.html')


def accomodation(request):
    return render(request, 'accomodation.html')


def contactus(request):
    return render(request, 'contactUs.html')


def travel(request):
    return render(request, 'travel.html')
