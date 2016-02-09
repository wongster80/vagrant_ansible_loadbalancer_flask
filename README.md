#Vagrant, Ansible, load ballanser VM, Flask (NGINX uWSGI)


##Prepare host:<br>
#### Install Virtualbox<br>
wget http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb<br>
sudo dpkg -i virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb<br>
#### Install Vagrant<br>
wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb<br>
sudo dpkg -i vagrant_1.8.1_x86_64.deb<br>
vagrant plugin install vagrant-vbguest<br>
vagrant plugin install vagrant-hostmanager<br>
#### Install Ansible<br>
apt-get -y install software-properties-common<br>
apt-add-repository -y ppa:ansible/ansible<br>
apt-get update<br>
apt-get -y install ansible<br>
##Run VMs<br>
vagrant box add ubuntu/trusty64<br>
mkdir -p ~/vagrant/test<br>
cd ~/vagrant/test<br>
vagrant init ubuntu/trusty64<br>
vagrant up # to allow modify /etc/hosts by vagrant-hostmanager input sudo password<br>
##Tests:<br>
####test Flask app:<br>
http://localhost:8080/<br>
####test static image:<br>
http://localhost:8080/imgs/welcome.jpg<br>
####test round robin load balancer:<br>
http://localhost:8080/haproxy?stats<br>
#####use benchmark for load balancer:<br>
host$ ab -n 10000 -c 25 http://localhost:8080/<br>
ab - installed apache bench on host machine (sudo apt-get install apache2-utils)<br>
##Softvare version:<br>
Ansible 1.9.2<br>
Vagrant 1.8.1<br>
Flask 0.9<br>
Jinja2 2.6<br>
host: Ubuntu 15.10 wily 4.2.0-23-generic x86_64<br>
