## How to set up DVC on local system for Python project with code repo as github and data storage as GCS

## Download DVC on MAC OS
- Goto DCV official website (https://dvc.org/) and download DVC package. Install the executables on the local system. One can follow the same steps to install DVC for other operating system.
- Verify instlled DVC version
```bash
$ dvc --version
```

### Step 1:
**Create a python virtual environment**
``` bash
$ conda create -n dvc python=3.6 anaconda
```
**Activate python virtual environment**
``` bash
$ source activate dvc
```

### Step 2: 
**Install the required python dependencies**
```bash
$ pip install -r requirements.txt
```
**Install DVC Python packages for remote storage as GCS**
```bash
$ pip install 'dvc[gs]'
```

### Step 3:
**Project set-up**
Create 2 folders, paste code and data:
1. For code
2. For data
3. For model

### Step 4:
Clone the code from Github

### Step 5:
**Initialize DVC**
```bash
$ dvc init
$ ls -a .dvc
$ git status -s
$ cat .dvc/.gitignore
$ git commit -m 'init DVC'
$ git push
```

### Step 6: Create a bucket and integrate with DVC
**Create bucket on GCS**
gs://dvc-data-versioning
**Setup DVC remote**
```bash
$ dvc remote add -d myremote gs://dvc-data-versioning
```
**Set up crendentials**
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="/Users/ravranja6/ravi/CoE/Spotlight Sessions/DVC/tf_credentials_dev.json"
```

### Step 7: Add version 1 data to DVC cache
```bash
$ dvc add data
```

### Step 8: Train ML model for version 1 data
```bash
$ python code/train_log_reg.py
```
### Step 9: Add version 1 model to DVC cache
```bash
$ dvc add model
```


### Step 10: Push version 1 code to git
```bash
$ git add .gitignore data.dvc model.dvc .dvc/config README.md code/ requirements.txt
$ git commit -m "model version 1.0, gcp storage"
$ git tag -a "v1.0" -m "model v1.0, full data"
$ git push origin HEAD:master
```

### Step 11: Push version 1 data to storage
```bash
$ dvc push
```

### Step 12: Add version 2 data to DVC cache
```bash
$ dvc add data
```

### Step 13: Train ML model for version 2 data
```bash
$ python code/train_log_reg.py
```
### Step 14: Add version 2 model to DVC cache
```bash
$ dvc add model
```


### Step 15: Push version 2 code to git
```bash
$ git add .gitignore data.dvc model.dvc .dvc/config README.md code/ requirements.txt
$ git commit -m "model version 2.0, gcp storage"
$ git tag -a "v2.0" -m "model v2.0, 1000 data"
$ git push origin HEAD:master
```

### Step 16: Push version 1 data to storage
```bash
$ dvc push
```

### Step 17: Check out version 1 code and data from git 
```bash
$ git checkout v1.0
$ dvc checkout data.dvc
$ dvc checkout model.dvc
```

### Step 18: Check out version 2 code and data from git 
```bash
$ git checkout v2.0
$ dvc checkout data.dvc
$ dvc checkout model.dvc
```


