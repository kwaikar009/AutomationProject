pytest -v -s -m "sanity" --html=./Reports/sanityreport.html testCases/ --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/sanityreport.html testCases/ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/sanityreport.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/sanityreport.html testCases/ --browser chrome