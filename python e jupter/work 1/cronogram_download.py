from EG_LIB import *

url = "https://schaeferyachts-my.sharepoint.com/personal/igor_phelippe_schaeferyachts_com_br/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Figor%5Fphelippe%5Fschaeferyachts%5Fcom%5Fbr%2FDocuments%2FPCP&FolderCTID=0x012000CF964A0AA3FFEB4A8782D9C299D7A8E0"
download_path = r"C:\Users\alisson.dalton\Desktop\Nova pasta"
css_selector1 = "button[aria-label='Mostrar ações']"
css_selector2 = "button[aria-label='Baixar']"
class_name = "checkCell_92154229"

chrome.open_page(url, download_path)
chrome.clickon("class name", class_name)
chrome.clickon("css selector", css_selector1)
chrome.clickon("css selector", css_selector2)
chrome.quit()

chrome.clickon()