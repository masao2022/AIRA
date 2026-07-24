# AIRA
AI Robot Assistant

## 概要

AIRAはOllamaを利用したローカルAIアシスタントです。

## 必要環境

- Windows 10 / 11
- Python 3.12以上
- Ollama

## インストール

### 1. ダウンロード

```bash
git clone https://github.com/masao2022/AIRA.git

2. 仮想環境作成
</> PowerShellで
python -m venv .venv

有効化：
</> PowerShellで
.venv\Scripts\activate

3. ライブラリインストール
</> PowerShellで
pip install -r requirements.txt

4. Ollama起動

モデル取得：
ollama pull gemma3:4b

5. AIRA起動
</> PowerShellで
python app.py

使用例
あなた > こんにちは

AIRA > こんにちは！