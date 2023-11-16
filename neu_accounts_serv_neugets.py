import requests
def get_acc_serv_neug(token,url,id):
  headers= {"Authorization": f"Bearer {token}"}
  url=url+str(id)
  response = requests.get(url, headers=headers)
  print(response)
  myjson = response.json()
  return myjson
