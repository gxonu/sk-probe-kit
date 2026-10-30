"""Synthetic educational scenarios. Not a production analysis/model library.

No external packages, input files, network calls, or actual manufacturing data.
"""
import math
import unittest
from collections import defaultdict


def unique_join(left, right):
    """Toy m:1 left join; reject unknown/duplicate/null keys instead of guessing."""
    lookup = {}
    for key, value in right:
        if key is None or key in lookup:
            raise ValueError('right keys must be non-null and unique')
        lookup[key] = value
    if any(key is None or key not in lookup for key in left):
        raise ValueError('unmatched or null left key')
    return [(key, lookup[key]) for key in left]


def yields(attempts):
    """Fixture contract: first/last attempt determines pass, no missing attempts."""
    if not attempts:
        raise ValueError('no tested units')
    units = defaultdict(dict)
    for unit, attempt, passed in attempts:
        if unit is None or attempt in units[unit] or type(passed) is not bool:
            raise ValueError('invalid or duplicate attempt')
        units[unit][attempt] = passed
    first = sum(v[min(v)] for v in units.values())
    final = sum(v[max(v)] for v in units.values())
    return first / len(units), final / len(units)


def wilson(d, n, z=1.96):
    if type(d) is not int or type(n) is not int or n <= 0 or not 0 <= d <= n:
        raise ValueError('require integer 0 <= d <= n and n > 0')
    if not math.isfinite(z) or z <= 0:
        raise ValueError('positive finite z required')
    p = d / n
    scale = 1 + z * z / n
    center = (p + z * z / (2 * n)) / scale
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / scale
    return max(0, center - half), min(1, center + half)


def p_limits(p, n):
    if not 0 <= p <= 1 or type(n) is not int or n <= 0:
        raise ValueError('invalid baseline or exposure')
    delta = 3 * math.sqrt(p * (1 - p) / n)
    return max(0, p - delta), min(1, p + delta)


def capability(low, high, mean, sigma):
    if not all(math.isfinite(x) for x in (low, high, mean, sigma)) or low >= high or sigma <= 0:
        raise ValueError('ordered specifications and positive sigma required')
    return (high - low) / (6 * sigma), min(high - mean, mean - low) / (3 * sigma)


def past_value(events, group, predict_at, max_age):
    """Times are minutes from a common origin; event tuple=(group,event,available,value)."""
    if max_age < 0:
        raise ValueError('negative age')
    candidates = [e for e in events if e[0] == group and e[1] <= predict_at
                  and e[2] <= predict_at and predict_at - e[1] <= max_age]
    return max(candidates, key=lambda e: e[1])[3] if candidates else None


def validate_split(train, validation, cutoff):
    """Fixture contract: unseen groups in future; tuple=(group,prediction,label_available)."""
    if not train or not validation:
        raise ValueError('empty partition')
    if {x[0] for x in train} & {x[0] for x in validation}:
        raise ValueError('group overlap')
    if any(pred > cutoff or available > cutoff for _, pred, available in train):
        raise ValueError('future training information')
    if any(pred <= cutoff for _, pred, _ in validation):
        raise ValueError('validation is not in future')


def binary_metrics(truth, prediction):
    if not truth or len(truth) != len(prediction) or any(v not in (0, 1) for v in truth + prediction):
        raise ValueError('aligned non-empty binary labels required')
    tp = sum(y == 1 and p == 1 for y, p in zip(truth, prediction))
    fp = sum(y == 0 and p == 1 for y, p in zip(truth, prediction))
    fn = sum(y == 1 and p == 0 for y, p in zip(truth, prediction))
    tn = len(truth) - tp - fp - fn
    ratio = lambda a, b: a / b if b else None  # explicitly undefined, not silently perfect
    return dict(TP=tp, FP=fp, FN=fn, TN=tn, precision=ratio(tp, tp + fp),
                recall=ratio(tp, tp + fn), F1=ratio(2 * tp, 2 * tp + fp + fn),
                accuracy=(tp + tn) / len(truth))


def validate_submission(expected, actual):
    """Fixture contract: exact ID order and one finite probability per ID."""
    ids = [row[0] for row in actual]
    if len(set(expected)) != len(expected) or len(set(ids)) != len(ids) or ids != expected:
        raise ValueError('wrong IDs/order or duplicates')
    if any(not math.isfinite(value) or not 0 <= value <= 1 for _, value in actual):
        raise ValueError('invalid probability')


