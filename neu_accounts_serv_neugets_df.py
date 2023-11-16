import requests
import pandas as pd
def get_acc_serv_neug_df(token,url,id):
  #id ==> integer from id_account
  headers= {"Authorization": f"Bearer {token}"}
  url=url+str(id)
  response = requests.get(url, headers=headers)
  print(response)
  myjson = response.json()
  return pd.DataFrame(myjson)
