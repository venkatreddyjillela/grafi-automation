pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/test_login.py --browser chrome
@REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
@REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox