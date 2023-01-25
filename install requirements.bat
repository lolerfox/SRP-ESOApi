echo off
CHCP 1251
cls
echo Expect :) It may take some time...

python -m pip install --upgrade pip
python -m pip install -r src/config/requirements.txt
pause