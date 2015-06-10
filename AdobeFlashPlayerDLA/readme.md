AdobeFlashPlayerDLA Recipes
===========================

These recipes are designed to be used by SysAdmins who have a Distribution License Agreement (DLA) with Adobe (that's all of you, right?). You use the super secret URI that Adobe provided you to gather the information that this recipe needs, which you enter in an override.

Current Status
--------------
* If you are using the ESR version of Flash Player, use the AdobeFlashPlayerDLA recipe set.
* If you want the most current version of Flash Player, use the AdobeFlashPlayerDLACurrent recipe set.

Background Information
----------------------
My original attempt at writing this set of recipes was a bit clumsy (AdobeFlashPlayerDLA), requiring that you enter the Major Version number as well as retrieve part of the link's URL manually from that super secret page Adobe provided for you. Yet it added one bit of functionality that the main repo recipe did not: support for the Extended Support Release (ESR) version.

Now that I have a little more skill writing recipes (and using the URLTextSearcher processor), I've provided a more robust set of recipes (AdobeFlashPlayerDLACurrent) that grab the latest version of the Flash Player pkg installer without the need to increment the Major Version number. It's also simpler in that you just provide the URI that Adobe provided you — no more grabbing the link on that page. (I've intentionally obscured part of the URI in the regular expression that finds the download so as to not run afoul of Adobe's license agreement.) Unfortunately, it does not support ESR, hence the need to maintain both sets of recipes.

Development Plan
----------------
Once I learn how to code a bit in Python, I would like to write a custom processor that combines the functionality of the two current sets of recipes, much like the Firefox recipes in the main repo allow you to specify "current" or "current-esr" in an input key and let it do the work for you (after all, isn't that the point of AutoPkg?). It would use the simpler method of specifying the URI that Adobe provided you in your override. There is no timeline for this. When completed, I expect that the combined recipe will take over the old AdobeFlashPlayerDLA identifiers and the AdobeFlashPlayerDLACurrent recipes will become deprecated.