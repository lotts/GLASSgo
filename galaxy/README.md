# Configuration of Galaxy to run GLASSgo in Docker 

## Prerequisites

1.	configure Galaxy to run tools in Docker as described at https://galaxyproject.org/admin/tools/docker/.

	In addition, GLASSgo requires the current BLAST nucleotide database. For that, the `tool-data/blastdb.loc` has to be configured accordingly as the GLASSgo wrapper reads this information as options when laying out the user interface. We use Docker volumes to do so (Docker CLI option -v). 
	For that, we add Docker volumes to the (id=`docker_local`) Docker destination 
	```
	<param id="docker_volumes">$defaults,/Volumes/TC1/nt:/Volumes/TC1/nt/</param>
    ```
    More information can be found in the [./config/job_conf.xml.sample_advanced](https://github.com/galaxyproject/galaxy/blob/release_18.09/config/job_conf.xml.sample_advanced#L378) of any Galaxy instance. Obviously, the exposed folder needs to be identical with the path specified in `tool-data/blastdb.loc`. Here the local folder `Volumes/TC1/nt` contains the BLAST database and is exposed to the Docker container. In this case, the folder is bound to the same location in the container. This allows to execute the GLASSgo call in the tool XML file directly with the selected option.

2.	Install GLASSgo from the [Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/view/computationaltranscriptomics/glassgo). Afterwards, the Galaxy instance
	needs to be configured such that it is aware of the accession lists. This can be done either manually or using a custom script.
	*	download the accession lists from Zenodo (https://zenodo.org/record/1320180) and copy the file 
	[`glassgo_accession_list.txt`](./tool-data/glassgo_accession_list.txt) into the folder `tool-data` of Galaxy (e.g., `/galaxy/tool-data/`) or
	*	use [`config_lookup`](./config_lookup/dist/) to download the look tables using [`accession_lists_links.txt`](./accession_lists_links.txt) 
	(option --acclinks) and creates `glassgo_accession_list.txt` in `tool-data` of Galaxy. 

	Note: Any changes of files within `tool-data` requires a (re)start of Galaxy.

## config_lookup
```
usage: config_lookup [-h] --galaxy GALAXY --acclinks ACCLINKS [--acclists ACCLISTS]

incorporate the accession lists in GLASSgo/Galaxy to enable clade-specific searches

optional arguments:
  -h, --help           show this help message and exit
  --galaxy GALAXY      (absolute) path to the root directory of the Galaxy instance
  --acclinks ACCLINKS  (absolute) path to file containing URLs to the accession lists
  --acclists ACCLISTS  (absolute) path to directory to save the accession lists to
```



