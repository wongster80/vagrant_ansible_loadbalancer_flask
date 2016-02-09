# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  #vbguest
  config.vbguest.auto_update = false
  config.vbguest.no_remote = true
  
  #start bash as a non-login shell (fix 'stdin: is not a tty' error)
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
  
  #vagrant plugin to install run command 'vagrant plugin install vagrant-hostmanager'
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true
  
  config.ssh.insert_key = false

  #load balancer
  config.vm.define :lb do |lb_config|
      lb_config.vm.box = "ubuntu/trusty64"
      lb_config.vm.hostname = "lb"
      lb_config.vm.network :private_network, ip: "10.0.15.11"
      lb_config.vm.network "forwarded_port", guest: 80, host: 8080
      lb_config.vm.provider "virtualbox" do |vb|
        vb.memory = "192"
      end
  end
  
  
  #web servers
  N=2 #web servers number
  (1..N).each do |i|
    config.vm.define "web#{i}" do |node|
        node.vm.box = "ubuntu/trusty64"
        node.vm.hostname = "web#{i}"
        node.vm.network :private_network, ip: "10.0.15.2#{i}"
        node.vm.network "forwarded_port", guest: 80, host: "808#{i}"
        node.vm.provider "virtualbox" do |vb|
          vb.memory = "192"
        end
    # Execute  ansible provisioner once,
    # when all the machines are up and ready.
       if i == N
         node.vm.provision :hostmanager
         node.vm.provision :ansible do |ansible|
           # Disable default limit to connect to all the machines
           #ansible.sudo = true
           ansible.limit = "all"
           ansible.inventory_path ="ansible/hosts"
           ansible.playbook = "ansible/playbooks/setupall.yml"
           #ansible.verbose =  'vvvv'
         end
       end

    end
  end

end
