AdobeFlashPlayerDLA Recipes
===========================

These recipes are designed to be used by SysAdmins who have a Distribution License Agreement (DLA) with Adobe (that's all of you, right?). You use the super secret URI that Adobe provided you to gather the information that this recipe needs, which you enter in an override.

Current Status - November 2016
------------------------------
* Adobe has discontinued the ESR version of Flash Player. Because of this, the AdobeFlashPlayerDLA recipes are now removed from my repo.
* If you want the most current version of Flash Player and still have an active agreement with Adobe that has "distribution4" in the URL, you may still use the AdobeFlashPlayerDLACurrent recipe set.
* If you have had to renew your DLA after a particular date in October 2016, you are now required to login with an Adobe ID. Until such time as I (or someone else in the community) can craft a recipe that logs you in with your Adobe ID, the only automated method of retrieving packages suitable for mass deployment is using the recipes in the main AutoPkg recipe repo.

Development Plan
----------------
With the writing being on the wall for Flash, I'm not going to spend a lot of time trying to chase Adobe's moving target for Mac Admins. If I can determine a way to login with the designated Adobe ID and then download, I'll create a new set of recipes.