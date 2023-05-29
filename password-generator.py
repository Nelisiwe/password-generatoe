import random

def generate_password(length=12):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]<>,.?/;':"

  password = "".join(random.choice(alphabet) for _ in range(length))

  return password

def main():
  password = generate_password()
  print(password)

if __name__ == "__main__":
  main()
