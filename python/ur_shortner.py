



from hashids import Hashids

pk = 123 # Your object's id
domain = 'https://erp.bjitgroup.com' # Your domain

hashids = Hashids(salt='this is my salt', min_length=6)
link_id = hashids.encode(pk)
url = 'http://{domain}/{link_id}'.format(domain=domain, link_id=link_id)

print(url)