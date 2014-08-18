autopkg-recipes
===============

These are [AutoPkg recipes](https://github.com/autopkg/autopkg), mostly related to making AutoPkg feed a DeployStudio repository (so if there is no existing .pkg recipe, that is also created). The DeployStudio recipes use the .ds suffix. You could use such recipes to move a copy to any location, not just DeployStudio, since the package is copied, not moved. I've also included a template if you wish to create more DeployStudio recipes that leverage existing .pkg recipes as parents.
You will almost certainly need to use a recipe override for the DS repo location, as the pre-entered variables are specific to my setup. I will try to generalize them in the future, but that probably won't help with the need to override.
