#!/usr/bin/env python

import os
import sys
import yaml

if len(sys.argv) == 3:
    print("####################################################")
    print("##         _ _  _____       _                     ##")
    print("##        | | |/  ___|     | |                    ##")
    print("##    __ _| | |\ `--. _   _| |__  ___             ##")
    print("##   / _` | | | `--. \ | | | '_ \/ __|            ##")
    print("##  | (_| | | |/\__/ / |_| | |_) \__ \            ##")
    print("##   \__,_|_|_|\____/ \__,_|_.__/|___/  --- k0b1z ##")
    print("####################################################")
    domain = str(sys.argv[1])

    assetfinder = "assetfinder -subs-only " + domain + " | anew assetFinderDomain.txt"
    os.system(assetfinder)

    subfinder = "subfinder -silent -d " + domain + " | anew subFinderDomain.txt"
    os.system(subfinder)

    with open("config.yaml", 'r') as config:
        cfg = yaml.safe_load(config)

    chaos_key = cfg["chaos_key"]
    os.environ["CHAOS_KEY"] = chaos_key

    chaos = "chaos -silent -d " + domain + " | anew chaosDomain.txt"
    os.system(chaos)

    crtsh_url = "https://crt.sh/?q=%25." + domain + "&output=json"
    crtsh = "curl -s " + '"' + crtsh_url + '"' + " | jq -r '.[].name_value' | sed 's/\*\.//g' | anew crtshDomain.txt"
    os.system(crtsh)

    github_key = cfg["github_key"]
    github = "python3 github-search/github-subdomains.py -t " + github_key + " -d " + domain + " | anew gitHubDomain.txt"
    os.system(github)

    conc = "cat assetFinderDomain.txt subFinderDomain.txt chaosDomain.txt crtshDomain.txt gitHubDomain.txt | sort | anew " + str(sys.argv[2])
    print(conc)
    os.system(conc)

    os.system("rm assetFinderDomain.txt")
    os.system("rm subFinderDomain.txt")
    os.system("rm chaosDomain.txt")
    os.system("rm crtshDomain.txt")
    os.system("rm gitHubDomain.txt")

else:
    print("USAGE: python3 allSubs.py domainExample.com reconExample.txt")
    sys.exit(1)
