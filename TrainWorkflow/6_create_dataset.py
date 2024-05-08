from azureml.core import Workspace, Dataset, Datastore

ws = Workspace.from_config()

blob_ds = Datastore.get(ws, datastore_name='<DATASTORENAME>')
csv_path = [(blob_ds, 'diabetes.csv')]
tab_ds = Dataset.Tabular.from_delimited_files(path=csv_path)
tab_ds = tab_ds.register(workspace=ws, name='<FOR EXAMPLE: testplan_csv_table_fm>')

df = tab_ds.to_pandas_dataframe()
print(df.head())

# You can also manually upload the dataset to the datastore using aml.azure.com