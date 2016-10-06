from azure.storage import CloudStorageAccount


queue_name ='my_queue_name'
storage_account_name = 'my_storage_account_name'
storage_account_key = 'my_storage_account_key'


account = CloudStorageAccount(account_name=storage_account_name,account_key=storage_account_key)

msg = 'this is my message'

service = account.create_queue_service()

service.put_message(queue_name, msg)
