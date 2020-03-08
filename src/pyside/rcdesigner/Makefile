PYSIDEUIC="O:\\WinProgs\\Anaconda3\\python.exe" "O:\\WinProgs\\Anaconda3\\Library\\bin\\pyside2-uic"
all: 
	@echo "Targets are: testall(aka: alltest) allexamples"

alltest: testall

alltests: testall

testall:
	@echo "Run all tests"
	$(PYTHON) -m unittest discover

allexamples:
	cd examples && make allexamples

updategui: mainwindow.ui
	$(PYSIDEUIC) $< -o ui_mainwindow.py

clean : 
	rm -f ui_mainwindow.py
	rm -rf __pycache__
