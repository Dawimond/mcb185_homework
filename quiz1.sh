echo "user: $USER"
echo "name: Yutong Ji"

gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^muocatf]" | grep "a" | grep -E "[muocatf].{2}[muocatf]" | wc

gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^taibrnl]" | grep "b" | grep -E "[taibrnl].{2}[taibrnl]" | wc

gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^maocdin]" | grep "c" | grep -E "[maocdin].{2}[maocdin]" | wc

gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^anozigr]" | grep "z" | grep -E "[anozigr].{2}[anozigr]" | wc

gunzip -c ../MCB185/data/jaspar2024_core.transfac.gz | uniq -c | grep tax | cut -d ":" -f -2 | sort -n

echo "Co-author: Akshat, Roger"