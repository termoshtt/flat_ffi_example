
flat_example.so:
	cmake -Bbuild -H.
	make -C build
	mv build/flat_example.so .

test: flat_example.so
	./test.py
