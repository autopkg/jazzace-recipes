Pro Driver Downloads Directly from Epson
========================================

This recipe family requires that you find the support page for your product and copy that URL for use as the base string for the SEARCH_URL key in your override. In order for the recipe to work, the target OS must be explicitly specified in the URL.

Recommended Procedure for Creating URL:
---------------------------------------
1. Go to the Epson site for your country.
2. Find the support page for your Epson device.
3. The support page will attempt to determine your current OS version and will display that in a pop-up menu on the page. If that is OS you are targeting for deployment, temporarily change the value in that popup menu to any other OS, wait a second (enough for the page to quickly reload), and then change to the OS you are targeting for deployment. If you are targeting a different OS, then directly change the OS in the popup menu. 
4. Copy the URL.
5. Create an override of this recipe (or edit an existing override).
6. In the Input section, paste the URL that you copied earlier into the string for SEARCH_URL.
7. Check the URL you just pasted. Confirm that it ends with something that looks like the following: 
    ?review-filter=macOS+15.x
(substituting the number of the major macOS version as appropriate). You can append this string if it is not present. 

For example, the URL for the Epson SureColor P9000 fetched from the Canadian Epson site with macOS Sequoia as the deployment OS is:
````
	https://epson.ca/Support/Printers/Professional-Imaging-Printers/SureColor-Series/Epson-SureColor-P9000-Standard-Edition/s/SPT_SCP9000SE?review-filter=macOS+15.x
````
(The US URL is the same, except it is .com instead of .ca. Only the Canadian and US sites have been tested.)

When Epson was using separate code signing authorities for older and new products, it was
necessary to have separate recipes (EpsonProDrivers and EpsonSureColorDrivers). Now that 
Epson is using the same authority for all new releases, the EpsonSureColorDrivers.download recipe has been turned into a stub recipe that points to EpsonProDrivers.download. It will be removed at a future date.

As well, if you need to extract the pkg from the disk image and rename it without a version number included, use the .ds recipe, as the EpsonProDrivers.pkg and EpsonProDriversVersioned.pkg recipes will be merged in the near future to only support versioned packages.
