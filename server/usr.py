import toml
def check(usr):
  try:
    open(f'users/{usr}.toml').close()
    return True
  except:
    return False
def record(usr):
  k=toml.load(open(f"users/{usr}.toml"))
  print(k)