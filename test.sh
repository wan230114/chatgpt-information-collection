mkdir -p res
for i in `seq 50`; do
    # outfile=res/$i.`date "+%F_%H-%M-%S_%N"`.txt
    # proxychains4 python3 chat.py >$outfile
    proxychains4 python3 chat.py
done

