NAME := "termoshtt/flat_ffi_example"

all: build

login:
	docker login

push: login
	docker push ${NAME}

build:
	docker build . -t ${NAME}

run: build
	docker run -it --rm ${NAME}
