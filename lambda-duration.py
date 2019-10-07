# aws logs filter-log-events --log-group-name "/aws/lambda/sleep" | jq '.events | .[] | select(.message | contains("Duration")) | .message' > output.txt
filepath = 'output.txt'
with open(filepath) as fp:
   line = fp.readline()
   print "This represents the amount of overhead required to invoke the Thread.Sleep"
   print "Duration (ms), Billed Duration (ms)"
   while line:
       durPattern = 'Duration: '
       billedDurPattern = 'Billed Duration: '
       memSizePattern = 'Memory '
       durIndex = line.find(durPattern)
       billedDurIndex = line.find(billedDurPattern)
       memIndex = line.find(memSizePattern)
       print("{}, {}".format(
           line[durIndex+len(durPattern):billedDurIndex - 5], 
           line[billedDurIndex+len(billedDurPattern):memIndex - 5]))
       line = fp.readline()