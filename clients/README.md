```sh
protoc --fatal_warnings --proto_path=protobuf --python_out=protobuf $(find protobuf/entities -name "*.proto" -print)
protoc --fatal_warnings --proto_path=protobuf --python_out=protobuf $(find protobuf/events -name "*.proto" -print)
```
