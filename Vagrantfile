# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "dbbalancer" do |dbbalancer|
    dbbalancer.vm.box = "ubuntu/bionic64"
    dbbalancer.vm.box_check_update = false
    dbbalancer.vm.network "private_network", ip: "192.168.56.20"
    dbbalancer.vm.hostname = "dbbalancer"
    dbbalancer.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "512"
      vb.name = "dbbalancer"
      end
  end

  config.vm.define "database1" do |database1|
    database1.vm.box = "ubuntu/bionic64"
    database1.vm.box_check_update = false
    database1.vm.network "private_network", ip: "192.168.56.21"
    database1.vm.hostname = "database1"
    database1.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "512"
      vb.name = "database1"
      end
  end

  config.vm.define "database2" do |database2|
    database2.vm.box = "ubuntu/bionic64"
    database2.vm.box_check_update = false
    database2.vm.network "private_network", ip: "192.168.56.22"
    database2.vm.hostname = "database2"
    database2.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "512"
      vb.name = "database2"
      end
  end

  config.vm.define "database3" do |database3|
    database3.vm.box = "ubuntu/bionic64"
    database3.vm.box_check_update = false
    database3.vm.network "private_network", ip: "192.168.56.23"
    database3.vm.hostname = "database3"
    database3.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "512"
      vb.name = "database3"
      end
  end

  config.vm.define "app1" do |app1|
    app1.vm.box = "centos/7"
    app1.vm.box_check_update = false
    app1.vm.network "private_network", ip: "192.168.56.30"
    app1.vm.hostname = "app1"
    app1.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "1024"
      vb.name = "app1"
      end
  end

  config.vm.define "app2" do |app2|
    app2.vm.box = "ubuntu/bionic64"
    app2.vm.box_check_update = false
    app2.vm.network "private_network", ip: "192.168.56.40"
    app2.vm.hostname = "app2"
    app2.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "1024"
      vb.name = "app2"
      end
  end

  config.vm.define "haproxy" do |haproxy|
    haproxy.vm.box = "ubuntu/bionic64"
    haproxy.vm.box_check_update = false
    haproxy.vm.network "private_network", ip: "192.168.56.10"
    haproxy.vm.hostname = "haproxy"
    haproxy.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "512"
      vb.name = "haproxy"
      end
  end
end
