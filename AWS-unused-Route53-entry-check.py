import boto3
import os
import slackweb

sum_profile=0

##Below lines will connect to the AWS Route53 Client##
def r53(session,account):
	t = open("R53_SEC_output.txt","+w")
	lst=list()
	a_lst=list()
	c_lst=list()
	f_dict={}
	g_dict={}
	f_availst=list()
	f_unavailst=list()
	g_availst=list()
	g_unavailst=list()
	final_availst=list()
	final_unavailst=list()

	client = session.client('route53')


	##Below lines will get the Hosted Zone Ids from the Account's Route 53##

	dict=client.list_hosted_zones()
	dict_1=dict['HostedZones']
	for i in dict_1:
	    if i['Id'] not in lst: lst.append(i['Id'].split('/')[2])

	##Below lines will print out the FQDNs for A and CNAME record Sets and will also print the resource record set for the eNAMEs rom each of the above Hosted Zones##

	for i in lst:
		response = client.list_resource_record_sets(
			HostedZoneId=i
		)
		dict=response['ResourceRecordSets']
		for i in dict:
			if (i['Type']) == "A" :a_lst.append(i['Name'])
			elif (i['Type']) == "CNAME" :c_lst.append(i['ResourceRecords'][0]['Value'])
			else: continue


	d={}
	d.update(f_dict)
	d.update(g_dict)
	for i in c_lst:
		x=os.system('host '+i)
		if x !=0: f_unavailst.append(i)
		else: continue
	print(f_unavailst)
	str = '\n'.join(f_unavailst)
	t.write(str)
	t.close()

def <profile name>():
         #sum=0
         global sum_profile
         session = boto3.Session(profile_name=<profile name>,region_name=<region code>)
         r53(session,<profile name>)
         f_handle=open('R53_SEC_output.txt','r')
         for i in f_handle:
             sum_profile=sum_profile+1
if __name__ == '__main__':
        <profile name>()

session = boto3.Session(profile_name=<profile name>,region_name=<region code>)
s3=session.client('s3')
s3.upload_file('/Users/rramani/python_scripts/R53_SEC_output.txt','unusedr-53-entries','SEC.txt')

slack = slackweb.Slack(url="")

slack.notify(text="*Summary of Unused Route53 Check Results(Checking only CNAMES for now)*")
slack.notify(text="=============================")

if sum_profile==0:
   slack.notify(text="Number of Unused Route-53 entries(URLs) in the `<profile name>` account = 0")
else:
   slack.notify(text="Number of Unused Route-53 entries(URLs) in the `<profile name>` account = "+str(sum_sec_usw2))
