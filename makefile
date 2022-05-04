ping:
	pip3 install -U ccxt
	pip3 install pandas
	python3 ./ping_tester.py
	git add .
	git commit -am 'add data'
	git push

