jazzace-recipes
===============

This is my public AutoPkg recipe repository, included in the [AutoPkg project](https://github.com/autopkg/autopkg). Some recipes I have written for teaching/presentation/blogging purposes may also show up in [my personal GitHub repo](https://github.com/jazzace).

The recipes here that are being actively maintained (until I retire, at least)…
* support products used by performing and visual artists, especially in a University context;
* are `.pkg` recipes for titles that I use;
* are `.jamf` recipes, tailored to my needs, that use the [JamfUploader processors](https://github.com/autopkg/grahampugh-recipes/tree/main/JamfUploaderProcessors) to feed a Jamf Pro management system; or
* support usage contexts where you need to copy a package without version information to a local directory.

That last kind, the `.ds` type of recipe (invented here), was originally used to feed the Packages folder of a DeployStudio repository. With the near-elimination of the kind of workflows at which DeployStudio excelled, many of those recipes are not of use to most. Having said this, the `.ds` recipes can still be used to copy a package installer without version information in the filename to a local directory. One possible application would be to keep the installers you use in [MDS](https://twocanoes.com/products/mac/mac-deploy-stick/) up to date.

Recipe templates are available for [some of the `.jamf` recipe varieties I use](https://github.com/autopkg/jazzace-recipes/tree/master/JamfTemplates/RecipeTemplates) as well as [the old `.ds` recipes](https://github.com/autopkg/jazzace-recipes/blob/master/Template.ds.recipe).

I have written a lot of [blog posts on AutoPkg](http://maclabs.jazzace.ca/) (look for the 📦 symbol), contributed to the [AutoPkg Wiki](https://github.com/autopkg/autopkg/wiki), and have given a number of [conference presentations](https://maclabs.jazzace.ca/resources/index.html) as a way to give back to the AutoPkg project.