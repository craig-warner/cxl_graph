init:
	pip install -r requirements.txt --break-system-packages

test:
#	py.test tests

sample:
	python3 bin/cxl_graph.py --gen_sample

clean:
	rm data/sample/*

.PHONY: init test sample
