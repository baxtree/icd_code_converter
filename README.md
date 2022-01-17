# icd_code_converter
Command line interface for converting between ICD-9 codes and ICD-10 codes. It functions as a thin wrapper of [touch.icd_map](https://hub.wwenjie.org/touch/).

# Prerequisites
- The [R language and environment](https://cloud.r-project.org/) has been downloaded and installed.

- Your login user needs to have the permission for installing R libraries. Otherwise, try `sudo usermod -a -G staff $USER`.

# Examples
```
$ ./icd_code_converter --icd9 "401.9"                       # I10,I169
$ ./icd_code_converter --icd10 "I10;I169"                   # 4010,4011,4019;4019
$ ./icd_code_converter --icd9 "401.9=001.1" --delimiter "=" # I10,I169=A001
```

# Usage
```
usage: icd_code_converter [--] [--help] [--icd9 ICD9] [--icd10 ICD10]
       [--delimiter DELIMITER]

Convert between ICD-9 codes and ICD-10 codes

flags:
  -h, --help       show this help message and exit

optional arguments:
  -n, --icd9       single ICD-9 code or semicolon-separated ICD-9 codes
  -t, --icd10      single ICD-10 code or semicolon-separated ICD-10
                   codes
  -d, --delimiter  symbol for separating ICD codes and cannot be ','
                   [default: ;]
```