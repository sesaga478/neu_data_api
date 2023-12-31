import requests
import pandas as pd
def neu_fact_notif_df(url,token,id=2219, From:str="2023-01-01T00:00:00", To:str="2023-12-31T00:00:00"):
    #id ==> id_service
    headers= {"Authorization": f"Bearer {token}"}
    try:
        response = requests.post(url, headers=headers,json = {"Id_service": id,"From": From,  "To": To})
        print(response)
        myjson = response.json()
        maxPage = myjson['maxPage']
        data = []
        data.extend(myjson['data'])

        if maxPage > 1:
            for i in range(2,maxPage+1):
                response = requests.post(url+"?page={PagenNumber}".format(PagenNumber=i), headers=headers,json = {"Id_service": id,"From": From,  "To": To})
                myjson = response.json()
                data.extend(myjson['data'])
        return pd.DataFrame(data)
    except:
        print("No se obtuvieron datos")
