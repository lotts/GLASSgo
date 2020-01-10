# GLASSgo Docker Integration within Galaxy
## Prerequisites

We (more or less) followed the tutorial on how to work with Galaxy and Docker, 
found [here](https://github.com/apetkau/galaxy-hackathon-2014).

Initially, the GLASSgo Docker images needs to be made available on the system.
```
docker pull lotts/glassgo_acc_version
```

In particular, the integration of the GLASSgo Docker container within Galaxy requires:
1.	the GLASSgo tool XML file 
	
	We have deployed the GLASSgo XML wrapper in the [Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/view/computationaltranscriptomics/glassgo), 
	for it to be installed in any Galaxy instance with admin access. Afterwards, the Galaxy instance needs to be configured such that it is aware of the accession lists. This can be done either manually or with the custom script [`config_acclists`](./config_acclists). 
 
2. (modified) `job_conf.xml` to instruct Galaxy to run tools using Docker

	At first, create a basic `job_conf.xml` can be constructed with the following command
	```
	cp config/job_conf.xml.sample_basic config/job_conf.xml
	```
	that is made available using the corresponding entry in `./config/galaxy.yml`
	```
	job_config_file: config/job_conf.xml
	```
	The Docker destination needs to be added to `config/job_conf.xml`:
	```
	<destinations default="docker_local">
       <destination id="local" runner="local"/>
       <destination id="docker_local" runner="local">
         <param id="docker_enabled">true</param>
       </destination>
    </destinations>
	```
	In addition, GLASSgo requires the current BLAST nucleotide database. For that, the `tool-data/blastdb.loc` has to be configured accordingly as the GLASSgo wrapper reads this information as options when laying out the user interface. As the container needs to be aware of the BLAST database, we use Docker volumes to do so (Docker CLI option -v). For that, we add Docker volumes to the (id=`docker_local`) Docker destination 
	```
	<param id="docker_volumes">$defaults,/Volumes/TC1/nt:/Volumes/TC1/nt/</param>
    ```
    More information can be found in the [./config/job_conf.xml.sample_advanced](https://github.com/galaxyproject/galaxy/blob/release_18.09/config/job_conf.xml.sample_advanced#L378) of any Galaxy instance. Obviously, the exposed folder needs to be identical with the path specified in `tool-data/blastdb.loc`. Here the local folder `Volumes/TC1/nt` contains the BLAST database and is exposed to the Docker container. In this case, the folder is bound to the same location in the container. This allows to execute the GLASSgo call in the tool XML file directly with the selected option. 

## Lookup Tables

GLASSgo 1.5.2 now supports the use of accession numbers as unique identifiers. This adaptation also makes it necessary to create new lookup tables for the 
taxonomic classification. This is a prerequisite for clade-specific searches that are often more powerful than untargeted analyses. To ensure easy updating 
and retrieval for existing and new installations, these lookup tables are stored in an open access repository (Zenodo: https://zenodo.org/record/1320180). 

However, the user interface of the Galaxy integration follows the design of the GLASSgo webserver to ease the transfer to the new environment. As a 
consequence the lookup tables need to be integrated into Galaxy. This can be done manually or using a custom script. 

### Manual
`accession_lists_links.txt` contains the URLs (in rows) to the lookup tables that need to be stored in the filesystem. Afterwards, 
the `glassgo_accession_list.txt` that is located in `./tool-data/` needs to be copied into the `tool-data` directory of the Galaxy 
instance (e.g., `/galaxy/tool-data`). It contains the name-value pairs that populate the GLASSgo interface. In particular, the 
name (that appears in the interface) needs to be tab-separated from the value (path of the lookup table). 
```
global	global	# special entry to consider a global search
Alphaproteobacteria	/data/db/databases/glassgo/Alphaproteobacteria.acc
Aquificae	/data/db/databases/glassgo/Aquificae.acc
Archaea	/data/db/databases/glassgo/Archaea.acc
...

```
### Script
We provide the `config_lookup` as a one-file bundled executable script (`./config_lookup/dist/`) that downloads the lookup tables, creates the 
`glassgo_accession_list.txt` and integrates the file into the `tool-data` directory of the Galaxy instance. 
```
usage: config_lookup [-h] --galaxy GALAXY --acclinks ACCLINKS
                     [--acclists ACCLISTS]

incorporate the accession lists in GLASSgo/Galaxy to enable clade-specific searches

optional arguments:
  -h, --help           show this help message and exit
  --galaxy GALAXY      (absolute) path to the root directory of the Galaxy
                       instance
  --acclinks ACCLINKS  (absolute) path to file containing URLs to the
                       accession lists
  --acclists ACCLISTS  (absolute) path to directory to save the accession
                       lists to
```

It is important to note, that these changes require a (re)start of Galaxy. 





