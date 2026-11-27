#!/usr/bin/env python3
"""Q9 post_acc 救活探针 — 全量 LLM 判定 + 数值一致性检查。

动机 (2026-11-27): s5_state_machine._scan_contradictions 太弱 (每轮只扫 30 节点、
只报 5 个), 10 个 run 只抓到 2 个矛盾事件, post_acc 恒 = 1.0, 无区分度。
本探针用更强仪器重算 post_acc = verified/(verified+contradicted):

  1. 数值一致性检查 (纯脚本): 从 claim 抽数值参数 (参数名+值+单位),
     同一参数名不同节点数值差异 >10% 记一个 contradiction。
  2. LLM judge 全量判定 (qwen3.8-27b @8787, temp=0): 对每个 run 全部
     verified 节点, 每批 20 个, 判 (a) 互相矛盾 (b) 明显无依据/荒谬。

输入: data/q9-budget-scan/q9-{50,100,150,300}-r{1,2,3}-*.json (300 只有 r1)
输出: data/q9-budget-scan/postacc-rescue-probe-<date>.json
缓存: data/q9-budget-scan/.postacc-rescue-cache/ (幂等, 命中跳过 LLM)

口径: post_acc_rescued = (n_verified - min(n_verified, n_num_contra + n_llm_contra)) / n_verified
     (n_unsupported 单独记录, 不计入 post_acc 分子扣减 — 保守口径)
"""
import json, os, re, sys, time, urllib.request
from datetime import datetime, timezone
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # modules/B-pipeline-ablation
DATA = os.path.join(BASE, "data", "q9-budget-scan")
LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
BATCH = 20
CACHE = os.path.join(DATA, ".postacc-rescue-cache")
MAX_RETRIES = 2
CLAIM_TRUNC = 400

# ---------- 数值参数抽取 ----------
UNIT = (r"(?:TB|GB|MB|KB|TBps|GBps|MBps|KBps)/s|TFLOPS|GFLOPS|MFLOPS|FLOPS|FLOPs|TOPS|"
        r"kWh|MWh|Wh|Joule|Joules|kW|MW|GW|kW|W|GHz|MHz|kHz|Hz|%"
        r"|元|USD|美元|€|tokens?/s|ms|µs|us|ns|秒|分钟|小时|天|周|月|年|倍|层|卡|核|"
        r"GPU|V100|A100|H100|B200|GB200|NVLink|bits?|bps|bytes?|vCPU|cores")
# 参数名: 汉字/字母开头, 可含汉字/字母/数字/下划线/连字符/点/空格, 最长 24 字;
# 可选分隔符 (= : ： 为 是 约 达); 紧跟数值; 可选空格; 单位 (后接非字母数字, 防 GB200 误配)
NUM_PARAM_RE = re.compile(
    r"(?<![0-9A-Za-z\u4e00-\u9fff])"
    r"(?P<name>[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z_\-.\s]{0,15})"
    r"\s*[=:：为是约达]?\s*"
    r"(?P<val>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"
    r"\s*(?P<unit>" + UNIT + r")(?![0-9A-Za-z])")

