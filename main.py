import pandas as pd

def turn(csv_file, target_file):
	en = pd.read_csv(csv_file).product_title.dropna()
	en = en.str.replace('\n', ' ')
	en = en.str.replace('\r', ' ')
	en = en.str.strip()

	with open(target_file, 'w', encoding='utf-8') as f:
		f.writelines('\n'.join(en.to_list()))

turn('test_tcn.csv', 'test.cn')