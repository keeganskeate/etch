"""
State Variables

TODO: Save in database and retrieve and load.
"""

state = {
    "author": "ETCH",
    "email": "michargecommunity@gmail.com",
    "phone": "360 915-3209",
    "phone_number": "13609153209",
    "social": [
        { 
          "title": "GitHub",
          "url": "https://github.com/keeganskeate/etch",
        },
    ]
}

homepage = {
    "hero": {
        "action": "Contact us",
        "title": "Energy, transportation, community, and heritage for a sustainable future.",
        "message": "ETCH is awesome because we put freedom at your fingertips. Mobility, marketing, and management made easy for you.",
        "url": "/contact",
    },
    "features": [
        {
            "title": "Community driven",
            "message": "We believe that everyone benefits when people are able to study and tinker with their solutions. With the freedom provided by ETCH, users (both individually and collectively) control the solutions and what they do for them.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_garden.svg"
        },
        {
            "title": "Dedicated discovery",
            "message": "You can trust our dedicated team to communicate with you, discover your needs, and deliver a researched plan to get the most benefits out of your initiative. Let us help in the discovery of the solutions that you have invested hard-earned time and money.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_discovery.svg"
        },
        {
            "title": "Building jobs",
            "message": "ETCH empowers you with control over the development process, resources, and decision making authority. We believe that the community is the best judge of how their impact on the environment can be improved, so, we have entrusted the resources with you.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_work.svg"
        }
    ],
    "featurettes": [
        {
            "title": "Marketing and mobility management.",
            "subtitle": "Free your time for science and analysis.",
            "message": "The more mundane tasks that you can automate and execute quickly and efficiently by ETCH, then the more time you have to conduct science and experiments.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_puzzle.svg"
        },
        {
            "title": "Extend, modify, and personalize.",
            "subtitle": "Add anything that you need.",
            "message": "An advantage of the ETCH system over proprietary solutions is that ETCH lets you make modifications as you need because ETCH is an open box of free solutions.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_communication.svg"
        },
        {
            "title": "A ride @ at your fingertips.",
            "subtitle": "Freedom at your fingertips.",
            "message": "ETCH is a system of free solutions that you can use to empower your community. ETCH belongs to you so that you can use the ETCH system however that you please. Free solutions let you operate ethically with the stars as the limit.",
            "image": "etch_mobility/images/illustrations/brilliant_ideas_transportation.svg"
        }
    ]
}

header = {
    "action": {
        "title": "Contact",
        "url": "contact",
    },
    "nav_items": [
        {
            "category": "j-box",
            "slug": "about",
            "title": "J-Box",
        },
        {
            "category": "mi-charge",
            "slug": "about",
            "title": "Mi Ch@rge",
        },
        {
            "category": "ev",
            "slug": "about",
            "title": "EV's",
        },
    ]
}

footer = {
    "index": [
        {
            "slug": "about",
            "group": "Energy",
            "links": [
                {"title": "Emissions", "url": "about"},
                {"title": "Water","url": "about"},
                {"title": "Waste", "url": "about", "path": ""},
                {"title": "Agriculture", "url": "about", "path": ""},
                {"title": "Forests", "url": "about"},
            ],
        },
        {
            "slug": "about",
            "group": "Transportation",
            "links": [
                {"title": "EVs", "url": "about", "path": ""},
                {"title": "Rural transit", "url": "about", "path": ""},
                {"title": "Idling reduction", "url": "about", "path": ""},
                {"title": "Carpooling", "url": "about", "path": ""},
                {"title": "Commuting", "url": "about", "path": ""},
            ],
        },
        {
            "slug": "about",
            "group": "Community",
            "links": [
                {"title": "Land use", "url": "about"},
                {"title": "Housing","url": "about"},
                {"title": "Food", "url": "about", "path": ""},
                {"title": "Water", "url": "about", "path": ""},
                {"title": "Health", "url": "about"},
            ],
        },
        {
            "slug": "about",
            "group": "Heritage",
            "links": [
                {"title": "Generations", "url": "about"},
                {"title": "Education", "url": "about", "path": ""},
                {"title": "Partners", "url": "contact", "path": ""},
                {"title": "Interconnection", "url": "about", "path": ""},
                {"title": "Community", "url": "about", "path": ""},
            ],
        },
    ]
}
