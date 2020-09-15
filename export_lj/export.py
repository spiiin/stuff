#script for export livejournal entries
#uses fixed lj module and fix_encoding module
#template for render post from jupyter notebook

import xmlrpc
from ftfy import fix_encoding
from lj import backup

j = backup.DEFAULT_JOURNAL
backup.backup("user", "password", j)

tagDict = {}

entries = j["entries"]
for entryKey in sorted(entries.keys()):
	entry = entries[entryKey]
	subj = entry.get("subject", "-"*60)
	tags = fix_encoding(str(entry.get("props").get("taglist")))
	
	tagsList = tags.split(",")
	for tag in tagsList:
		if tag.strip() not in tagDict:
			tagDict[tag.strip()] = 0
		tagDict[tag.strip()] += 1
	
	text = fix_encoding(str(entry["event"]))
	if type(subj) == xmlrpc.client.Binary:
		subj = fix_encoding(str(subj))
	
	display(HTML("<p>%s <a href=%s>%s</a> - %s</p>"%(entry["eventtime"], entry["url"], subj, tags)))
	#print(text)
	#display(HTML(text))
	
#print tags
for k,v in tagDict.items():
	print(k,v)