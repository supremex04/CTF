```
Problem:
Files can always be changed in a secret way. Can you find the flag? cat.jpg
```

```
exiftool cat.jpg | grep License | awk -F ": " '{print $2}' | base64 -d
Base 64 decoding the License

Flag: picoCTF{the_m3tadata_1s_modified}
```