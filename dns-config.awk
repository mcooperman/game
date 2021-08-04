#
BEGIN {flag=0;}
{if (flag) {print;}}
/^DNS configuration \(for scoped queries\)/ {flag=1; print;}
END { print NR }
