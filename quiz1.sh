echo "user: $USER"
echo "name: Yutong Ji"

gunzip -c dictionary.gz | grep -v "[^muocatf]" | grep "a" | grep -E "[muocatf].{2}[muocatf]" | wc
