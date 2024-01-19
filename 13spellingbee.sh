gunzip -c dictionary.gz | grep -v "[^zoniacr]" | grep "r" | grep -E "[zoniacr].{2}[zoniacr]" | wc
