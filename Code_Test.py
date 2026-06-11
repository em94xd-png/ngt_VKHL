from selenium import webdriver
from selenium.webdriver.edge.options import Options

import time

options = Options()
options.add_argument(r"C:\Users\dutymanager.vkhl\AppData\Local\Microsoft\Edge\User Data\Default")
options.add_argument("profile-directory=Default") # Use the default profile
options.add_argument("--start-maximized") # Start the browser maximized
options.add_experimental_option("detach", True) # Keep the browser open after the script finishes

# Launch with the specified options
driver = webdriver.Edge(options=options)
driver.get("https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud")

# time.sleep(86400)  # Keep the browser open for 24 hours (86400 seconds)