from notion.client import NotionClient
from ticktick import api
client = api.TickTickClient('your email ', 'yourpassword') 
from datetime import datetime  
clien =NotionClient(token_v2="your access token")
cv = clien.get_collection_view("link of the table")
for i in cv.collection.get_rows():
    if i.show == True and i.moved == False and i.Done == False:
        name = i.Name
        date = datetime.now()
        groceries = client.task.create(name, start=date,tags=i.Context)  
        i.moved = True
