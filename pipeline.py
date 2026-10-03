import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
DATA = Path('/workspaces/mcdia-idp-agentes-ia/exercicios/aula3/data')

def build():
    lojas = {}
    with (DATA / 'lojas.csv').open(newline='') as f:
        for row in csv.DictReader(f): lojas[row['id_loja']] = row
    joined = []
    with (DATA / 'vendas.csv').open(newline='') as f:
        for row in csv.DictReader(f):
            loja = lojas.get(row['id_loja'])
            if loja is not None:
                joined.append({**row, **{k:v for k,v in loja.items() if k != 'id_loja'}})
    with (ROOT / 'vendas_lojas.csv').open('w', newline='') as f:
        fields = list(joined[0]); w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(joined)
    sums = defaultdict(float)
    for row in joined: sums[(row['regiao'], row['data'][:7])] += float(row['receita_brl'])
    months = [f'2026-{i:02d}' for i in range(1,7)]
    regions = sorted({r for r,_ in sums})
    with (ROOT / 'pivot_receita.csv').open('w', newline='') as f:
        w = csv.writer(f); w.writerow(['regiao', *months])
        for region in regions: w.writerow([region, *[f'{sums[(region,m)]:.2f}' for m in months]])

if __name__ == '__main__': build()
