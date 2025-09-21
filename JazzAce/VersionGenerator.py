#!/usr/local/autopkg/python
#
# Copyright 2021 Anthony Reimer
# leveraging SampleSharedProcessor by Tim Sutton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for VersionGenerator class"""

from datetime import datetime, timezone

from autopkglib import Processor, ProcessorError

__all__ = ["VersionGenerator"]


class VersionGenerator(Processor):
    """Generates a string that is the number of seconds after 2021-05-21 23:00 UTC.
    This can be used to create an ever-incrementing version number for pkgs/scripts
    that do not have built-in (or meaningful) versioning."""

    description = __doc__
    input_variables = {}
    output_variables = {
        "version": {
            "description": "Outputs an number (as a string) based on the current time in seconds."
        }
    }

    def main(self):
        try:
            self.env["version"] = str(
                int(datetime.now(timezone.utc).timestamp()) - 1621638000
            )
        except Exception as err:
            # handle unexpected errors here
            raise ProcessorError(err)


if __name__ == "__main__":
    PROCESSOR = VersionGenerator()
    PROCESSOR.execute_shell()
