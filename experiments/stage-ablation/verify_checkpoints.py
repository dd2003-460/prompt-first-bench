#!/usr/bin/env python3
"""T53b 卡点验证测试（对应 tasks/T53-bus/checkpoints-and-tests.md 矩阵）。
origin: ai, 2026-11-20

P0（必须全过）: T1/T2/T3/T8/T9/T10/T14
P1（≥80%）: T12/T13（静态检查）；T4-T7 为半自动故障注入，本脚本标记 manual。
结果落盘 experiments/stage-ablation/verify-results.json。
用法: python3 verify_checkpoints.py
"""
import json, os, re, sys, time, subprocess, glob

STAGE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.abspath(os.path.join(STAGE, "..", ".."))
CC_STATE = os.path.join(PFB, "tasks/T53-bus/cc-state.json")
RESULTS = os.path.join(STAGE, "ablation-results.json")
DRIVER = os.path.join(STAGE, "ablation_driver.sh")
# 2026-11-20 修复: 实际在跑的是多路版 t53b-watchdog-multi.sh（pid 25886 实证）。
# 旧单路 t53b-watchdog.sh 已废弃——pgrep "t53b-watchdog.sh" 匹配不到 "-multi.sh"，
# T14 假 FAIL；T12/T13 也读错了文件（旧文件恰好含 SM_STALE 才蒙混过关）。
WATCHDOG = os.path.join(STAGE, "t53b-watchdog-multi.sh")
OUT = os.path.join(STAGE, "verify-results.json")

sys.path.insert(0, STAGE)
results = []

# 统一 import（T1/T2/T3 依赖；失败时 rh=None，后续 rh.xxx 抛 AttributeError 被各 try 捕获）
try:
    import research_hook as rh
except Exception as _e:
    rh = None
    print(f"[WARN] research_hook import 失败: {_e}")

def record(tid, name, priority, passed, detail, manual=False):
    results.append({
        "id": tid, "name": name, "priority": priority,
        "passed": passed, "manual": manual, "detail": detail,
        "ts": time.strftime("%F %T"),
    })
    mark = "SKIP" if manual else ("PASS" if passed else "FAIL")
    print(f"[{mark}] {tid} {name}: {detail}")

# ── T1: _probe_network 返回时间 ≤12s（不卡死）──
try:
    t0 = time.time()
    healthy = rh._probe_network()
    dt = time.time() - t0
    record("T1", "_probe_network 返回时间", "P0", dt <= 12,
           f"{dt:.1f}s, healthy={healthy}")
except Exception as e:
    record("T1", "_probe_network 返回时间", "P0", False, f"异常: {e}")

# ── T2: 强制不健康，_wiki_search 返回 [] 且 ≤5s（不碰 urlopen）──
try:
    rh._network_healthy = False
    rh._network_probe_at = time.time()  # 让 guard 读到 False 不重新探测
    t0 = time.time()
    r = rh._wiki_search("H100 memory bandwidth")
    dt = time.time() - t0
    record("T2", "不健康时 _wiki_search 快速降级", "P0",
           r == [] and dt <= 5, f"{dt:.2f}s, 返回 {r!r}")
except Exception as e:
    record("T2", "不健康时 _wiki_search 快速降级", "P0", False, f"异常: {e}")

# ── T3: _local_corpus_search("H100") 含 knowledge-base 来源（KB 优先级）──
try:
    r = rh._local_corpus_search("H100 memory bandwidth", max_results=5)
    kb_hits = [x for x in r if "knowledge-base" in str(x.get("url", ""))]
    record("T3", "KB 本地语料优先级", "P0", len(kb_hits) >= 1,
           f"{len(kb_hits)}/{len(r)} 命中来自 knowledge-base")
except Exception as e:
    record("T3", "KB 本地语料优先级", "P0", False, f"异常: {e}")

# ── T8: driver resume 路径是绝对路径（静态检查）──
try:
    src = open(DRIVER).read()
    # resume 调用处 CKPT 必须用 $(pwd) 前缀
    m = re.search(r'CKPT="([^"]+)"', src)
    ok = bool(m) and "$(pwd)" in m.group(1)
    record("T8", "driver resume 绝对路径", "P0", ok,
           f"CKPT={m.group(1) if m else '未找到'}")
