#!/usr/bin/env python
"""

Copyright (c) 2017, Konrad Foerstner <konrad@foerstner.org>

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted, provided that the
above copyright notice and this permission notice appear in all
copies.

THE SOFTWARE IS PROVIDED 'AS IS' AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
         
"""
__description__ = ""
__author__ = "Konrad Foerstner <konrad@foerstner.org>"
__copyright__ = "2017 by Konrad Foerstner <konrad@foerstner.org>"
__license__ = "ISC license"
__email__ = "konrad@foerstner.org"
__version__ = ""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__description__)
    subparsers = parser.add_subparsers(help="commands")
    
    compile_data_parser = subparsers.add_parser(
        "compile_data", help="Compile the data")
    compile_data_parser.add_argument("--episode_url", "-u", required=True)
    compile_data_parser.add_argument(
        "--output_folder", "-o", required=True)
    compile_data_parser.set_defaults(runner_class=OSRDataCompiler)
    
    upload_parser = subparsers.add_parser("upload", help="Upload data")
    upload_parser.add_argument("--input_folder", "-i", required=True)
    upload_parser.set_defaults(runner_class=OSRZenodoUploader)
    args = parser.parse_args()
    try:
        runner = args.runner_class(args)
        runner.run()
    except:
        parser.print_help()


class OSRDataCompiler(object):

    def __init__(self, args):
        pass

    def run(self):
        pass


class OSRZenodoUploader(object):

    def __init__(self, args):
        pass

    def run(self):
        pass


main()
