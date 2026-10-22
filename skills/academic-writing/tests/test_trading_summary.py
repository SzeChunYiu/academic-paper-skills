import copy
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).parents[2] / 'nature-shared/scripts/verify_trading_summary.py'
spec = importlib.util.spec_from_file_location('trading_summary', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class TradingSummaryTests(unittest.TestCase):
    def setUp(self):
        self.data = dict(metric='log_bp_day', aggregation='equal_panel_mean',
                         panels=[dict(id='a', **{'return': 30}, max_drawdown_pct=60),
                                 dict(id='b', **{'return': -10}, max_drawdown_pct=20)],
                         reported_mean=10, claims_all_positive=False)
    def test_heterogeneous_positive_mean_is_allowed(self):
        self.assertEqual(module.validate(self.data), [])
    def test_positive_mean_cannot_rescue_all_positive_claim(self):
        self.data['claims_all_positive'] = True
        self.assertTrue(module.validate(self.data))
    def test_wrong_mean_rejected(self):
        self.data['reported_mean'] = 30
        self.assertTrue(module.validate(self.data))
    def test_risk_cannot_be_omitted(self):
        del self.data['panels'][0]['max_drawdown_pct']
        self.assertTrue(module.validate(self.data))
    def test_nonfinite_and_boolean_numbers_rejected(self):
        for v in (float('nan'), float('inf'), True, '30'):
            d=copy.deepcopy(self.data);d['panels'][0]['return']=v
            self.assertTrue(module.validate(d))
    def test_panel_mean_is_not_pooled_account(self):
        self.data['aggregation']='pooled_account'
        self.assertTrue(module.validate(self.data))
    def test_duplicate_identity_rejected(self):
        self.data['panels'][1]['id']='a'
        self.assertTrue(module.validate(self.data))
    def test_metric_semantics_required(self):
        self.data['metric']='bp_day'
        self.assertTrue(module.validate(self.data))
    def test_bad_structures_rejected(self):
        for value in (None, [], {'panels':[]}, {'panels':[None]}):
            self.assertTrue(module.validate(value))
    def test_unknown_risk_and_zero_are_not_equal(self):
        self.data['panels'][0]['max_drawdown_pct']=None
        self.assertTrue(module.validate(self.data))
        self.data['panels'][0]['max_drawdown_pct']=0
        self.assertEqual(module.validate(self.data), [])

if __name__ == '__main__': unittest.main()
