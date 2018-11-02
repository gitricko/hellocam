# hellocam
Hello Cam

### How to setup
conda env create -f environment.yml

### How to run
```ssh
conda activate hellocam
python -m http.server 8080 --cgi
```

open [http://localhost:8080/cgi-bin/nestcam.py](http://localhost:8080/cgi-bin/nestcam.py)
