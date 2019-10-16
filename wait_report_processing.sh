#!/bin/bash

# +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
# |W|A|I|T| |R|E|P|O|R|T| |F|I|R|S|T| |S|T|A|G|E| |P|R|O|C|E|S|S|I|N|G|
# +-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+

#ECOBANK:
#cluster.com.ericsson.em.am.ca.banke.url=https://f5.mtn.com.gh:9007/telcogw/dataexchange/main/telcoin/v1
#cluster.com.ericsson.em.am.ca.banke.url:http://localhost:8080/sp 

#sdpitcpayment:
#cluster.com.ericsson.em.am.ca.provider.url:http://localhost:8080/sp
#cluster.com.ericsson.em.am.ca.provider.url=https://huaweisdp.mtn.com.gh:19313/IB/services

#cis:
#cluster.com.ericsson.em.am.ca.cis.url:http://localhost:8080/sp
#cluster.com.ericsson.em.am.ca.cis.url=https://f5.mtn.com.gh:8880/cisBusiness/Mservice/MobileMoneyHttpService

#StartDateTime; 2019-09-01T17:20;
#EndDateTime; 2019-09-01T17:30;
#Task; com.ericsson.em.am.ca.cis.https://f5.mtn.com.gh:8880/cisBusiness/Mservice/MobileMoneyHttpService/debitcompleted;
#Number of calls (N); 2894;
#Min wait (ms); 73.34;
#Max wait (ms); 2568.65;
#Mean wait (ms); 954.84;
#Tps; 4.82;
#Mean * N; 2763308;
#Success rate (%); 100.00;
#Number of failures; 0;
#Number of errors; 0;

COUNTER=0
for i in $( ls *csv )
do
        echo $i
        myDir=$( echo $i | awk -F- ' { print $6 } ' )
        if [ $COUNTER -eq 0 ]
        then
                mkdir $myDir
                mkdir $myDir/finales
                COUNTER=$( expr $COUNTER + 1 )
        fi
        for j in telcogw huaweisdp cisBusiness
        do
                echo $j
                grep $j $i >> $myDir/finales/$i.final
                grep $j $i >> $myDir/$j
        done
        if [ -s $myDir/finales/$i.final ]
        then
                echo "$myDir/finales/$i.final is ok"
        else
                echo "$myDir/finales/$i.final removed"
                rm -rf $myDir/finales/$i.final
        fi
done
