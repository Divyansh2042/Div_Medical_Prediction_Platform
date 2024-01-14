import pickle
from pathlib import  Path
import streamlit_authenticator as stauth

names = ["Peter Parker","Divyansh Singh"]
usernames = ["pparker","dsingh"]
passwords = ["abc123", "div2003"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

