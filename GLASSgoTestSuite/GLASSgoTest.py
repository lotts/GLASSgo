#!/usr/bin/python3

import argparse
import os
import sys

"""
GLASSgoTest.py Version 0.1.0

MIT License
Copyright (c) 2017
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#export PERL5LIB=/Users/steffen/Developing/Python/GLASSgo/GITHUB/Bionfo_Galaxy_Version/GLASSgo/reqPackages:$PERL5LIB

if __name__ == "__main__":
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    scriptPathGLASSgo = os.path.abspath(os.path.join(__file__, "../.."))

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--glassgoFile", help="Path to GLASSgo.py", type=str, default=str(scriptPathGLASSgo) + "/GLASSgo.py")
    parser.add_argument("-i", "--inputFile", help="Path to test input FASTA file", type=str, default=str(scriptPath) + "/data/input/test.fasta")
    parser.add_argument("-d", "--dbFile", help="Path to test DB", type=str, default=str(scriptPath) + "/data/db/test.fasta")
    parser.add_argument("-t", "--testMD5", help="Path to MD5 Files", type=str, default=str(scriptPath) + "/data/precomputed/")
    args = parser.parse_args()

    # 1. Test -> Call "GLASSgo.py -h"
    value = os.system(str(args.glassgoFile) + " -h > /dev/null ")
    if value == 0:
        sys.stderr.write("==> TEST-1-PASSED: GLASSgo.py -h is executable.\n")
    else:
        sys.stderr.write("==> TEST-1-ERROR: GLASSgo.py does not work! Please check file path as well as permissions (chmod +x GLASSgo.py)!\n")

    # 2. Test -> Call "GLASSgo.py" using standard settings
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -o defaultSettings")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings.md5 > /dev/nul")
    if value == 0:
        sys.stderr.write("==> TEST-2-PASSED: GLASSgo.py run with default parameters\n")
    else:
        sys.stderr.write("==> TEST-2-ERROR: GLASSgo.py run with default parameters failed. MD5SUM differs! (./data/precomputed/defaultSettings.md5)\n")
    os.system("rm defaultSettings")

    # 3. Test -> Call "GLASSgo.py" without Londen (-l 0)
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -l 0 -o withoutLonden")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings_LondenOFF.md5 > /dev/null")
    if value == 0:
        sys.stderr.write("==> TEST-3-PASSED: GLASSgo.py run without Londen\n")
    else:
        sys.stderr.write("==> TEST-3-ERROR: GLASSgo.py run without Londen failed. MD5SUM differs! (./data/precomputed/defaultSettings_LondenOFF.md5)\n")
    os.system("rm withoutLonden")

    # 4. Test -> Call "GLASSgo.py" with single cut method (-l 1)
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -l 1 -o londenSingleCut")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings_LondenSingleCut.md5 > /dev/null")
    if value == 0:
        sys.stderr.write("==> TEST-4-PASSED: GLASSgo.py run with Londen Single Cut method (-l 1)\n")
    else:
        sys.stderr.write("==> TEST-4-ERROR: GLASSgo.py run with Londen Single Cut method failed. MD5SUM differs! (./data/precomputed/defaultSettings_LondenSingleCut.md5)\n")
    os.system("rm londenSingleCut")

    # 5. Test -> Call "GLASSgo.py" default settings with upstream region (-u 100)
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -u 100 -o upstreamRegion")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings_upstream.md5 > /dev/null")
    if value == 0:
        sys.stderr.write("==> TEST-5-PASSED: GLASSgo.py run with default settings + extracting upstream region of 100 nucleotides (-u 100)\n")
    else:
        sys.stderr.write("==> TEST-5-ERROR: GLASSgo.py run with default settings + extracting upstream region of 100 nucleotides failed. MD5SUM differs! (./data/precomputed/defaultSettings_upstream.md5)\n")
    os.system("rm upstreamRegion")

    # 6. Test -> Call "GLASSgo.py" default settings with modified area filter (-a 0.1)
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -a 0.1 -o areaFilter")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings_areaFilter.md5 > /dev/null")
    if value == 0:
        sys.stderr.write("==> TEST-6-PASSED: GLASSgo.py run with default settings + modified area filter (-a 0.1)\n")
    else:
        sys.stderr.write("==> TEST-6-ERROR: GLASSgo.py run with default settings + modified area filter failed. MD5SUM differs! (./data/precomputed/defaultSettings_areaFilter.md5)\n")
    os.system("rm areaFilter")

    # 7. Test -> Call "GLASSgo.py" default settings with modified E-Value (-e 0.000001)
    os.system(str(args.glassgoFile) + " -i " + str(args.inputFile) + " -d " + str(args.dbFile) + " -e 0.000001 -o eValue")
    value = os.system("md5sum -c " + str(args.testMD5) + "defaultSettings_eValue.md5 > /dev/null")
    if value == 0:
        sys.stderr.write("==> TEST-7-PASSED: GLASSgo.py run with default settings + modified E-Value (-e 0.000001)\n")
    else:
        sys.stderr.write("==> TEST-7-ERROR: GLASSgo.py run with default settings + modified E-Value failed. MD5SUM differs! (./data/precomputed/defaultSettings_eValue.md5)\n")
    os.system("rm eValue")