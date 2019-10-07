# NB: add & to make it a background job instead.
 for i in {0..100}
    do
        echo $i
        aws stepfunctions start-execution --state-machine-arn "<TODO>"
 done
