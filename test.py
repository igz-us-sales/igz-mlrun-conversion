import sys

def handler(context):
    sys.path.append("/src/src_code")
    import mymodule

    name = context.get_param("name")
    print(f'Hello from test.py, {name}!')