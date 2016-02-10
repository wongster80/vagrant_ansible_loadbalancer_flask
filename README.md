#Vagrant, Ansible, load ballanser VM, Flask (NGINX uWSGI)

![alt tag](https://github.com/dgamanenko/vagrant_ansible_loadbalancer_flask/blob/master/vagrant_ansible.png)

######**this is not best redundancy scheme, but it's extended configuration example

##PROJECT TREE:
```
├── ansible #ansible provison playbooks and templates
│   ├── hosts #ansible inventory file
│   └── playbooks #ansible playbooks and templates
│       ├── setupall.yml #provision playbook
│       └── templates #provision templates
│           ├── haproxy.cfg.j2 #haproxy template
│           ├── nginx.conf #nginx.conf template
│           ├── nginx_site.conf #/etc/nginx/sites-available/{{app_name}}.conf template
│           ├── supervisord.conf #supervisord config template
│           ├── supervisord.sh #supervisord init script template
│           └── supervisor.ini #supervisor program config template
├── ansible.cfg #ansible configuration file (additional configuration for /etc/ansible/ansible.cfg)
├── hello_app_flask #Flask application
│   ├── __init__.py #application file
│   └── static #static resources dir
│       └── welcome.jpg #example image
├── README.md #this file
├── requirements.txt #requirement software to install into virtualenv
├── Vagrantfile_proj #Vagrantfile
└── wsgi.py #run app using uWSGI
```
##REQUIREMENTS:
####Project tested with:
```
Ansible 1.9.2
Vagrant 1.8.1 (ubuntu/trusty64 v.20160201.0.2 VM)
Flask 0.9
Jinja2 2.6
host: Ubuntu 15.10 wily 4.2.0-23-generic x86_64

...modify 'vb.memory' values in Vagrantfile to change VMs virtual memory (in project applied 256Mb per VM)
```
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
vagrant up 
  #to allow add hosts into /etc/hosts by vagrant-hostmanager input sudo password
run 'vagrant provision' command for provison if you have made changes on palybook, templates...
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
####round robin load balancer statistic:
```
http://localhost:8080/haproxy?stats
```
#####use benchmark:
```
host$ ab -n 10000 -c 25 http://localhost:8080/ #ab - installed apache bench on host machine (sudo apt-get install apache2-utils)
```
