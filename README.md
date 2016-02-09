#Vagrant, Ansible, load ballanser VM, Flask (NGINX uWSGI)
##REQUIREMENTS:
Project tested with:

Ansible 1.9.2

Vagrant 1.8.1

Flask 0.9

Jinja2 2.6

host: Ubuntu 15.10 wily 4.2.0-23-generic x86_64
##QUICK START:
#### Install Virtualbox
```
wget http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb
sudo dpkg -i virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb
```
#### Install Vagrant
```
wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
sudo dpkg -i vagrant_1.8.1_x86_64.deb
vagrant plugin install vagrant-vbguest
vagrant plugin install vagrant-hostmanager
```
#### Install Ansible
```
apt-get -y install software-properties-common
apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get -y install ansible
```
####Run VMs
```
vagrant box add ubuntu/trusty64
mkdir -p ~/vagrant/test
cd ~/vagrant/test
vagrant init ubuntu/trusty64
cp Vagrantfile_proj Vagrantfile
vagrant up #to allow modify /etc/hosts by vagrant-hostmanager input sudo password
```
##Tests:
####test Flask app:
```
http://localhost:8080/
```
####test static image:
```
http://localhost:8080/imgs/welcome.jpg
```
####test round robin load balancer:
```
http://localhost:8080/haproxy?stats
```
#####use benchmark for load balancer:
```
host$ ab -n 10000 -c 25 http://localhost:8080/
ab - installed apache bench on host machine (sudo apt-get install apache2-utils)
```
