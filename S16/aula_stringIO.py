#aula sobre o módulo StringIO

import io

message = "this is anormal string"
f = io.StringIO(message)
print(f.read())
f.seek(0)
f.write("second line written here")
f.seek(0)
print(f.read())

