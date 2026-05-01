"""
config/settings.py
All configuration for the framework lives here.
URLs, timeouts, credentials — single source of truth.
"""
BASE_URL = "https://automationexercise.com"
TIMEOUT  = 15000
HEADLESS = False

USERS={
    "valid_user":{
        "email":"kjeevanak@gmail.com",
        "password":"Theja@123"
    }
}
ROUTES={"home":"/",
        "login":"/login",
        "products":"/products",
        "cart":"/view_cart"
        }
