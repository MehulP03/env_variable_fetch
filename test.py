import os
print(os.environ)
secrets = os.environ.get('MY_SECRET')
print(secrets)
