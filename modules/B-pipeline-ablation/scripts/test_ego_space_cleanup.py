"""防回归: research_hook 三处 ego taskSpace 必须配对 task.finish 清理。

背景: webllm/arxiv/webfetch 三处检索每次创建 taskSpace 从不清理,
62 run 跑下来泄漏数百个 ego space (用户手动全关过)。
修复: 每处 JS 尾部加 task.finish({keep:[]})。

本测试离线秒级: monkeypatch _run_ego_browser 捕获生成的 JS,
断言每个含 taskSpace 的 JS 都含 task.finish 且顺序正确。
不联网、不真跑浏览器。
"""
import unittest
import research_hook


class EgoSpaceCleanupTest(unittest.TestCase):
    def _capture_js(self):
        """monkeypatch _run_ego_browser, 跑三处检索函数, 收集生成的 JS。"""
        captured = []
        orig = research_hook._run_ego_browser
        research_hook._run_ego_browser = lambda js, timeout=120: (captured.append(js), "")[1] or ""
        try:
            for fn, args in [
                (research_hook._arxiv_search, ("gpu inference throughput",)),
                (research_hook._fetch_page, ("https://example.com", "t")),
            ]:
                try:
                    fn(*args)
                except Exception:
                    pass  # 网络/解析失败无所谓, 只要 JS 已生成
            # webllm: 直接构造其 JS (函数内嵌 endpoints 循环, 走 _run_ego_browser)
            try:
                research_hook._webllm_search("gpu inference")
            except Exception:
                pass
        finally:
            research_hook._run_ego_browser = orig
        return captured

    def test_every_taskspace_has_finish(self):
        captured = self._capture_js()
        # 至少 arxiv + fetch 两处应被捕获 (webllm 可能因额度墙提前 return 但仍生成 JS)
        self.assertGreaterEqual(len(captured), 2, f"只捕获到 {len(captured)} 个 JS, 预期 >=2")
        for i, js in enumerate(captured):
            if "taskSpace" not in js:
                continue  # 非 ego 通道
            self.assertIn("task.finish", js, f"JS#{i} 有 taskSpace 但无 task.finish (泄漏)")
            self.assertLess(
                js.index("taskSpace"), js.index("task.finish"),
                f"JS#{i} task.finish 在 taskSpace 之前 (作用域错)",
            )

    def test_finish_keeps_nothing(self):
        """清理必须 keep:[] — 不留 page 给后续 (检索是一次性的)。"""
        for i, js in enumerate(self._capture_js()):
            if "task.finish" in js:
                self.assertIn("keep: []", js.replace("{{", "{").replace("}}", "}"),
                               f"JS#{i} task.finish 未用 keep:[]")


if __name__ == "__main__":
    unittest.main(verbosity=2)
