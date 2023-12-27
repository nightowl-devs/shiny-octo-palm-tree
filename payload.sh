sudo apt install python3
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get upgrade 
sudo apt install python3-pip
sudo pip install cloudscraper requests PySocks icmplib scapy
sudo ufw allow 22
sudo ufw allow 5512
sudo ufw allow 5511
sudo ufw allow 1:5655/tcp
sudo ufw allow 1:5655/udp
sudo ufw enable
sudo ufw status
