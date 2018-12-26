import yaml

dict2yaml = dict(list = [1,2,3],
                 int =4,
                 dict = {'а': 1,'б':2})

print(dict2yaml)

with open('test.yaml', 'w') as f_n:
    yaml.dump(dict2yaml, f_n, default_flow_style=False,allow_unicode=True)


with open('test.yaml', 'r') as f_n:
    f_n_cont = yaml.load(f_n)
    print(f_n_cont)
