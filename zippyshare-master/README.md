## zippyshare
### bash script for downloading zippyshare files

##### Download single file from zippyshare

```bash
./zippyshare url
```

##### Batch-download files from URL list (url-list.txt must contain one zippyshare.com url per line)

```bash
./zippyshare url-list.txt
```

##### Example:

```bash
./zippyshare https://www3.zippyshare.com/v/CDCi2wVT/file.html
```

zippyshare.sh uses `wget` with the `-C` flag, which skips over completed files and attempts to resume partially downloaded files.

### Requirements: `coreutils`, `grep`, `sed`, **`wget`**
