Driver Downloads Directly from Epson
====================================

These recipes require that you manually determine the "oid" of your Epson product. You can do this by going to the Drivers and Downloads section of the U.S. web site and clicking on the appropriate links until you get to the Drivers and Downloads page for your product. Then capture the URL of that page and look for "oid=" and the number that follows it (usually six digits long). For example, the URI for the Stylus Pro 9900 on the U.S. site looks like this:

````
   http://www.epson.com/cgi-bin/Store/support/supDetail.jsp?BV_UseBVCookie=yes&oid=119098&prodoid=63079720&infoType=Downloads&detected=yes&platform=OSF_M_X10
````

In this case, the oid would be 119098. Enter this number as the value for the OID input key in the recipe override (you _will_ require an override, but you can also create separate overrides for each Epson product you use).

You will also notice that the version of OS X is also present in that URI. Enter the desired major version of OS X (expressed as the number after the decimal point) as the OSX_VERSION input key. For example, Yosemite is 10, Mavericks is 9.
