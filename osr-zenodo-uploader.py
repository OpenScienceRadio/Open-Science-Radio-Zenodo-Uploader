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
import os
import sys
import requests
from bs4 import BeautifulSoup
import wget


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

    if "runner_class" not in args:
        parser.print_help()
        sys.exit(0)
    runner = args.runner_class(args)
    runner.run()


class OSRDataCompiler(object):

    def __init__(self, args):
        self._episode_url = args.episode_url
        self._output_folder = args.output_folder
        self._meta_data = {}
        self._audio_file_urls = []

    def run(self):
        self._create_dir()
        self._extract_meta_data_from_html()
        self._download_audio_files()
        
    def _create_dir(self):
        try:
            os.mkdir(self._output_folder)
        except:
            sys.stderr.write("Warning. Folder '{}' already existed.\n".format(
                self._output_folder))

    def _extract_meta_data_from_html(self):
        response = requests.get(self._episode_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response.text)
        self._meta_data = {"title": soup.title.string}
        for meta_tag in soup.find_all('meta'):
            property = meta_tag.get("property")
            content = meta_tag.get("content")
            if property == "og:title":
                self._meta_data = {
                    "title": "Open Science Radio - {}".format(content)}
            elif property == "og:description":
                self._meta_data = {
                    "description": content}
            elif property == "og:audio":
                self._audio_file_urls.append(content)

    def _download_audio_files(self):
        for audio_file_url in self._audio_file_urls:
            sys.stdout.write("Downloading {}\n".format(audio_file_url))
            wget.download(audio_file_url, out=self._output_folder)


class OSRZenodoUploader(object):

    def __init__(self, args):
        pass

    def run(self):
        pass


main()
