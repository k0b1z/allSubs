<h4 align="center">allSubs</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
</p>

# About
It is a tool for searching subdomains.
Combined automate [assetfinder](https://github.com/tomnomnom/assetfinder), [subfinder](https://github.com/projectdiscovery/subfinder), [chaos](https://github.com/projectdiscovery/chaos-client), [crt.sh](https://crt.sh/) and [github-search](https://github.com/gwen001/github-search).
To use the tool, you must have previously installed: [GO](https://golang.org/), [python3](https://www.python.org/downloads/), [jq](https://stedolan.github.io/jq/) and [Git](https://git-scm.com/) .

# Install
With Git installed, download the project:
```
git clone https://github.com/vitorsugai/allSubs.git
```
Inside the project's root folder, you can use the following command to install the necessary dependencies:
```
python3 requirements.py
```
Or you can also install the dependencies yourself. They are: [assetfinder](https://github.com/tomnomnom/assetfinder), [subfinder](https://github.com/projectdiscovery/subfinder), [chaos](https://github.com/projectdiscovery/chaos-client), [anew](https://github.com/tomnomnom/anew) and [github-search](https://github.com/gwen001/github-search) .

# Usage
```
python3 python3 allSubs.py domainExample.com reconExample.txt
```
domainExample.com can be replaced by the host that will be scanned.
reconExample.txt must be changed to the name of the file that will save the subdomains at the end of the scanner.
