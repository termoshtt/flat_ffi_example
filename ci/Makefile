NAME := "termoshtt/flat_ffi_example"

all: build

login:
	docker login

build:
	docker build . -t ${NAME}

run: build
	docker run -it --rm ${NAME}

push: login build
	docker push ${NAME}

