#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd


# In[78]:


df = pd.read_excel(r"C:\Users\Rhugved\Desktop\Python for DA\Customer Call List.xlsx")
df


# 

# In[79]:


df = df.drop_duplicates()


# In[80]:


df = df.drop(columns = 'Not_Useful_Column')
df


# In[81]:


df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df


# In[82]:


df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df


# In[83]:


df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] 


# In[84]:


## we can also use below

df['Last_Name'] = df['Last_Name'].str.strip("123./_% ")
df


# In[85]:


df["Phone_Number"]= df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')


# In[86]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)[0:3] + '-' + str(x)[3:6] + '-' + str(x)[6:10])


# In[87]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[88]:


df[["Street_Address","State","Zip"]] = df["Address"].str.split(',',2,expand = True) # to split the address column
df


# In[91]:



df


# In[96]:


df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('N/a','')


# In[100]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('NaN','')


# In[103]:


df = df.fillna('')


# In[104]:


df


# In[111]:


## remove rows Do_Not_Contact with 'Y' and with no contact number in phone_number

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y" or df.loc[x, "Phone_Number"] == '':
        df.drop(x,inplace = True)
df


# In[120]:


## reset index values
df.reset_index(drop = True)

# alt way to drop null values 
# df = df,dropna(subset = 'Phone_Number', inplace = True)


# In[121]:





# In[ ]:




