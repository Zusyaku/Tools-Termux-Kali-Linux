## mediafire
### bash script for downloading mediafire files

##### Download single file from mediafire

```bash
./mediafire url
```

##### Batch-download files from URL list (url-list.txt must contain one mediafire.com url per line)

```bash
./mediafire url-list.txt
```

##### Example:

```bash
./mediafire https://www.mediafire.com/file/479ijso81rt5muh/MGC_6.2.030_MI9SE_V0c.apk/file
```

zippyshare.sh uses `wget` with the `-C` flag, which skips over completed files and attempts to resume partially downloaded files.

### Requirements: `coreutils`, `grep`, `sed`, **`wget`**
