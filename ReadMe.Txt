# Environment: Python 3.4 +, pytest
# Coding Standard PEP8

# Files included are
1. Main.py - Runs the entire application
2. Login.py - Login module
3. Transaction_mgt.py - Transactions module
4. Settings.py - Settings data dictionary acting as cache db
5. Start.py - Menu's control
6. Test.py - PyTest unit testing on the application

# How to run from commandline

python ../saved_folder/TalaAtm/src/main.py

# Tests

pytest ../saved_folder/TalaAtm/src/tests.py

# coverage

pytest --cov=test.py .