STOP_NAMES = {"大约", "约为", "超过", "低于", "高于", "小于", "大于", "至少",
              "最多", "平均", "共计", "总共", "合计", "其中", "以及", "但是", "如果",
              "假设", "例如", "比如", "截止", "截至", "公元", "版本", "编号", "日期",
              "需要", "支持", "拥有", "配备", "使用", "采用", "达到", "约", "共",
              "总", "每", "各", "该", "此", "其", "之", "和", "与", "或", "但",
              "而", "在", "有", "是", "为", "达", "超", "低", "高", "小", "大",
              "当", "若", "则", "即", "年", "月", "日", "周", "时", "分", "秒",
              "左右", "以内", "以上", "以下", "期间", "前后", "上下", "大概",
              "大致", "接近", "几乎", "将近", "不足", "不到", "少于", "多于",
              "相当于", "约合", "估计", "估算", "预估", "预计", "假定", "设定",
              "设置", "配置", "规格", "指标", "参数", "数值", "数量", "比例",
              "比率", "占比", "份额", "规模", "容量", "大小", "长度", "宽度",
              "高度", "深度", "厚度", "面积", "体积", "重量", "质量", "密度",
              "强度", "速度", "速率", "频率", "周期", "相位", "幅度", "增益",
              "损耗", "效率", "性能", "能力", "水平", "程度", "范围", "区间",
              "界限", "边界", "极限", "上限", "下限", "峰值", "谷值", "均值",
              "中值", "总值", "净值", "余额", "差额", "差距", "距离", "间隔",
              "间距", "间隙", "空隙", "空间", "时间", "时长", "期限", "工期",
              "节奏", "频次", "次数", "回数", "遍数", "轮数", "回合", "阶段",
              "环节", "步骤", "工序", "流程", "程序", "过程", "进度", "进展",
              "约等于", "折算", "换算", "计算", "限定", "限制条件"}

# 动词/介词尾巴: 贪心 name 会吞掉这些, 从 name 尾部剥掉 (剥后须 >=2 字)
TRAIL_VERBS = ("需要", "提升至", "提升到", "提升至", "降低至", "降到", "升至", "提高到",
               "提升至", "增加至", "减少至", "压缩至", "扩大至", "缩小至", "优化到",
               "提升至", "当", "若", "在", "为", "是", "约", "达", "超", "至", "到",
               "约", "近", "近", "超", "低", "高", "小", "大", "每", "各", "该", "此",
               "其", "之", "和", "与", "或", "但", "而", "有", "被", "将", "把", "让",
               "使", "需", "要", "求", "称", "示", "指", "表", "含", "占", "计", "估")

def _trim_name(norm):
    changed = True
    while changed and len(norm) > 2:
        changed = False
        for v in TRAIL_VERBS:
            if norm.endswith(v) and len(norm) - len(v) >= 2:
                norm = norm[: -len(v)]
                changed = True
                break
    return norm

def _norm_unit(u):
    return u.strip().lower().replace("µs", "us")

def extract_params(claim):
    """claim -> [(name_norm, value, unit_norm)]"""
    out = []
    for m in NUM_PARAM_RE.finditer(claim):
        name = m.group("name").strip()
        norm = re.sub(r"\s+", "", name).lower()
        norm = _trim_name(norm)
        if len(norm) < 2:
            continue
        if norm in STOP_NAMES:
            continue
        try:
            val = float(m.group("val"))
        except ValueError:
            continue
        out.append((norm, val, _norm_unit(m.group("unit"))))
    return out

def numeric_contradictions(nodes):
    """nodes: [{id, claim}] -> (n_contra_params, {param: [(nid,val,unit)...]}, contra_node_ids)
    同 (参数名, 单位) 组内数值差异 >10% 记一个 contradiction; 不同单位不比较."""
    param_map = defaultdict(list)
    for n in nodes:
        for name, val, unit in extract_params(n.get("claim", "")):
            param_map[(name, unit)].append((n["id"], val, unit))
    contra_params = {}
    contra_nodes = set()
    for (name, unit), entries in param_map.items():
        vals = sorted({v for _, v, _ in entries})
        if len(vals) < 2:
            continue
        lo, hi = vals[0], vals[-1]
        if hi > 0 and (hi - lo) / hi > 0.10:
            contra_params[f"{name} ({unit})"] = [{"node": nid, "val": v, "unit": u} for nid, v, u in entries]
            contra_nodes.update(e[0] for e in entries)
    return len(contra_params), contra_params, contra_nodes