except Exception as e:
    record("T8", "driver resume 绝对路径", "P0", False, f"异常: {e}")

# ── T9: cc-state.json 合法 ──
try:
    s = json.load(open(CC_STATE))
    n = len(s.get("work_units", []))
    done = sum(1 for w in s["work_units"] if w.get("done"))
    record("T9", "cc-state.json 合法", "P0", n > 0,
           f"{done}/{n} done")
except Exception as e:
    record("T9", "cc-state.json 合法", "P0", False, f"异常: {e}")

# ── T10: ablation-results.json 合法 ──
try:
    r = json.load(open(RESULTS))
    n = len(r.get("runs", []))
    record("T10", "ablation-results.json 合法", "P0", n > 0, f"{n} runs")
except Exception as e:
    record("T10", "ablation-results.json 合法", "P0", False, f"异常: {e}")

# ── T14: watchdog 进程存在 ──
try:
    pids = [p for p in subprocess.run(
        ["pgrep", "-f", "t53b-watchdog-multi.sh"], capture_output=True, text=True
    ).stdout.split() if p.strip()]
    record("T14", "watchdog 进程存在", "P0", len(pids) >= 1, f"pids={pids}")
except Exception as e:
    record("T14", "watchdog 进程存在", "P0", False, f"异常: {e}")

# ── T12: watchdog 有 SM stale 检测逻辑（静态检查）──
try:
    src = open(WATCHDOG).read()
    ok = "SM_STALE" in src and "sm_log" in src.lower() or "SM_STALE" in src
    record("T12", "watchdog SM stale 检测", "P1", "SM_STALE" in src,
           "含 SM_STALE 逻辑" if "SM_STALE" in src else "缺失（B1 卡点无防护）")
except Exception as e:
    record("T12", "watchdog SM stale 检测", "P1", False, f"异常: {e}")

# ── T13: watchdog 有 batch 重启逻辑（静态检查）──
try:
    src = open(WATCHDOG).read()
    ok = "nohup" in src and "t53b-batch.sh" in src
    record("T13", "watchdog batch 重启逻辑", "P1", ok,
           "含 nohup + t53b-batch.sh" if ok else "缺失")
except Exception as e:
    record("T13", "watchdog batch 重启逻辑", "P1", False, f"异常: {e}")

# ── T4-T7: 半自动故障注入（不自动执行，避免干扰正在跑的 batch）──
for tid, name, how in [
    ("T4", "watchdog 检测 SM 卡死并 kill", "启动 SM 后 block LLM 连接，观察 watchdog 120s 内 kill"),
    ("T5", "8787 挂时 SM 报错退出不卡死", "停 8787 跑一个 run，观察 SM 退出码 + watchdog 检测"),
    ("T6", "双 SM 写冲突防护", "启动 2 个 SM，观察 watchdog 清场只留 1 个"),
    ("T7", "SM FATAL 后 resume 续跑", "制造 FATAL，观察 resume 从 ckpt 继续"),
]:
    record(tid, name, "P1", None, f"manual: {how}", manual=True)

# ── 汇总 ──
auto = [r for r in results if not r["manual"]]
p0 = [r for r in auto if r["priority"] == "P0"]
p1 = [r for r in auto if r["priority"] == "P1"]
p0_pass = all(r["passed"] for r in p0)
p1_rate = (sum(1 for r in p1 if r["passed"]) / len(p1)) if p1 else 0
summary = {
    "ts": time.strftime("%F %T"),
    "p0_all_pass": p0_pass,
    "p1_rate": round(p1_rate, 2),
    "p0": {r["id"]: r["passed"] for r in p0},
    "p1": {r["id"]: r["passed"] for r in p1},
    "manual": [r["id"] for r in results if r["manual"]],
    "verdict": "PASS" if (p0_pass and p1_rate >= 0.8) else "FAIL",
}
with open(OUT, "w") as f:
    json.dump({"summary": summary, "results": results}, f, ensure_ascii=False, indent=2)
print(f"\n=== 汇总: P0 全过={p0_pass}, P1 通过率={p1_rate:.0%}, 判定={summary['verdict']} ===")
print(f"结果落盘: {OUT}")
sys.exit(0 if summary["verdict"] == "PASS" else 1)
