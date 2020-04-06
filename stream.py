prompt = "Enter your file_id:" 
file_id = input(prompt)

prompt = "Enter your api_key:"
api_key = input(prompt)

print(f"https://www.googleapis.com/drive/v3/files/{file_id}/?key={api_key}&alt=media")
