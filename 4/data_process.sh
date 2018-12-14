sed "s/[]]//g" original-input | sed "s/[[#]//g" | awk '{print $1" "$2 " " $4}'|  sort > input
