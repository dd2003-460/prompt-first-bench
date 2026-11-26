#!/usr/bin/env python3
# origin: ai
# T8c call() finish_reason==length 截断重试 单测（mock urlopen，不真实调 27b）
# 场景A [length,length,stop] → length_retries==2, 最终 finish_reason=='stop'
# 场景B [length,length,length] → length_retries==2, 最终 finish_reason=='length', 总共只调 3 次
# 场景C [stop] → length_retries==0, 只调 1 次
import io, json, unittest
from unittest import mock

import run_exp_t8c


def _make_response(fr, content="ok", reasoning="think"):
    return io.BytesIO(json.dumps({
        "choices": [{"message": {"content": content, "reasoning": reasoning},
                     "finish_reason": fr}],
        "usage": {"completion_tokens": 10},
    }).encode())


class FakeUrlopen:
    """按序吐出预设 finish_reason 序列的 urlopen 替身；记录调用次数"""
    def __init__(self, seq):
        self.seq = list(seq)
        self.calls = 0

    def __call__(self, req, timeout=None):
        self.calls += 1
        assert self.seq, f"urlopen called {self.calls}x but sequence exhausted"
        return _make_response(self.seq.pop(0))


class TestCallLengthRetry(unittest.TestCase):
    def _run(self, seq):
        fake = FakeUrlopen(seq)
        with mock.patch.object(run_exp_t8c.urllib.request, "urlopen", side_effect=fake), \
             mock.patch.object(run_exp_t8c.time, "sleep"):
            r = run_exp_t8c.call([{"role": "user", "content": "hi"}], 12288, "test")
        return r, fake

    def test_a_length_length_stop(self):
        r, fake = self._run(["length", "length", "stop"])
        self.assertEqual(r["length_retries"], 2)
        self.assertEqual(r["finish_reason"], "stop")
        self.assertEqual(fake.calls, 3)

    def test_b_three_lengths(self):
        r, fake = self._run(["length", "length", "length"])
        self.assertEqual(r["length_retries"], 2)
        self.assertEqual(r["finish_reason"], "length")
        self.assertEqual(fake.calls, 3, "3 次（首次+2 重试）后必须停止，不再重试")

    def test_c_stop_first_try(self):
        r, fake = self._run(["stop"])
        self.assertEqual(r["length_retries"], 0)
        self.assertEqual(r["finish_reason"], "stop")
        self.assertEqual(fake.calls, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
