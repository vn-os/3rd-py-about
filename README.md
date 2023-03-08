# 3rd-py-about
About Dialog for Python

### Usage

```
pip install git+https://github.com/vic4key/PyVutils.git
git submodule add --force https://github.com/vn-os/3rd-py-about.git pyabout
pip install -r pyabout/requirements.txt
```

```python
from pyabout import AboutDlg

[...]

AboutDlg(
  self, # 
  name="name",
  year=1991,
  repo="link\to\code\repository"
).exec_()
```
