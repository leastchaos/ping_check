ping:
	pip install -U ccxt
	pip install pandas
	python3 ./ping_tester.py
	git add .
	git commit -am 'add data'
	git push
	
