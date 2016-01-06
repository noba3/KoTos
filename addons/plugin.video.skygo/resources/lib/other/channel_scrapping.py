import urllib2
import marshal as pickle

def channel_scraper(filename):

	url = "http://go.sky.com/vod/page/tvListing.do"

	#Search for channel information to pass to launcher
	channel_database = []
	
	def get_all_data():
		# Get all data
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
		req = urllib2.Request(url, None, headers)
		html = urllib2.urlopen(req).read()
		#finds channel list
		channel_list = html.find('channelList')
		channel_list_start =  html.find('[',channel_list)
		channel_list_end = html.find(']',channel_list_start)
		channel_list = html[channel_list_start:channel_list_end]
		return channel_list

	#Finds channel start & end
	def find_a_channel(channel_list):
		start_channel = channel_list.find("{")
		end_channel = channel_list.find("}")
		channel = channel_list[start_channel:end_channel+1]
		return channel, end_channel	

	def get_channel_info(channel):
	#Finds channel name
		start_ch = channel.find(":") + 4
		end_ch = channel.find("\\",start_ch)
		channel_name = channel[start_ch:end_ch]
	#find EPG number
		start_epg = channel.find(":", end_ch) + 4
		end_epg = channel.find("\\",start_epg)
		epg = channel[start_epg:end_epg]
	#find epgchild
		start_epgchild = channel.find(":", end_epg) + 4
		end_epgchild = channel.find("\\",start_epgchild)
		epgchild = channel[start_epgchild:end_epgchild]
	#find urls
		start_url = channel.find(":", end_epgchild) + 4
		end_url = channel.find("\\",start_url)
		url = channel[start_url:end_url]
		return channel_name, epg, url, epgchild
		
	def scrap_channels(channel_list):
		while True:
			channel, end_channel = find_a_channel(channel_list)
			if channel:
				channel_name, epg, url, epgchild= get_channel_info(channel)
				channel_database.append([channel_name, epg, url, epgchild])
				channel_list = channel_list[end_channel+1:]
			else:
				del channel_database[-1]
				break
	
	scrap_channels(get_all_data())
	pickle.dump(channel_database,  open(filename, "wb"))
	return channel_database