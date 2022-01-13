# icd_code_converter
Command line interface for converting between ICD-9 codes and ICD-10 codes.

# Prerequisites
- The [R language and environment](https://cloud.r-project.org/) has been downloaded and installed.

- Your login user needs to have the permission for installing R libraries. Otherwise, try `sudo usermod -a -G staff $USER`.

# Usage
```
usage: icd_code_converter [--] [--help] [--icd9 ICD9] [--icd10 ICD10]

Convert between ICD-9 codes and ICD-10 codes

flags:
  -h, --help   show this help message and exit

optional arguments:
  -n, --icd9   The ICD-9 code
  -t, --icd10  The ICD-10 code
```