```sh
cd ${workspaceRoot}/clients
protoc --fatal_warnings --proto_path=. --python_out=. $(find . -name "*.proto" -print)
```
