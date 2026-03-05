import dis

code = "print('hello')"
compiled_code = compile(code,'<string>','exec')
dis.dis(compiled_code)