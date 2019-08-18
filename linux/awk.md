AWK

remove duplicate lines (keep order)

```awk '!visited[$0]++' your_file > deduplicated_file``` --> [reference](https://iridakos.com/how-to/2019/05/16/remove-duplicate-lines-preserving-order-linux.html)