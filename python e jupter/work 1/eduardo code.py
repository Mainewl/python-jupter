from imap_tools import MailBox



mailbox = MailBox(imap_server)
mailbox.login(my_email, _, initial_folder='Inbox/WATCHER')
folders = mailbox.folder.list('Inbox/WATCHER')
folders_list = []
for folder in folders[1:]:
folder_name = folder.name[folder.name.rfind('/')+1:]
folders_list.append(folder_name)
status = mailbox.folder.status(folder.name)
try:
json_data[folder_name]['MAIL_COUNT'] = status['MESSAGES']
except:
try:
json_data[folder_name].update({'MAIL_COUNT': status['MESSAGES']})
except:
json_data.update({folder_name : {}})
json_data[folder_name].update({'MAIL_COUNT': status['MESSAGES']})
print(f"\nMESSAGES IN {folder_name} = {status['MESSAGES']}")

mailbox.folder.set(folder.name)
for msg in mailbox.fetch(criteria='ALL', mark_seen=False, reverse=True):
sbj = msg.subject
print(f"LAST RECEIVED: {msg.date_str[:msg.date_str.rfind('-')-1]}\n{sbj}")
form_name = sbj[sbj.rfind('for ')+4:]
form_name = unidecode(form_name)
payload = msg.html
break
soup = BeautifulSoup(payload, 'html.parser')
link_tag = soup.find_all(class_="email-template-content-summary-link")[0]
link = link_tag['href']
form_id = link[link.find('=')+1:link.rfind('&')]
try:
json_data[folder_name]['FORM_NAME'] = form_name
json_data[folder_name]['FORM_ID'] = form_id
except:
json_data[folder_name].update({'FORM_NAME': form_name})
json_data[folder_name].update({'FORM_ID': form_id})
try:
json_data[folder_name]['TRIGGERED_COUNT']
except:
json_data[folder_name].update({'TRIGGERED_COUNT' : 0})

# IMAP SERVER LOGOUT
# print("\nLOGGING OFF...")
# close = mailbox.close()
# print(f"\n{close[0]}: {close[1][0].decode()}")
logout = mailbox.logout()
print(f"\n{logout[1][0].decode()}.. {logout[0]}!\n"