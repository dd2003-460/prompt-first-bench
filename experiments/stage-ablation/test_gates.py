import unittest
from gates import analyze, apply

class GatesTest(unittest.TestCase):
    def test_units_and_identifiers(self):
        data = analyze('H100 PCIe 带宽 2 TB/s，SXM 3.35 TB/s。\n编号 1。\n成本 1,200 元，误差 10–20%。')
        self.assertEqual(data['numeric_count'], 4)
        self.assertEqual(data['unanchored_count'], 4)
    def test_anchor_and_quarantine(self):
        text = '# 总结\n速度 3 GB/s\n耗时 2 ms https://example.com\n'
        b = apply(text, 'B')
        self.assertEqual(len(b['quarantine']), 1)
        self.assertNotIn('速度 3 GB/s', b['published'])
        self.assertIn('耗时 2 ms', b['published'])
        self.assertFalse(b['raw']['numeric_claims'][1]['source_verified'])
        self.assertEqual(apply(text, 'A')['published'], text)
    def test_conflict_scope(self):
        text = 'PCIe 显存带宽 2 TB/s\nPCIe 显存带宽 3 TB/s\nSXM 显存带宽 3.35 TB/s'
        self.assertEqual(analyze(text)['conflict_pair_count'], 1)
        self.assertIn('conflict', apply(text, 'B')['quarantine'][0]['status'])
    def test_zero_denominator(self):
        result = analyze('没有量化数据。')
        self.assertIsNone(result['unanchored_rate'])
        self.assertIsNone(result['bare_hedge_rate'])
        self.assertIsNone(result['accuracy'])

if __name__ == '__main__':
    unittest.main()
