# GLASSgo Docker Integration within Galaxy
## Setup

We (more or less) followed the tutorial on how to work with Galaxy and Docker, 
found [here](https://github.com/apetkau/galaxy-hackathon-2014).

Initially, the GLASSgo Docker images needs to be made available on the system.
```
docker pull lotts/glassgo_acc_version
```

In particular, the integration of the GLASSgo Docker container within Galaxy requires:
1.	the GLASSgo tool XML file 
	
	We have deployed the GLASSgo XML wrapper in the (Galaxy Toolshed)[https://toolshed.g2.bx.psu.edu/view/computationaltranscriptomics/glassgo], for it to be installed in any Galaxy instance with admin access.
	
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
    More information can be found in the (./config/job_conf.xml.sample_advanced)[https://github.com/galaxyproject/galaxy/blob/release_18.09/config/job_conf.xml.sample_advanced#L378] of any Galaxy instance. Obviously, the exposed folder needs to be identical with the path specified in `tool-data/blastdb.loc`. Here the local folder `Volumes/TC1/nt` contains the BLAST database and is exposed to the Docker container. In this case, the folder is bound to the same location in the container. This allows to execute the GLASSgo call in the tool XML file directly with the selected option. 



