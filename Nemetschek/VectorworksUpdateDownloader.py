#!/usr/local/autopkg/python


from __future__ import absolute_import

import os
import subprocess

from autopkglib import Processor, ProcessorError

__all__ = ["VectorworksUpdateDownloader"]


class VectorworksUpdateDownloader(Processor):
    """This processor uses the Vectorworks Installation Manager app 
    to download the Uodate file used for offline installs"""

    description = __doc__
    input_variables = {
        "install_manager_path": {
            "required": True,
            "description": "Path to the install manager app.",
        }
    }
    output_variables = {
        "downloaded_update_path": {"description": "Outputs path to the update file."}
    }

    def main(self):
        try:
            downloader_cli = self.env["install_manager_path"] + "/Contents/Resources/cli.sh"
            list_updates_command = [downloader_cli,
                            'download',
                            '--ls']
            self.output("Running command : %s" % list_updates_command)
            process = subprocess.run(
                   list_updates_command,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE,
                   text=True)
            List = process.stdout.strip()

            high_version = "0"
            for line in List.split("\n"):
                if "Update" in line:
                    version = line[10:]
                    if version > high_version:
                        high_version = version

            update_target_version = "Update" + high_version
            self.output("Found update target %s" % update_target_version)

            update_dir = self.env["RECIPE_CACHE_DIR"] + "/Update"
            update_download_command = [downloader_cli,
                        'download',
                        '--target',
                        update_target_version,
                        '--dest',
                        update_dir]
            download_update_path = update_dir + '/' + update_target_version + '.vwim'

            if not os.path.isfile(download_update_path):
                self.output("Running command  %s" % update_download_command)
                process = subprocess.run(
                        update_download_command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)
            else:
                self.output("Update already exists as : %s" % download_update_path)
            self.env["downloaded_update_path"] = download_update_path 

        except Exception as err:
            # handle unexpected errors here
            raise ProcessorError(err)


if __name__ == "__main__":
    PROCESSOR = VectorworksUpdateDownloader()
    PROCESSOR.execute_shell()