default:
	make deps
	make build
	make run

deps:
	pip install prettytable

build:
	python -m compileall .

run:
	python task_1/line_algorytms.py
	python task_2/triangle.py
	python task_3/a_branching.py
	python task_3/b_branching.py
	python task_4/choise.py
	python task_5/loop_measures.py
	python task_6/the_sum_and_the_product.py
	python task_7/endless_sum.py
	python task_8/loop_data_search.py
	python task_9/one_dimencional_arrs.py
	python task_10/arrs_hard_data_search.py

clean:
	rd /s /q task_1\__pycache__
	rd /s /q task_2\__pycache__
	rd /s /q task_3\__pycache__
	rd /s /q task_4\__pycache__
	rd /s /q task_5\__pycache__
	rd /s /q task_6\__pycache__
	rd /s /q task_7\__pycache__
	rd /s /q task_8\__pycache__
	rd /s /q task_9\__pycache__
	rd /s /q task_10\__pycache__

install:
	set path=%path%;"@task1";"@task2";"@task3";"@task4";"@task5";"@task6";"@task7";"@task8";"@task9";"@task_10";
