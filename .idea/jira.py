import requests
import zipfile
import io
import re
headers = {'Authorization':'Basic Zmd1b0BpcGFzcy5jb206WDE2NGwzbzVSSTBIeFRYWXNRNmkzQzQ3', 'Content-Type':'application/json'}
# lastRunKey = 'DFOD-1034' # for delta mode.
lastRunKey = 'DFOD-100'
#r = requests.get('https://ipassagile.atlassian.net/rest/api/2/issue/87592?expand=names', headers=headers)
# r = requests.get('https://ipassagile.atlassian.net/rest/api/2/attachment/49944', headers=headers)
ids = []
r = requests.get(f'https://ipassagile.atlassian.net/rest/api/2/search?jql=project+%3D+%22Dogfood+Queries%22+AND+component+%3D+curation+AND+status+!%3D+DONE+and+key>{lastRunKey}+ORDER+BY+key+DESC', headers=headers)
total = r.json()["total"]
for startAt in range (0, total, 50):
    r = requests.get(f'https://ipassagile.atlassian.net/rest/api/2/search?jql=project+%3D+%22Dogfood+Queries%22+AND+component+%3D+curation+AND+status+!%3D+DONE+and+key>{lastRunKey}+ORDER+BY+key+DESC', params={'startAt':startAt}, headers=headers)
    issues = r.json()["issues"]
    for item in issues:
        ids.append(item["id"])
# r.text
print(f"total since last run {total}" )
ids




# print(r.json()["id"])
# f = io.BytesIO()
# f.write(r.content)
# z = r.json()["content"]["id

# z = r.json()["fields"]["attachment"][0]["self"]
# r = requests.get('https://ipassagile.atlassian.net/rest/api/2/issue/87655?expand=names', headers=headers)
# print(r.json()["fields"]["attachment"][0]["self"])




## now get the attachment ids
attachement_ids = []
for zf in ids:
    # get attachment id
    print("+++++"+zf)
    ra = requests.get(f"https://ipassagile.atlassian.net/rest/api/2/issue/{zf}?expand=names", headers=headers)
    try:
        att = ra.json()["fields"]["attachment"][0]
        #["self"]
        print("-----" + att["id"] + "    " + att["filename"])
        if att["filename"] == 'Logs.zip':
            attachement_ids.append(att["id"])
    except IndexError:
        pass


## unzip the files
def extract_zip(input_zip):
    input_zip = zipfile.ZipFile(input_zip)
    logOutput = "/Users/fguo/work/curation"
    input_zip.extractall(logOutput)
    # for i in input_zip.namelist():
    #     #print(i)
    #     input_zip.extract(i, "./blahblah")

headers_zip = {'Authorization':'Basic Zmd1b0BpcGFzcy5jb206WDE2NGwzbzVSSTBIeFRYWXNRNmkzQzQ3', 'Content-Type':'application/zip'}
for zip in attachement_ids:
    rz = requests.get(f'https://ipassagile.atlassian.net/secure/attachment/{zip}/Logs.zip', headers=headers_zip)
    print("extracting..." + zip)
    f = io.BytesIO()
    f.write(rz.content)
    extract_zip(f)


# extracted = print(extract_zip(f))
import shutil
shutil.move("/Users/fguo/work/curation/storage/emulated/0/Android/data/com.ipass.fhisv2/files/iPass", logOutput+"/log")
# r.json["fields.attachment.self"]