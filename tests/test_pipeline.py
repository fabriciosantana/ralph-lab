import csv
from pathlib import Path
ROOT = Path(__file__).parents[1]
def test_join_exists(): assert (ROOT/'vendas_lojas.csv').exists()
def test_join_shape_and_sum():
    rows = list(csv.DictReader((ROOT/'vendas_lojas.csv').open()))
    assert len(rows) == 420
    assert abs(sum(float(r['receita_brl']) for r in rows)-931274.06) < .5
def test_pivot_header():
    with (ROOT/'pivot_receita.csv').open() as f: assert next(csv.reader(f)) == ['regiao','2026-01','2026-02','2026-03','2026-04','2026-05','2026-06']
def test_pivot_total():
    rows=list(csv.reader((ROOT/'pivot_receita.csv').open()))[1:]
    assert abs(sum(float(x) for r in rows for x in r[1:])-931274.06) < .5
