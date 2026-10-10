# Read from the file file.txt and output the tenth line to stdout.
# read file.txt, only print line 10 then quit, -n stops sed printing every line, and 10{p;q} prints line 10 and exits
sed -n '10{p;q}' file.txt