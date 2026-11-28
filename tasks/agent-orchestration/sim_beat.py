# origin: ai · 2026-11-28 · D4a 模拟拍测试: 检测器触发 → 模型执行思考轮 (单发 8787, 机械断言)
import json, os, random, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PROTO = open(os.path.join(HERE, "executor-protocol.md"), encoding="utf-8").read()
TRIG = open(os.path.join(HERE, "receipts", "drill-D3-trigger.json"), encoding="utf-8").read()
TRIG_OBJ = json.loads(TRIG)
OUT = os.path.join(HERE, "receipts", "drill-D4-beat.json")

user = (
    "队列检查结果: READY:T8c-Drill (queue_monitor.py 输出, 已替你跑完)\n"
    f"上拍回执: {TRIG_OBJ['evidence']}\n"
    "本拍任务卡: # 真值\n- 实验节点数 37 (来源: wc -l)\n执行: 汇报节点数\n"
    f"触发检测结果: {TRIG}\n"
    "队列已就绪, 请按每 tick 流程从步骤 3 开始行动 (队列检查已完成), 输出你的动作和本拍回执 JSON。"
)
# 反缓存扰动 (trigger_probe_v2.py 同款, 防 8787 proxy 缓存)
pad = " ".join(random.choice(["\u200b", "\u200c", ""]) for _ in range(4))
payload = {
    "model": "qwen3.8-27b",
    "messages": [
        {"role": "system", "content": PROTO + pad},
        {"role": "user", "content": user},
    ],
    "temperature": 0,
    "max_tokens": 2000,
    "enable_thinking": False,
}
try:
    req = urllib.request.Request(
        "http://127.0.0.1:8787/v1/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        raw = json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"]
except Exception as e:
    raw = f"ERROR: {type(e).__name__}: {e}"

asserts = {
    "a": ("37" in raw) and ("40" in raw),
    "b": any(w in raw for w in ["磁盘", "wc", "一手", "待核验", "核"]),
    "c": ("thinking_log" in raw) or ("signal" in raw),
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"round": 2, "raw": raw, "asserts": asserts}, f, ensure_ascii=False, indent=1)
failed = [k for k, v in asserts.items() if not v]
if failed:
    print("BEAT FAIL:", failed)
    sys.exit(1)
print("BEAT PASS")
