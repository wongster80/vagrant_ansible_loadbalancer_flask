#Vagrant, Ansible, load ballanser VM, Flask (NGINX uWSGI)


##prepare host:

wget http://download.virtualbox.org/virtualbox/5.0.14/virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb

wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb

sudo dpkg -i virtualbox-5.0_5.0.14-105127~Ubuntu~wily_amd64.deb

sudo dpkg -i vagrant_1.8.1_x86_64.deb

vagrant plugin install vagrant-vbguest

vagrant plugin install vagrant-hostmanager

vagrant box add ubuntu/trusty64

mkdir -p ~/vagrant/test

cd ~/vagrant/test

vagrant init ubuntu/trusty64

vagrant up # to allow modify /etc/hosts by vagrant-hostmanager input sudo password
