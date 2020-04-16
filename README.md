jazzace-recipes
===============

This is my public AutoPkg recipe repository, included in the [AutoPkg project](https://github.com/autopkg/autopkg). Some recipes I have written for teaching/presentation/blogging purposes may also show up in [my personal GitHub repo](https://github.com/jazzace).

The recipes here are generally one of two kinds:
* Supporting products used by performing and visual artists, especially in a University context;
* Supporting usage contexts where you need to copy a package without version information to a local directory.

This second kind, the “.ds” type of recipe (invented here), was originally used to feed the Packages folder of a DeployStudio repository. With the near-elimination of the kind of workflows at which DeployStudio excelled, many of those recipes are not of use to most. (Jamf users may find the .pkg recipes that were created to work with DeployStudio the most useful remnant.) Having said this, the .ds recipes can still be used to copy a package installer without version information in the filename to a local directory. One possible application would be to keep the installers you use in [MDS](https://twocanoes.com/products/mac/mac-deploy-stick/) up to date.

Should you still find value in the .ds recipe type, there is a template included in this repository that walks you through the settings needed to make it work.