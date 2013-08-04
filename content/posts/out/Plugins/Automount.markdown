title: Automount
date: 2013-08-03
This plugin can automatically "mount" notebooks when needed. It can e.g. be used to connect with remote drives or unlock an encrypted drive when zim is trying to open a specific notebook.

**Dependencies:** This plugin has no additional dependencies.

Config file
-----------
The paths to be automounted and the commands to mount them are configured in a config file "``~/.config/zim/automount.conf``" (this file is in the same folder where the other zim config should be found).

The config file has a group for each path, followed with options. Currently the only supported option is a "mount" command. For example if you have an Ubuntu setup to encrypt the "``~/Documents``" folder, you can create a config file with the following two lines:

	[Path ~/Documents]
	mount=xterm -e /usr/bin/ecryptfs-mount-private

The result will be that whenever zim tries to access an notebook stored under the Documents folder while that folder is not decrypted, it will prompt a terminal window to ask for the password and then mount the folder. If it fails, you still get an "notebook not found" error.

Similarly you can configure various scripts of your own design.