class ApplicationChecks(unittest.TestCase):
    def test_yield_with_retests_and_join(self):
        attempts = [(f'd{i}', 1, i < 8) for i in range(10)]
        attempts += [('d8', 2, True), ('d9', 2, False)]
        self.assertEqual(yields(list(reversed(attempts))), (.8, .9))
        self.assertEqual(sum(x[2] for x in attempts) / len(attempts), .75)
        self.assertEqual(len(unique_join([x[0] for x in attempts], [(f'd{i}', 'lotA') for i in range(10)])), 12)
        self.assertAlmostEqual((1 + 90) / (2 + 100), .892156862745098)
        self.assertAlmostEqual((.5 + .9) / 2, .7)

    def test_retest_is_not_any_pass(self):
        self.assertEqual(yields([('d1', 1, True), ('d1', 2, False)]), (1, 0))
        for bad in ([], [('d1', 1, True), ('d1', 1, False)]):
            with self.assertRaises(ValueError):
                yields(bad)

    def test_join_rejects_ambiguous_or_missing_keys(self):
        for right in ([('a', 1), ('a', 2)], [(None, 1)], [('b', 1)]):
            with self.assertRaises(ValueError):
                unique_join(['a'], right)

    def test_wilson_and_zero_defects(self):
        low, high = wilson(2, 100)
        self.assertAlmostEqual(low, .005501852234968185)
        self.assertAlmostEqual(high, .07001316294199365)
        self.assertAlmostEqual(wilson(0, 100)[0], 0)
        self.assertGreater(wilson(0, 100)[1], 0)
        self.assertAlmostEqual(wilson(100, 100)[1], 1)
        for args in ((0, 0), (101, 100), (-1, 10)):
            with self.assertRaises(ValueError):
                wilson(*args)

    def test_spc_and_capability_are_separate(self):
        self.assertEqual(p_limits(.02, 100), (0, .062))
        self.assertGreater(8 / 100, p_limits(.02, 100)[1])
        # The sparse discrete tail differs from a normal upper 3-sigma tail.
        tail = sum(math.comb(100, k) * .02**k * .98**(100-k) for k in range(7, 101))
        self.assertAlmostEqual(tail, .0040620540801008355)
        self.assertGreater(tail, .00135)
        self.assertLess(p_limits(.02, 400)[1], p_limits(.02, 100)[1])
        cp, cpk = capability(90, 110, 102, 2)
        self.assertAlmostEqual(cp, 5 / 3)
        self.assertAlmostEqual(cpk, 4 / 3)
        self.assertAlmostEqual(capability(90, 110, 108, 2)[1], 1 / 3)
        self.assertLess(capability(90, 110, 112, 2)[1], 0)
        for args in ((90, 110, 100, 0), (110, 90, 100, 2)):
            with self.assertRaises(ValueError):
                capability(*args)

    def test_product_mix_reverses_aggregate(self):
        self.assertGreater(9 / 10, 80 / 100)
        self.assertGreater(20 / 100, 1 / 10)
        self.assertLess(29 / 110, 81 / 110)

    def test_point_in_time_join(self):
        events = [('A', 595, 596, 10), ('A', 598, 602, 99),
                  ('A', 601, 601, 88), ('B', 599, 599, 77)]
        self.assertEqual(past_value(events, 'A', 600, 5), 10)
        self.assertIsNone(past_value(events, 'A', 600, 4))
        self.assertIsNone(past_value(events, 'C', 600, 5))
        self.assertEqual(past_value(events, 'A', 602, 5), 88)
        self.assertEqual(past_value([('A', 600, 600, 5)], 'A', 600, 0), 5)

    def test_group_and_time_validation(self):
        train = [('A', 1, 2), ('B', 3, 4)]
        validate_split(train, [('C', 6, 7)], 5)
        for tr, va in ((train, [('B', 6, 7)]),
                       ([('A', 1, 6)], [('C', 6, 7)]),
                       (train, [('C', 5, 7)])):
            with self.assertRaises(ValueError):
                validate_split(tr, va, 5)

    def test_imputation_uses_training_only(self):
        train, validation = [10, None, 20], [1000, None]
        observed = [x for x in train if x is not None]
        fill = sum(observed) / len(observed)
        transformed = [fill if x is None else x for x in validation]
        self.assertEqual(transformed, [1000, 15])
        self.assertNotEqual(fill, (10 + 20 + 1000) / 3)

    def test_rare_defect_metrics_against_baseline(self):
        truth = [1] * 10 + [0] * 990
        pred = [1] * 8 + [0] * 2 + [1] * 12 + [0] * 978
        m = binary_metrics(truth, pred)
        self.assertEqual((m['TP'], m['FP'], m['FN'], m['TN']), (8, 12, 2, 978))
        self.assertEqual((m['precision'], m['recall'], m['accuracy']), (.4, .8, .986))
        self.assertAlmostEqual(m['F1'], 8 / 15)
        baseline = binary_metrics(truth, [0] * 1000)
        self.assertEqual((baseline['accuracy'], baseline['recall']), (.99, 0))
        self.assertIsNone(baseline['precision'])
        self.assertIsNone(binary_metrics([0], [0])['recall'])

    def test_regression_units(self):
        actual, pred = [10, 20], [12, 19]
        errors = [p - y for p, y in zip(pred, actual)]
        self.assertEqual(sum(abs(e) for e in errors) / 2, 1.5)
        self.assertAlmostEqual(math.sqrt(sum(e * e for e in errors) / 2), 1.5811388300841898)

    def test_alarm_samples_and_events(self):
        alarms = [False] + [True] * 10 + [False]
        starts = sum(flag and (i == 0 or not alarms[i - 1]) for i, flag in enumerate(alarms))
        self.assertEqual((sum(alarms), starts), (10, 1))
        self.assertEqual(20 / 1000, .02)

    def test_cross_stage_hbm_bandwidth(self):
        capacity_bytes = 16 * 2**30 * 8 / 8
        peak_bytes_s = 1024 * 4e9 / 8
        measured_bytes_s = 320e9
        self.assertEqual(capacity_bytes / 2**30, 16)
        self.assertEqual(peak_bytes_s / 1e9, 512)
        self.assertEqual(measured_bytes_s / peak_bytes_s, .625)
        self.assertNotEqual(peak_bytes_s, peak_bytes_s * 8)

    def test_observed_bandwidth_already_includes_latency(self):
        from pathlib import Path
        data_bytes, stream_bytes_s, latency_s = 100e6, 2e9, .01
        total_s = latency_s + data_bytes / stream_bytes_s
        observed_bytes_s = data_bytes / total_s
        self.assertAlmostEqual(total_s, .06)
        self.assertAlmostEqual(data_bytes / observed_bytes_s, total_s)
        self.assertAlmostEqual(latency_s + data_bytes / observed_bytes_s, .07)
        # Limited text linkage for this repaired example, not a semantic proof.
        body = (Path(__file__).resolve().parents[1] / 'fundamentals/capacity-bandwidth-latency.md').read_text()
        for token in ('B_obs = D/t_total', 'L + D/B_stream', '0.06 s', '0.07 s'):
            self.assertIn(token, body)

    def test_capacitance_uses_absolute_permittivity(self):
        from pathlib import Path
        epsilon0_F_m, relative, area_m2, gap_m = 8.85e-12, 4, 1e-12, 1e-8
        capacitance_F = (relative * epsilon0_F_m) * area_m2 / gap_m
        self.assertAlmostEqual(capacitance_F / 1e-15, 3.54)
        self.assertAlmostEqual(capacitance_F / (epsilon0_F_m * area_m2 / gap_m), relative)
        wrong_F = relative * area_m2 / gap_m
        self.assertGreater(wrong_F / capacitance_F, 1e11)
        # Limited linkage for this example; not full semantic verification.
        body = (Path(__file__).resolve().parents[1] / 'fundamentals/capacitance.md').read_text()
        for token in ('ε = κ ε0', 'F/m', '무차원', '3.54 fF', 'S84'):
            self.assertIn(token, body)

    def test_submission_contract(self):
        validate_submission(['a', 'b', 'c'], [('a', .1), ('b', .2), ('c', .3)])
        for bad in ([('a', .1), ('a', .2), ('c', .3)],
                    [('a', .1), ('b', .2)],
                    [('a', .1), ('b', .2), ('d', .3)],
                    [('b', .1), ('a', .2), ('c', .3)],
                    [('a', math.nan), ('b', .2), ('c', .3)],
                    [('a', 1.1), ('b', .2), ('c', .3)]):
            with self.assertRaises(ValueError):
                validate_submission(['a', 'b', 'c'], bad)


def run_checks():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ApplicationChecks)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    return result.testsRun


if __name__ == '__main__':
    run_checks()
