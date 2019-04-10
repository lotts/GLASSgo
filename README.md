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
-i input_file (single sRNA sequence in FASTA format)
-o output_file (optional, default: stdout)
-e E-Value (default: 1)
-p lower limit for pairwise identity (default: 52)
-g ACC-List (optional), (default: global search)
-d NCBI nt-database
-t number of threads for performing the BLAST search (default: 1)
-u upstream region (default: 0)
```


ACC-Lists on Zenodo
-------
https://zenodo.org/record/1320180

GLASSgo on DockerHub
-------
https://cloud.docker.com/u/lotts/repository/docker/lotts/glassgo_acc_version

GLASSgo Web-Server Version + interactive taxonomic tree viewer
-------
http://rna.informatik.uni-freiburg.de/GLASSgo/
