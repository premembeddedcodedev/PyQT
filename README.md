cat /etc/*release*
sudo -s apt-get remove docker docker-engine docker.io containerd runc
curl -fsSL https://get.docker.com -o get-docker.sh
sudo -s sh get-docker.sh 
sudo docker --version
sudo docker version
mkdir docker
cd docker/
docker run docker/whalesay cowsay boo
sudo -s docker run docker/whalesay cowsay boo
docker ps
sudo -s docker ps
sudo -s docker run ubuntu
sudo -s docker ps -a
sudo -s docker run ubuntu sleep 5
sudo -s docker ps -a

sudo -s docker search centos
sudo -s docker run centos
sudo -s docker ps 
sudo -s docker ps -a


sudo -s docker images
sudo -s docker run -d centos
sudo -s docker run -d ubuntu
sudo -s docker run -d docker/whalesay
sudo -s docker images

/* Delete the images from process list*/
sudo -s docker ps -a
sudo -s docker rm ce037c075ff2


/* Delete the images from process list*/
sudo -s docker images
sudo -s docker rmi ubuntu

/* CentOS installation example */
sudo -s docker pull centos
sudo -s docker images
sudo -s docker ps -a
sudo -s docker run centos
sudo -s docker run -it centos

/* Delete the instance from process list and image list*/
sudo -s docker rm ffe348c89ee4 88877d729398
sudo -s docker ps -a 
sudo -s docker images
sudo -s docker rmi centos

history > docker.txt
