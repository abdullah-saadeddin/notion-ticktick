from ticktick import api
from notion.client import NotionClient
client = api.TickTickClient('your email ', 'yourpassword') 
clien = NotionClient(token_v2="your access token")
cv = clien.get_collection_view("link of the table")
tasks = client.task.get_from_project("6034b0298f08dd57bb74631c")
for i in tasks:
    row = cv.collection.add_row() 
    row.Name = i['title']
    client.task.complete(i['id'])
    
