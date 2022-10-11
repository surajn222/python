build:
	-pip3 install --upgrade pip
	-pip3 install -r requirements.txt
	-python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto