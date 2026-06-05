import gradio as gr

from attacks.jailbreak import jailbreak_attack
from attacks.prompt_injection import prompt_injection
from defense.sanitizer import sanitize
from defense.output_filter import filter_output
from models.mock_model import generate
from evaluator.safety_score import compute_score


def run_pipeline(prompt):

    # 1. 攻击生成
    jailbreaks = jailbreak_attack(prompt)
    injected = prompt_injection(prompt)

    # 2. 防御处理
    clean_prompt = sanitize(prompt)

    # 3. 模型输出
    raw_output = generate(clean_prompt)

    # 4. 输出过滤
    filtered_output = filter_output(raw_output)

    # 5. 安全评分
    score = compute_score(prompt, filtered_output)

    return {
        "original_prompt": prompt,
        "jailbreak_samples": jailbreaks,
        "injected_prompt": injected,
        "model_output": raw_output,
        "filtered_output": filtered_output,
        "safety_score": score
    }


ui = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Textbox(lines=4, label="Input Prompt"),
    outputs=gr.JSON(label="Security Analysis Report"),
    title="🔐 AIShield-Lab",
    description="LLM Jailbreak Attack & Defense Evaluation System"
)

if __name__ == "__main__":
    ui.launch()
