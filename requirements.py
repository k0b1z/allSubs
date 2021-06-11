#!/usr/bin/env python

import os

os.system("go get -u github.com/tomnomnom/assetfinder")
os.system("mv /root/go/bin/assetfinder /usr/bin")

os.system("go get -u github.com/tomnomnom/anew")
os.system("mv /root/go/bin/anew /usr/bin")

os.system("GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder")
os.system("mv /root/go/bin/subfinder /usr/bin")

os.system("GO111MODULE=on go get -v github.com/projectdiscovery/chaos-client/cmd/chaos")
os.system("mv /root/go/bin/chaos /usr/bin")

os.system("git clone https://github.com/gwen001/github-search.git")
