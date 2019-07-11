NAME := "termoshtt/flat_ffi_example"

all: build

login:
	docker login

build:
	docker build . -t ${NAME}

push: login
	docker push ${NAME}
