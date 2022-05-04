ping:
	sudo apt-update
	sudo apt install -y python3-pip
	pip3 install -U ccxt
	pip3 install pandas
	python3 ./ping_tester.py
	git add .
	git commit -am 'add data'
	git push

