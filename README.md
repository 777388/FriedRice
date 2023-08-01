# FriedRice
Sugar and Spice

First be sure to download dependencies, you'll need GOLANG, as well as www.github.com/lc/gau

sudo apt install hellfire dnsutils

Next I want you to create a rootservers.txt File, do not copy rootserver ips from other people as each is designated their own rootservers which contain virtual servers, just put in your home address

0.0.0.0

127.0.0.1

dig +trace will then begin to collect IPs to put into rootservers.txt every time you run this program, so the more you use this the more variability of responses you will obtain. Each collection should give you variation on the file structure of what was obtained by GAU, with this methodology you should be able to gain access to what was meant for you no matter what virtual machine they have you set on in your browser.

