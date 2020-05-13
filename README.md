# GLASSgo
GLASSgo (GLobal Automated sRNA Search go) combines iterative BLAST searches, pairwise identity filtering, and structure based clustering in an automated prediction pipeline to find sRNA homologs from scratch. The returned GLASSgo result is in FASTA format, whereby the first entry represents the input sequence. 
Please cite us if your are using GLASSgo for your work (https://doi.org/10.3389/fgene.2018.00124).


**Required packages:**
- Python version >3.x
- Perl version >5.x
- Clustal Omega (http://www.clustal.org/omega/) version 1.2.4
- Biopython version 1.76
- Python3 'numpy' package version 1.17.4
- Bioperl version 1.7.2
- RNApdist (https://www.tbi.univie.ac.at/RNA/RNApdist.1.html)(viennarna version 2.4.14)
- BLAST+ version 2.8.1 (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
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
https://hub.docker.com/repository/docker/lotts/glassgo

GLASSgo Web-Server Version + interactive taxonomic tree viewer
-------
http://rna.informatik.uni-freiburg.de/GLASSgo/

GLASSgo on the RNA Workbench Server
-----------------------------------
[https://rna.usegalaxy.eu/](https://rna.usegalaxy.eu/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fcomputationaltranscriptomics%2Fglassgo%2Fglassgo%2F1.5.2)

GLASSgo within Galaxy
-------
https://github.com/lotts/GLASSgo/tree/master/galaxy
