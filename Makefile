init:
	pip install -r requirements.txt --break-system-packages

test:
	./bin/cxl_graph.py --analyze_graph --ifile data/finance/finance256.gml --verbose > log

sample:
	./bin/cxl_graph.py --gen_sample

clean:
	rm data/sample/*

.PHONY: init test sample
