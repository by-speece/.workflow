sudo cp -rf  ~/.workflow/modules/universalbright/install/systemd/universalbright.service /etc/systemd/system/universalbright.service
sudo chmod 644 /etc/systemd/system/universalbright.service 
sudo mkdir /etc/universalbright
sudo cp -rf ~/.workflow/modules/universalbright/install/systemd/script.sh /etc/universalbright/script.sh
sudo systemctl start universalbright.service 
sudo systemctl enable universalbright.service 
