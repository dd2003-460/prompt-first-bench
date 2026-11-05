#!/usr/bin/env python3
"""Fullloop multi-stage pipeline runner for T8-C3 G2 matrix completion."""
import json, os, time, hashlib, urllib.request, sys

VLLM_URL = "http://localhost:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
TEMPERATURE = 0.7
MAX_TOKENS = 4096
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # c3-v3 root
R4_DIR = os.path.join(BASE_DIR, "runs-r4")
OUT_DIR = os.path.join(BASE_DIR, "runs-fullloop")

def sha256_16(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

def call_vllm(messages, timeout=300):
    """Call vLLM chat completions API."""
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }
    req = urllib.request.Request(
        VLLM_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
            latency = time.time() - start
            text = data["choices"][0]["message"]["content"]
            return text, latency
    except Exception as e:
        raise RuntimeError(f"vLLM call failed after {time.time()-start:.1f}s: {e}")

def load_component(config, comp_name):
    """Load a component file for a given config."""
    manifest = json.load(open(os.path.join(BASE_DIR, "prompts/MANIFEST.json")))
    ops = manifest.get(config, {}).get("ops", {})
    if ops.get(comp_name) == "keep":
        path = os.path.join(BASE_DIR, "prompts/A-full", f"{comp_name}.md")
        if os.path.exists(path):
            return open(path).read()
    return None

def build_stage_prompt(stage, config, domain, seed, prev_output):
    """Build the prompt for a given stage."""
    seeds = json.load(open(os.path.join(BASE_DIR, "design/seeds/seeds.json")))
    brief = seeds[domain][f"brief_{seed}"]
    
    if stage == "01":
        # Use R4 frozen prompt (byte-exact)
        r4_prompt_path = os.path.join(R4_DIR, config, domain, f"seed{seed}-prompt.txt")
        if os.path.exists(r4_prompt_path):
            return open(r4_prompt_path, encoding="utf-8").read()
        else:
            raise FileNotFoundError(f"R4 prompt not found: {r4_prompt_path}")
    
    elif stage == "02":
        comp = load_component(config, "evidence")
        if comp:
            instruction = comp
        else:
            instruction = """# 阶段 02：资料搜集（无 evidence 组件）
## 操作流程
1. 读取阶段 01 的空缺条件，只围绕这些空缺搜集资料。
2. 使用公开知识和已有信息回答空缺问题。
3. 对每个关键事实标注来源或标记为"待核验假设"。
4. 产出结构化的证据清单。"""
        
        return f"""{instruction}

---

## 输入上下文

**任务**: {brief}

**阶段 01 输出**:
{prev_output}

请基于以上阶段 01 的输出，执行阶段 02 流程，产出完整的阶段 02 工件。"""
    
    elif stage == "03":
        comp = load_component(config, "owner")
        if comp:
            instruction = comp
        else:
            instruction = """# 阶段 03：具体行动分解（无 owner 组件）
## 操作流程
1. 基于阶段 02 的证据，将目标拆成可执行步骤。
2. 每步写输入、动作、依赖、预期产出和验收方式。
3. 标注哪些步骤可以并行。
4. 为关键失败情况写替代路径。"""
        
        return f"""{instruction}

---

## 输入上下文

**任务**: {brief}

**阶段 02 输出**:
{prev_output}

请基于以上阶段 02 的输出，执行阶段 03 流程，产出完整的阶段 03 工件。"""
    
    elif stage == "04":
        return f"""# 阶段 04：最终报告

基于前三个阶段的全部输出，产出最终选型报告。要求：
1. 推荐方案（单一最佳选择，含核心理由）
2. 备选方案（1-2 个，含对比优势/劣势）
3. 淘汰理由（对未入选候选的明确排除依据）
4. 成本明细（年度总成本拆解）
5. 风险与缓解措施

---

## 输入上下文

**任务**: {brief}

**阶段 01 输出**:
{prev_output}

请产出完整的最终选型报告。"""

def run_pipeline(config, domain, seed):
    """Run the full 4-stage pipeline for one cell."""
    out_path = os.path.join(OUT_DIR, config, domain, f"seed{seed}")
    os.makedirs(out_path, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Running: {config} / {domain} / seed{seed}")
    print(f"{'='*60}")
    
    results = {}
    prev_output = ""
    
    for stage in ["01", "02", "03", "04"]:
        stage_md_path = os.path.join(out_path, f"stage{stage}.md")
        stage_json_path = os.path.join(out_path, f"stage{stage}.json")
        
        # Skip if already done
        if os.path.exists(stage_md_path) and os.path.getsize(stage_md_path) > 100:
            print(f"  Stage {stage}: already exists ({os.path.getsize(stage_md_path)} bytes), skipping")
            prev_output = open(stage_md_path).read()
            continue
        
        # Build prompt
        prompt = build_stage_prompt(stage, config, domain, seed, prev_output)
        prompt_sha = sha256_16(prompt)
        
        # Call vLLM
        print(f"  Stage {stage}: calling vLLM (prompt {len(prompt)} chars, sha={prompt_sha})...")
        try:
            output, latency = call_vllm([{"role": "user", "content": prompt}])
        except RuntimeError as e:
            print(f"  Stage {stage}: FAILED - {e}")
            results[stage] = {"error": str(e), "prompt_sha256_16": prompt_sha}
            break
        
        # Save output
        with open(stage_md_path, "w", encoding="utf-8") as f:
            f.write(output)
        
        # Save metadata
        meta = {
            "config": config,
            "domain": domain,
            "seed": seed,
            "stage": stage,
            "prompt_sha256_16": prompt_sha,
            "prompt_chars": len(prompt),
            "output_chars": len(output),
            "latency_s": round(latency, 1),
            "model": MODEL,
            "temperature": TEMPERATURE,
            "finished_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        with open(stage_json_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        
        print(f"  Stage {stage}: done ({len(output)} chars, {latency:.1f}s)")
        results[stage] = meta
        prev_output = output
    
    return results

def main():
    configs = ["B-noevidence", "B-noowner", "B-2del-fe", "B-2del-fo", "B-2del-eo", "B-sham"]
    domains = ["D1-meeting-room", "D2-file-collab"]
    seed = "a"
    
    all_results = {}
    for config in configs:
        for domain in domains:
            key = f"{config}/{domain}/seed{seed}"
            result = run_pipeline(config, domain, seed)
            all_results[key] = result
    
    # Save summary
    summary_path = os.path.join(OUT_DIR, "fullloop-batch1-summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\nSummary saved: {summary_path}")
    print(f"Total cells: {len(all_results)}")

if __name__ == "__main__":
    main()
