Finale Update Recipes
=====================

The FinaleUpdate recipes have been removed.

Finale Full Installer Recipes
=============================
Since the downloads for the full Finale installer are only available through your MakeMusic account, and because the current installer package (v.25 and later) does not work as a deployable installer, a new pkg recipe has been written to bundle the installer pkg and a postinstall script into a new package that will run correctly in a management system (e.g., ARD, Jamf Pro). MakeMusic calls this a Silent Install. To use the recipe, run it with the `--pkg` option, specifying the Disk Image that contains the Finale Installer. For example:

`autopkg run Finale_NoGarritan.pkg --pkg /path/to/Finale26.2.dmg`

The file silentInstallerChoices.plist must be in the same directory as the recipe you are running (usually AutoPkg's RecipeOverrides directory). You can obtain a copy of the file from within this repo.

Currently, the only existing recipe (`Finale_NoGarritan.pkg`) does not install the Garritan Instruments nor the ARIA player. It is possible to craft a recipe that does this, but since the author does not have a need to do this, you are welcome to copy that recipe and create your own. The major changes would be:
* Copy the full disk image to the new package, not just the pkg installer;
* Change references to the `Install Finale.pkg` to account for the location inside the disk image;
* Add steps to the postinstall script to install the Garritan ARIA player (first) and the Instruments using the instructions in the [MakeMusic Help Center article](https://makemusic.zendesk.com/hc/en-us/articles/115007423647-Commands-to-silently-install-Finale-unattended-installer-#installMac).
