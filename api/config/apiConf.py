# Nexa API configuration
NX_Conf = {
    # Metadata for api
    "title": "Nexa-APIs 🌊",
    "description": """
# About ❓
Simple, Free and easy to use Public api.
Visit the API playground [here](/docs)


### Made with ♥️
[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/tiangolo/fastapi)

### Links 🔗
[![API Docs](https://img.shields.io/badge/Docs-112B3C?style=for-the-badge&logo=gitbook&logoColor=white)](/redoc)
[![API Playground](https://img.shields.io/badge/Playground-354259?style=for-the-badge)](/docs)
[![Github](https://img.shields.io/badge/GitHub-030202?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Itz-fork/Nexa-APIs)
""",
    "version": "0.3.1",

    # Home route
    "home_redirect": True,
    "redirect_to": "/docs",

    # Metadata for tags
    "tags": [
        {
            "name": "Search",
            "description": "Search for stuff in ~various~ sites"
        },
        {
            "name": "File server",
            "description": "Save your files on the server and download them whenever you want!"
        },
        {
            "name": "Tools",
            "description": "Tools for simple things"
        },
        {
            "name": "Language",
            "description": "Language related stuff"
        },
        {
            "name": "Fun",
            "description": "Endpoints made to have some fun"
        }
    ]
}
