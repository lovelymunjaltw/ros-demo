import sys, os

import rostopic
pubs, subs = rostopic.get_topic_list()
topic1_subscribers = [x for x in subs if x[0] == "/topic1"]

subscriber_subscribing_topic1 = [x for x in topic1_subscribers if '/subscriber' in x[2]]

if not subscriber_subscribing_topic1 :
	f = open(os.devnull, 'w')
	sys.stderr = f
	sys.tracebacklimit = 0
	raise Exception("Subscriber is not subscribing to topic1")

