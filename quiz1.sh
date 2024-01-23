echo "user: $USER"
echo "name: Yutong Ji"

gunzip -c dictionary.gz | grep -v "[^muocatf]" | grep "a" | grep -E "[muocatf].{2}[muocatf]" | wc

gunzip -c dictionary.gz | grep -v "[^taibrnl]" | grep "b" | grep -E "[taibrnl]].{2}[taibrnl]" | wc

gunzip -c dictionary.gz | grep -v "[^maocdin]" | grep "c" | grep -E "[maocdin].{2}[maocdin]" | wc

gunzip -c dictionary.gz | grep -v "[^anozigr]" | grep "z" | grep -E "[anozigr].{2}[anozigr]" | wc