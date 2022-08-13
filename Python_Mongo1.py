#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pymongo')


# In[26]:


import pymongo
db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["SIBAR"]

print("List of database :",db_client.list_database_names())

collection1 = db["student"]
print("List of databases :",db_client.list_database_names())
print("List of collections :",db.list_collection_names())

#Insert documents in collection - insert_one & insert_many

doc1 = collection1.insert_one({"RollNo" : 1, "Name" : "Ramesh", "Course" : "MCA", "City" : "Pune"})
print("Inserted Document Id :",doc1.inserted_id)

doc1 = collection1.insert_many([{"RollNo" : 1, "Name" : "Ramesh", "Course" : "MCA", "City" : "Pune"},
                                {"RollNo" : 1, "Name" : "Ramesh", "Course" : "MCA", "City" : "Pune"},
                                {"RollNo" : 1, "Name" : "Ramesh", "Course" : "MCA", "City" : "Pune"},
                                {"RollNo" : 1, "Name" : "Ramesh", "Course" : "MCA", "City" : "Pune"}
                               ])
print("Inserted Document Id :",doc1.inserted_ids)

doc1 = collection1.insert_many([{"_id" : 101, "RollNo" : 10, "Name" : "Reena", "Course" : "MCA", "City" : "Mumbai"},
                                {"_id" : 102, "RollNo" : 20, "Name" : "Meena", "Course" : "MBA", "City" : "Nasik"}
                               ]) 
print("Inserted Document Id :",doc1.inserted_ids)

#Read documents in collection - 

d1 = collection1.find_one()
print("First Document is :", d1)

for d2 in collection1.find():
    print("Document is :", d2)

for d21 in collection1.find({}, {"RollNo" : 0}):
    print("Document excluding Roll No 10 are :", d21)
    
t#Delete all documents in collection

d3 = collection1.delete_one({"RollNo" : 10, "Name" : "Reena"})
print("Deleted ", d3.deleted_count)

d4 = collection1.delete_many({})
print("Deleted ", d4.deleted_count)

