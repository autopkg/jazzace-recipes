# AdobeAdminConsole Recipes

The AdobeAdminConsole.pkg recipe leverages the [AdobeAdminConsolePackagesPkgInfoCreator](https://github.com/autopkg/dataJAR-recipes/blob/master/Adobe%20Admin%20Console%20Packages/AdobeAdminConsolePackagesPkgInfoCreator.py) custom processor from dataJAR to extract version information from an Adobe pkg installer and then add that version information to the pkg name. This makes it suitable for many more AutoPkg workflows than just the munki-related ones that the dataJAR recipes support.

The AdobeAdminConsolePackagesPkgInfoCreator processor does have some dependencies. The following workflow will ensure that you have met all the requirements of the processor.

1. Create and Download the “Package” you wish to use from the [Adobe Admin Console](https://adminconsole.adobe.com). This will generate a disk image (.dmg).
2. Mount the Disk Image and run the Adobe Package Downloader app contained in the image. Download the installer to the default location (`~/Downloads`). A zip archive will be downloaded.
3. When the download is completed, quit Adobe Package Downloader and go to the downloaded zip archive in `~/Downloads`. Expand the zip archive (e.g., by double-clicking on it).
4. If you have not already created a recipe override of the AdobeAdminConsole.pkg recipe (or a related child recipe, such as the `.jamf` recipe in this directory), do so now. If you are maintaining more than one Adobe installer pkg, make sure that each override gets a unique name (e.g., `autopkg make-override AdobeAdminConsole.pkg -n AdobePremiere.pkg`).
5. In the override, set the value for the NAME input variable to whatever you used in the Adobe Admin Console (it will also be the name of the folder containing the expanded archive in `~/Downloads`).
6. Run the recipe override. A copy of the Installer pkg with a version number appended to the name will be in the recipe’s cache when the run is completed.

You can then either manually upload the pkg to your management system of choice or you can write a child recipe to do the uploading (and perhaps other automation) for you. The path to the versioned pkg is stored in the `pkg_path` variable as you would expect. For Jamf Pro users, the [JamfUploader processors](https://github.com/autopkg/grahampugh-recipes/tree/main/JamfUploaderProcessors) are very useful in this context. The .jamf recipe I use to upload the pkg and set/update the policy is included in this repo. As mentioned, I override the `.jamf` recipe, not the `.pkg` recipe because of this.

To review, the expanded zip archive that you download from Adobe (in a 2-step process) must be located in `~/Downloads` for the custom processor to find it and the name of that expanded archive (and the related installer inside the archive) must be specified in the NAME input variable in your override.
