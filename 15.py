import zipfile as zp
with zp.ZipFile("test2.zip","w") as zipf:
    zipf.write("10.py")
    zipf.write("11.py")



