import requests
import pandas as pd
def neu_consumos_df(id,From, To,token):
  url="https://api.neu.com.co/data/consumption/"
  #id ==> id_account
  headers= {"Authorization": f"Bearer {token}"}
  try:
      response = requests.post(url, headers=headers,json = {"Id_account": id,"From": From,  "To": To})
      print(response)
      myjson = response.json()
      data=myjson[0]['data']
      return pd.DataFrame(data)
  except:
      print("No se obtuvieron datos")
