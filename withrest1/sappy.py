import requests
import json
base='http://127.0.0.1:8000/'
end='api/'
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(base+end,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource(1)

# def create_resource():
#     new_emp={
#         'eno':500,
#         'ename':'swapna',
#         'esal':'50000000',
#         'eaddr':'london',
#     }
#     r=requests.post(base+end,data=json.dumps(new_emp))
#     print((r.status_code))
#     print(r.json())
#     print(r.text)
# create_resource()

def update_resource(id):
    new_data={
        'id':id,
        'esal':30000000,
        'eaddr':'goa',
    }
    r=requests.put(base+end,data=json.dumps(new_data))
    print(r.status_code)
    print(r.text)
    print(r.json())
update_resource(5)

# def delete_resource(id):
#     data={
#         'id':id,
#     }
#     r=requests.delete(base+end,data=json.dumps(data))
#     print(r.status_code)
#     print(r.text)
#     print(r.json())
# delete_resource(3)




