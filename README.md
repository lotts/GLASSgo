# GLASSgo_ACC-Version
GLASSgo (GLobal Automated sRNA Search go) combines iterative BLAST searches, pairwise identity filtering, and structure based clustering in an automated prediction pipeline to find sRNA homologs from scratch. The returned GLASSgo result is in FASTA format, whereby the first entry represents the input sequence. 

The current GLASSgo version uses a compiled version of Londen (/reqPackages/londen). If you want to use the sources, please modify line 524 in the GLASSgo.py script. 

**Required packages:**
- Python version >3.x
- Perl version >5.x
- Clustal Omega (http://www.clustal.org/omega/)
- Biopython
- Python3 'numpy' package
- Bioperl
- RNApdist (https://www.tbi.univie.ac.at/RNA/RNApdist.1.html)
- BLAST+ version >2.7 (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
- NCBI 'nt' database (ftp://ftp.ncbi.nlm.nih.gov/blast/db/)

**Usage:**
```text
python3 GLASSgo.py -d <path to NCBI nt database> -i <sRNA input in FASTA format> -o <output filename>
```

**Most important GLASSgo parameters:**
```text
-i    input_file (single sRNA sequence in FASTA format)
-o    output_file (optional, default: stdout)
-e    E-Value (default: 1)
-p    lower limit for pairwise identity (default: 52)
-g    path to ACC-List (optional)  (default: global search)
-d    path to NCBI nt-database
-t    number of threads for performing the BLAST search (default: 1)
-u    upstream region (default: 0)
```

We provide a video that guides through the setup & usage of GLASSgo.

Schäfer, R.A, Lott, S.C. et. al (2020) "GLASSgo Setup & Usage", https://doi.org/10.18419/darus-517, DaRUS, V1

ACC-Lists on Zenodo
-------
https://zenodo.org/record/1320180

GLASSgo on DockerHub
-------
https://hub.docker.com/r/lotts/glassgo_acc_version

GLASSgo Web-Server Version + interactive taxonomic tree viewer
-------
http://rna.informatik.uni-freiburg.de/GLASSgo/

GLASSgo on the RNA Workbench Server
-----------------------------------
[https://rna.usegalaxy.eu/](https://rna.usegalaxy.eu/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fcomputationaltranscriptomics%2Fglassgo%2Fglassgo%2F1.5.2)

GLASSgo within Galaxy
-------
https://github.com/lotts/GLASSgo_ACC-Version/tree/master/galaxy
