#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recover_sm_matched.py — 恢复 SM matched 批 driver bug 期间的记账。

背景：ablation_driver.sh 的 KeyError('RUNS_DIR') bug（1cb797f50 修复）导致
批启动后修复前的轮次只落 archive、没拷进 runs_sm_matched/、没记账。
数据完整：archive 的 synth json 含 judge 分数（零 LLM 成本恢复）。

映射规则（已用 depth 分数验证）：
  archive 目录 sm-{qid}-{ts} 的 ts = 该目录创建时刻 = 下一轮 driver 启动时刻
  （driver 每轮启动时 clean 步骤把上一轮残留文件移入新建 archive）。
  所以 archive-{rN+1 开始时间} 里存的是 rN 的数据。
  最后一轮（r10）无下一轮触发 clean → 数据由修复后的 driver 直接记账。

用法：
  python3 recover_sm_matched.py --dry-run    # 只验证映射，不写文件
  python3 recover_sm_matched.py --apply      # 批完成后再跑，执行恢复
"""
import json, os, re, sys, glob, shutil
from datetime import datetime

ROOT = "/Users/a1-6/Desktop/workspace/pfb"
STAGE = os.path.join(ROOT, "experiments/stage-ablation")
ARCHIVE = os.path.join(STAGE, "checkpoints/archive")
LOGDIR = "/tmp/ablation-sm-matched"
RUNS_DIR = os.path.join(ROOT, "modules/B-pipeline-ablation/data/t53b/runs_sm_matched")
NOTES_DIR = os.path.join(ROOT, "modules/B-pipeline-ablation/data/t53b/notes-sm-matched")
RESULTS = os.path.join(ROOT, "modules/B-pipeline-ablation/data/t53b/results-sm-matched.json")
CC_STATE = os.path.join(ROOT, "tasks/T53-bus/cc-state-sm-matched.json")
QIDS = ["nat", "soc", "gpu"]

def parse_lane_log(qid):
    """从 lane log 解析每轮的 开始/完成 时间。返回 {round: (start_dt, end_dt, status)}"""
    log = os.path.join(LOGDIR, f"sm-matched-{qid}.log")
    if not os.path.exists(log):
        return {}
    rounds = {}
    cur = None
    for line in open(log):
        m = re.match(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (开始|完成|失败): (\w+_formula_r(\d{2}))", line)
        if not m:
            continue
        ts, action, run, rnd = m.groups()
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        if action == "开始":
            cur = int(rnd)
            rounds[cur] = [dt, None, None]
        elif cur is not None:
            rounds[cur][1] = dt
            rounds[cur][2] = "done" if action == "完成" else "failed"
    return rounds

def list_archives(qid):
    """该 qid 的 archive 目录，按 ts 排序。返回 [(dt, path)]"""
    out = []
    for d in glob.glob(os.path.join(ARCHIVE, f"sm-{qid}-*")):
        m = re.match(rf"sm-{qid}-(\d{{8}}-\d{{6}})$", os.path.basename(d))
        if m:
            dt = datetime.strptime(m.group(1), "%Y%m%d-%H%M%S")
            out.append((dt, d))
    return sorted(out)

def synth_info(arch_dir):
    """读 archive 里的 synth json，返回 (depth, coverage, n_nodes, answer_len) 或 None"""
    for qid in QIDS:
        f = os.path.join(arch_dir, f"runs-s5-sm-{qid}-synth.json")
        if os.path.exists(f):
            d = json.load(open(f))
            return (d.get("depth_score"), d.get("coverage"), d.get("n_nodes"),
                    len(d.get("answer", "")), f)
    return None

def log_depth(qid, rnd, end_dt):
    """从 per-round sm log 找该轮 synth 的 depth（用于交叉验证映射）"""
    f = os.path.join(LOGDIR, f"{qid}_formula_r{rnd:02d}.sm.log")
    if not os.path.exists(f):
        return None
    depths = []
    for line in open(f):
        m = re.search(r"Synth saved.*depth=([\d.]+|None)", line)
        if m:
            depths.append(m.group(1))
    return depths[-1] if depths else None

def main():
    dry = "--dry-run" in sys.argv
    print(f"{'DRY-RUN' if dry else 'APPLY'} 模式\n")

    # 已记账的 run（runs_sm_matched 里已有的）
    booked = set()
    for f in glob.glob(os.path.join(RUNS_DIR, "*.json")):
        m = re.match(r"(\w+_formula_r\d{2})\.json$", os.path.basename(f))
        if m:
            booked.add(m.group(1))
    print(f"已记账 {len(booked)} 个: {sorted(booked)}\n")

    all_ok = True
    for qid in QIDS:
        rounds = parse_lane_log(qid)
        archives = list_archives(qid)
        print(f"=== {qid}: {len(rounds)} 轮, {len(archives)} 个 archive ===")

        # 批启动时间（第一轮开始）
        batch_start = min(r[0] for r in rounds.values()) if rounds else None

        for rnd in sorted(rounds):
            run = f"{qid}_formula_r{rnd:02d}"
            r_start, r_end, r_status = rounds[rnd]
            if run in booked:
                print(f"  r{rnd:02d}: 已记账，跳过")
                continue
            if r_end is None:
                print(f"  r{rnd:02d}: 未完成（还在跑），跳过")
                continue
            # rN 的数据所在 archive = ts 严格大于 rN_start 的最小 archive。
            # 机制：每轮启动时 clean 步骤新建 archive（ts=该轮启动时刻）并把上一轮
            # 文件移入。所以 r(N+1) 启动时建的 archive 含 rN 的数据。
            # rN 自己启动时建的 archive（ts==rN_start）含上一轮数据，必须排除。
            # "failed" 状态的轮次（driver KeyError 未记账）数据仍在 archive，照常恢复。
            # 最后一轮（r10）无下一轮，其数据由修复后的 driver 直接记账。
            cands = [(dt, p) for dt, p in archives if dt > r_start]
            if not cands:
                print(f"  r{rnd:02d}: ⚠️ 没找到 archive（数据可能在工作目录或已丢）")
                all_ok = False
                continue
            dt, arch = cands[0]
            info = synth_info(arch)
            if info is None:
                print(f"  r{rnd:02d}: ⚠️ archive {os.path.basename(arch)} 无 synth json")
                all_ok = False
                continue
            depth, cov, n_nodes, alen, src = info
            # 交叉验证：depth 是否等于该轮 sm log 的 synth depth
            ld = log_depth(qid, rnd, r_end)
            match = ""
            if ld is not None:
                match = "✓" if (str(ld) == str(depth) or (ld != "None" and depth is not None and abs(float(ld) - float(depth)) < 1e-6)) else f"✗ 不匹配(log={ld})"
                if "✗" in match:
                    all_ok = False
            print(f"  r{rnd:02d}: archive={os.path.basename(arch)} depth={depth} cov={cov} nodes={n_nodes} ans={alen}ch {match}")

            if not dry:
                # 执行恢复
                os.makedirs(RUNS_DIR, exist_ok=True)
                dst = os.path.join(RUNS_DIR, f"{run}.json")
                shutil.copy2(src, dst)
                d = json.load(open(dst))
                # 补 run 元数据（对齐 driver 记账格式）
                d["qid"] = qid
                d["arm"] = "formula"
                d["round"] = rnd
                d["recovered"] = True
                d["recovered_from"] = os.path.basename(arch)
                d["recovered_at"] = datetime.now().astimezone().isoformat()
                json.dump(d, open(dst, "w"), ensure_ascii=False, indent=2)
                # judge 文件（synth json 已含 judge，单独存一份对齐格式）
                if d.get("judge"):
                    json.dump(d["judge"], open(os.path.join(RUNS_DIR, f"{run}_judge.json"), "w"),
                              ensure_ascii=False, indent=2)
                print(f"    → 已恢复 {dst}")

    print(f"\n{'='*50}\n映射验证{'全部通过' if all_ok else '有异常，检查上面 ✗/⚠️ 行'}")
    if dry:
        print("DRY-RUN 未写任何文件。批完成且验证通过后用 --apply 执行。")

if __name__ == "__main__":
    main()
