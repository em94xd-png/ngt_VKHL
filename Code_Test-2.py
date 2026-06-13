from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options
import json

edge_options = Options()
# edge_options.add_argument("--headless")      # Runs silently in the background
edge_options.add_argument('--kiosk-printing') # Skips the confirmation dialog

# Define your exact print format parameters
print_formatting = {
    "version": 2,
    "isHeaderFooterEnabled": False,  # True to include URL/date headers, False to hide them
    "isLandscapeEnabled": True,     # True for Landscape layout, False for Portrait
    
    # 1. SET BOTH SIDES (DUPLEX) PRINTING
    # 0 = Simplex (One-sided), 1 = Duplex Long Edge (Flip Book style), 2 = Duplex Short Edge (Tablet style)
    "duplex": 2, 
    
    # 2. SET PAGES PER SHEET
    # Options: 1, 2, 4, 6, 9, 16 pages per sheet layout
    "pagesPerSheet": 1 
}

# Inject these custom format settings directly into Edge's sticky browser properties
edge_options.add_experimental_option("prefs", {
    "printing.print_preview_sticky_settings.appState": json.dumps(print_formatting)
})

driver = webdriver.Edge(options=edge_options)
driver.get("https://example.com")

# Fires the print command and completes automatically
driver.execute_script("window.print();") 

# time.sleep(.5)
# driver.quit()
