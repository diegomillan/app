## Find Pairs Summing

Tested on Unix based machines, using python 3.9+.

## Prerequesites
 - Install python 3.9 or later
 - Install pip (https://pip.pypa.io/en/latest/installation/)
 - Install virtualenv (https://click.palletsprojects.com/en/8.1.x/quickstart/#virtualenv)
 - ```git clone https://github.com/diegomillan/app.git```

## Build & Requirements
- Create a python virtualenv:
```bash
virtualenv venv
```
- Activate the virtualenv:
```bash
. venv/bin/activate
```
- From the root folder of this repository, execute:
 ```bash
 make requirements
 ```
## Test the app
 From the root folder of this repository, execute:
 ```bash
 make tests
 ```

## Usage
 From the root folder of this repository, execute (it will run over each input line defined in input.txt):
 ```bash
 make run
 ```
 Also, you could run the app passing an existing file as argument (this file must follow the same format as input.txt):
 ```bash
 app <filename.txt>
 ```

 ## Help and Description
 Find a general description and help executing:
 ```bash
 app --help
 ```