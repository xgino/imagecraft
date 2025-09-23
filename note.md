git tag v0.2.4
git push origin v0.2.4

git add -A
git commit -m "release: v0.2.4"
git push


rm -rf dist build *.egg-info
pip install build twine
python -m build

twine upload dist/*
insert API in CLI