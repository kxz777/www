# www
Automatização do trabalho de venda de seguidores

Configurações do Servidor

go to light sail
centos (os only)
sudo su -
timedatectl set-timezone America/Sao_Paul
yum install -y python3
yum install screen
pip3 install selenium
pip3 install fake-useragent
pip3 install selenium-wire
pip3 install lxml
pip3 install keyboard
pip3 install requests
yum install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum install ./google-chrome-stable_current_*.rpm
rm google-chrome-stable_current_x86_64.rpm
google-chrome --version
Baixar chrome driver correspondente a versao do passo anterior deste site: https://sites.google.com/a/chromium.org/chromedriver/downloads
Usar FileZilla e jogar bin baixado em /home/centos
No terminal usar root privilege (sudo su -) para jogar o arquivo que está em /home/centos para usr/bin, para mover usar o comando mv /home/centos/chromedriver /usr/bin
chmod 777 /usr/bin/chromedriver
chmod 777 /home/centos/www (para poder jogar arquivos pelo visual studio)
chmod 777 /home/centos/www/temp (para pode deletar arquivos pelo filezilla)
Em /home/centos/www criar pasta temp


Para deletar temp:

find /tmp -type f -mmin +1 -delete

Para cronjobs

#aciona cronjobs das atualizacoes de Admin. Roda as 03 am
#30 3 * * * python3 /home/centos/www/index.py
