#!/usr/local/autopkg/python
#
# TextSearcher code extracted by Anthony Reimer from URLTextSearcher:
# Refactored 2018 Michal Moravec
# Copyright 2015 Greg Neagle
# Based on URLTextSearcher.py, Copyright 2014 Jesse Peterson
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
"""See docstring for TextSearcher class"""

import re

from autopkglib import Processor, ProcessorError

MATCH_MESSAGE = "Found matching text"
NO_MATCH_MESSAGE = "No match found in passed text"

__all__ = ["TextSearcher"]


class TextSearcher(Processor):
    """Performs a regular expression match on the text passed via the text_in
    input variable.

    Requires version 1.4."""

    input_variables = {
        "re_pattern": {
            "description": "Regular expression (Python) to match against the text (text_in).",
            "required": True,
        },
        "text_in": {"description": "Text to be searched", "required": True},
        "result_output_var_name": {
            "description": (
                "The name of the output variable that is returned "
                "by the match. If not specified then a default of "
                '"match" will be used.'
            ),
            "required": False,
            "default": "match",
        },
        "re_flags": {
            "description": (
                "Optional array of strings of Python regular "
                "expression flags. e.g., IGNORECASE."
            ),
            "required": False,
        },
    }
    output_variables = {
        "result_output_var_name": {
            "description": (
                "First matched sub-pattern found in the supplied text. "
                "Note the actual name of variable depends on the input "
                'variable "result_output_var_name" or is assigned a default of '
                '"match."'
            )
        }
    }

    description = __doc__

    def prepare_re_flags(self):
        """Create flag varible for re.compile"""
        flag_accumulator = 0
        for flag in self.env.get("re_flags", {}):
            if flag in re.__dict__:
                flag_accumulator += re.__dict__[flag]
        return flag_accumulator

    def re_search(self, content):
        """Search for re_pattern in content"""

        re_pattern = re.compile(self.env["re_pattern"], flags=self.prepare_re_flags())
        match = re_pattern.search(content)

        if not match:
            raise ProcessorError(f"{NO_MATCH_MESSAGE}: {content}")

        # return the last matched group with the dict of named groups
        return (match.group(match.lastindex or 0), match.groupdict())

    def main(self):
        output_var_name = self.env["result_output_var_name"]

        # Load text to search into content
        content = self.env["text_in"]
        groupmatch, groupdict = self.re_search(content)

        # favor a named group over a normal group match
        if output_var_name not in groupdict.keys():
            groupdict[output_var_name] = groupmatch

        self.output_variables = {}
        for key in groupdict.keys():
            self.env[key] = groupdict[key]
            self.output(f"{MATCH_MESSAGE} ({key}): {self.env[key]}")
            self.output_variables[key] = {
                "description": "Matched regular expression group"
            }


if __name__ == "__main__":
    PROCESSOR = TextSearcher()
    PROCESSOR.execute_shell()
