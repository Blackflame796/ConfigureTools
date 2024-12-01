sudo mv ~/Library/Containers/Blackflame796/Kaptein/Temp/com.Kaptein.UpdateManager.plist ~/Library/LaunchAgents/
sudo chown root:wheel ~/Library/LaunchAgents/com.Kaptein.UpdateManager.plist
sudo chmod 644 ~/Library/LaunchAgents/com.Kaptein.UpdateManager.plist
sudo launchctl bootstrap gui/501 ~/Library/LaunchAgents/com.Kaptein.UpdateManager.plist