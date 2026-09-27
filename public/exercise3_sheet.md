# Cheat cheet for exercise 3

### 1. Install the package directly from GitHub, without cloning
```
python -m pip install "git+https://github.com/amur-bashirov/explaining_git.git"
```
# 2. Verify the installed version
```
python -m pip show package_of_amur
```

# 3. Now install a specific tagged release instead, and check the version again
```
python -m pip install "git+https://github.com/amur-bashirov/explaining_git.git@v0.1.0"
python -m pip show package_of_amur
```