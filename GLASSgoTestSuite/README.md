# GLASSgoTest.py

** Applied Tests:**
- Check if GLASSgo.py -h is executable
- Check if GLASSgo.py works with default parameters (GLASSgo.py -i <INPUT> -d <DB>)
- Check if GLASSgo.py works with deactivated Londen analysis (GLASSgo.py -i <INPUT> -d <DB> -l 0)
- Check if GLASSgo.py works with Londen in single-cut mode (GLASSgo.py -i <INPUT> -d <DB> -l 1)
- Check if GLASSgo.py extracts 100 nt from UTR-region  (GLASSgo.py -i <INPUT> -d <DB> -u 100)
- Check if GLASSgo.py works with fixed area-filter  (GLASSgo.py -i <INPUT> -d <DB> -a 0.1)
- Check if GLASSgo.py works with different E-Values - default=1  (GLASSgo.py -i <INPUT> -d <DB> -e 0.000001)

**Usage:**
```text
python3 GLASSgoTest.py
```

GLASSgo on DockerHub
-------
https://hub.docker.com/r/lotts/glassgo_acc_version
