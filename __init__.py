import os, sys
import PyVutils as vu

from PyQt5 import uic as UiLoader
from PyQt5.QtWidgets import QDialog

def _get_current_directory():
	result = ""
	try: result = sys._MEIPASS
	except: result = os.path.dirname(os.path.realpath(__file__))
	return vu.normalize_path(result)

def _get_resource_file_path(file_name: str):
	result = os.path.join(_get_current_directory(), os.path.join("resources", file_name))
	return result

# auto compile resources .qrc
import pyqt5ac
resources_qrc = _get_resource_file_path("resources.qrc")
resources_py  = _get_resource_file_path("resources.py")
pyqt5ac.main(initPackage=False, force=False, ioPaths=[[resources_qrc, resources_py]])
import resources # import to load resource data

class AboutDlg(QDialog):
	'''About Dialog
	'''

	m_name: str
	m_year: str
	m_repo: str
	m_auth: str
	m_site: str

	def __init__(self, name: str, year: str, repo: str, author:  str = "Vic P.", website: str = "https://vic.onl/"):
		super(AboutDlg, self).__init__()
		self.m_name = name
		self.m_year = str(year)
		self.m_repo = repo
		self.m_auth = author
		self.m_site = website
		self.setup_ui()

	def setup_ui(self):
		about_ui = _get_resource_file_path("about.ui")
		UiLoader.loadUi(about_ui, self)
		self.buttonBox.clicked.connect(lambda: self.close())

		# name
		self.label_name.setText(self.m_name)

		# repository
		text = self.label_repository.text()
		text = text % self.m_repo
		self.label_repository.setText(text)

		# website
		text = self.label_website.text()
		text = text % self.m_repo
		self.label_website.setText(text)

		# copyright
		text = self.label_copyright.text()
		text = text % (self.m_auth, self.m_year)
		self.label_copyright.setText(text)