# ---------- LLM judge ----------
def call_llm(prompt, max_tokens=8192, timeout=300):
    payload = json.dumps({"model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": 0.0}).encode()
    req = urllib.request.Request(LLM_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    return d["choices"][0]["message"].get("content", "")

def parse_json_array(out):
    """模型夹带思考文字时取最后一个能解析的 JSON 数组 (从末尾 ] 向前配平)."""
    res = []
    end = out.rfind("]")
    while end > 0:
        depth = 0; start = -1
        for i in range(end, -1, -1):
            ch = out[i]
            if ch == "]":
                depth += 1
            elif ch == "[":
                depth -= 1
                if depth == 0:
                    start = i
                    break
        if start >= 0:
            try:
                arr = json.loads(out[start:end + 1])
                if isinstance(arr, list) and arr and isinstance(arr[0], dict) and "node" in arr[0]:
                    res = arr
                    break
            except Exception:
                pass
        end = out.rfind("]", 0, end)
    return res

def judge_batch(nodes):
    """nodes: [(nid, claim)] -> {nid: issue} 或 None (解析失败)"""
    npart = "\n".join(f"[{nid}] {c[:CLAIM_TRUNC]}" for nid, c in nodes)
    prompt = (
        "任务: 一致性判定。下面是某科研 run 中标记为 verified 的 claim 列表 (NODES)。\n"
        "对每个 NODE 判断:\n"
        "(a) contradiction: 该 claim 与本列表中另一 claim 存在数值或逻辑矛盾"
        "(同一参数不同数值、互斥结论、单位混淆导致的矛盾等);\n"
        "(b) unsupported: 该 claim 含明显无依据、荒谬或物理上不可能的数值/断言"
        "(如违反公开硬件规格、量级明显错误、凭空捏造的精确数字);\n"
        "(c) none: 以上都不是。\n"
        "注意: 同一参数在不同语境下取不同值 (如不同芯片/不同工况) 不算矛盾; "
        "合理估算区间内的差异不算矛盾。只判硬矛盾和明显荒谬。\n"
        "输出要求(严格遵守): 只输出一个 JSON 数组, 不要任何解释/前言/思考文字, "
        "每项 {\"node\":\"<nid>\",\"issue\":\"contradiction|unsupported|none\",\"desc\":\"<简要理由, none 时空字符串>\"}。\n"
        "必须覆盖全部 NODE, 不得遗漏。\n\n"
        f"NODES:\n{npart}"
    )
    out = call_llm(prompt)
    arr = parse_json_array(out)
    if not arr:
        return None
    res = {}
    for it in arr:
        nid = it.get("node")
        issue = it.get("issue", "none")
        if issue not in ("contradiction", "unsupported", "none"):
            issue = "none"
        res[nid] = {"issue": issue, "desc": str(it.get("desc", ""))[:200]}
    return res

def judge_run(fn, verified_nodes):
    """verified_nodes: [(nid, claim)] -> ({nid: info}, n_error_batches)"""
    per_node = {}
    n_err = 0
    for i in range(0, len(verified_nodes), BATCH):
        ck = f"{fn}_b{i // BATCH}.json"
        cf = os.path.join(CACHE, ck)
        if os.path.exists(cf):
            cached = json.load(open(cf))
            if cached.get("status") == "ok":
                per_node.update(cached["result"])
                continue
            if cached.get("status") == "error":
                n_err += 1
                continue
        chunk = verified_nodes[i:i + BATCH]
        ok = False
        for attempt in range(MAX_RETRIES + 1):
            try:
                r = judge_batch(chunk)
                if r is not None:
                    per_node.update(r)
                    os.makedirs(CACHE, exist_ok=True)
                    tmp = cf + ".tmp"
                    json.dump({"status": "ok", "result": r}, open(tmp, "w"), ensure_ascii=False)
                    os.replace(tmp, cf)
                    ok = True
                    break
            except Exception as e:
                print(f"  WARN {fn} batch{i // BATCH} attempt{attempt}: {e}", flush=True)
                time.sleep(2 * (attempt + 1))
        if not ok:
            n_err += 1
            os.makedirs(CACHE, exist_ok=True)
            tmp = cf + ".tmp"
            json.dump({"status": "error"}, open(tmp, "w"), ensure_ascii=False)
            os.replace(tmp, cf)
            print(f"  ERROR {fn} batch{i // BATCH}: marked error, skipped", flush=True)
        time.sleep(0.5)
    return per_node, n_err

# ---------- main ----------
def main():
    runs = sorted(f for f in os.listdir(DATA)
                  if re.match(r"q9-\d+-r\d+-2026.*\.json$", f))
    assert len(runs) == 10, f"expected 10 runs, got {len(runs)}: {runs}"
    per_run = []
    for fn in runs:
        m = re.match(r"q9-(\d+)-r(\d+)", fn)
        budget, rid = int(m.group(1)), int(m.group(2))
        d = json.load(open(os.path.join(DATA, fn)))
        nodes = d.get("nodes", [])
        verified = [(n["id"], n.get("claim", "")) for n in nodes if n.get("status") == "verified"]
        n_verified = len(verified)

        # 1) 数值一致性 (全节点, 不只 verified — 矛盾可能藏在 degraded/pending 里)
        n_num, contra_params, contra_nodes = numeric_contradictions(nodes)

        # 2) LLM 全量判定 (verified 节点)
        per_node, n_err = judge_run(fn, verified)
        n_llm = sum(1 for v in per_node.values() if v["issue"] == "contradiction")
        n_unsup = sum(1 for v in per_node.values() if v["issue"] == "unsupported")

        n_contra_total = min(n_verified, n_num + n_llm)
        post_acc = round((n_verified - n_contra_total) / n_verified, 4) if n_verified else None
        rec = {
            "file": fn, "budget": budget, "rep": rid,
            "n_nodes": len(nodes), "n_verified": n_verified,
            "n_contradictions_numeric": n_num,
            "n_contradictions_llm": n_llm,
            "n_unsupported": n_unsup,
            "n_error_batches": n_err,
            "n_judged_nodes": len(per_node),
            "numeric_contra_params": {k: v for k, v in list(contra_params.items())[:20]},
            "llm_issues": {nid: v for nid, v in per_node.items() if v["issue"] != "none"},
            "post_acc_rescued": post_acc,
        }
        per_run.append(rec)
        print(f"{fn}: verified={n_verified} num_contra={n_num} llm_contra={n_llm} "
              f"unsupported={n_unsup} err_batches={n_err} post_acc_rescued={post_acc}", flush=True)

    per_budget = {}
    for b in sorted({r["budget"] for r in per_run}):
        vals = [r["post_acc_rescued"] for r in per_run if r["budget"] == b and r["post_acc_rescued"] is not None]
        per_budget[str(b)] = round(sum(vals) / len(vals), 4)

    all_pa = [r["post_acc_rescued"] for r in per_run if r["post_acc_rescued"] is not None]
    out = {
        "instrument": "postacc-rescue-probe: numeric-consistency (regex) + LLM judge "
                      f"({MODEL} @127.0.0.1:8787, temp=0, batch={BATCH})",
        "observed_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "per_run": per_run,
        "per_budget_mean": per_budget,
        "overall_mean": round(sum(all_pa) / len(all_pa), 4) if all_pa else None,
        "baseline_post_acc": 1.0,
        "note": "post_acc_rescued=(n_verified-min(n_verified,n_num+n_llm))/n_verified; "
                "n_unsupported 单独记录未计入扣减(保守口径); 数值检查覆盖全部节点, LLM 只判 verified; "
                "n_num 按矛盾参数个数计, n_llm 按矛盾节点数计, 两者相加可能有少量重复计数",
    }
    fp = os.path.join(DATA, f"postacc-rescue-probe-{datetime.now().strftime('%Y%m%d')}.json")
    tmp = fp + ".tmp"
    json.dump(out, open(tmp, "w"), ensure_ascii=False, indent=1)
    os.replace(tmp, fp)
    print(f"\nSUMMARY per_budget_mean={json.dumps(per_budget)} overall={out['overall_mean']} baseline=1.0")
    print("saved:", fp)

if __name__ == "__main__":
    main()
