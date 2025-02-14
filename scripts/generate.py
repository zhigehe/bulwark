import os
import json
import re
import hashlib
from datetime import datetime
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from markdownify import markdownify as md
import shutil  # Add this import at the top of the file


def clone_repo():
    if not os.path.exists("news"):
        os.system("git clone --depth 1 --branch main https://github.com/genkin-he/news")

def create_summary(text, language="en"):
    """Generate a summary of the text using LexRank"""
    text = text.strip()
    # Remove HTML tags, css, javascript
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text)
    text = re.sub(r"<script[^>]*>.*?</script>", "", text)
    if not text:
        return ""

    # If text is short enough, return as is
    if "zh" in language:
        if len(text) < 80:
            return text
    else:
        if len(text.split()) < 50:
            return text

    # Initialize LexRank summarizer
    summarizer = LexRankSummarizer()

    try:
        # Create parser and tokenizer
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        # Get summary (1 sentence)
        summary = summarizer(parser.document, 1)
        return str(summary[0]) + "..."
    except:
        # Fallback to first 50 words if summarization fails
        if "zh" in language:
            return text[:50] + "..."
        else:
            return " ".join(text.split()[:50]) + "..."


def process_json_file(json_file, output_dir, folder):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    items = data.get("data", {})

    for item in items:
        kind = item.get("kind", 1)
        kind_name = "news"
        if kind == 2:
            continue

        # Determine filename
        file_id = item.get("id", "")
        title = item.get("title", "")
        language = item.get("language", "")
        if not language:
            continue
        filename = f"{file_id}.{language}" if file_id else f"{hashlib.md5((title + item.get("pub_date", "")).encode('utf-8')).hexdigest()}{'.' + language}"

        # Sanitize filename
        filename = re.sub(r'[\\/*?:"<>|]', "", filename) + ".md"
        
        # 直接按语言分类
        lang_dir = os.path.join(output_dir, language, kind_name, folder)
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
        filepath = os.path.join(lang_dir, filename)
        print(filepath)

        if os.path.exists(filepath):
            continue

        # Prepare content
        pub_date = item.get("pub_date", "")
        description = item.get("description", "")
        description_d = create_summary(description, language)

        # Convert HTML to Markdown
        try:
            description_md = md(description).strip()
        except:
            # If conversion fails, use the original description
            description_md = description.strip()

        original_link = f"[{item.get('source', '')}]({item.get('link', '')})"

        # Escape special characters in YAML values
        def escape_yaml(value):
            if not value:
                return ""
            # Escape double quotes and backslashes
            value = str(value).replace("\\", "\\\\").replace('"', '\\"')
            # Remove newlines and other special characters that could break YAML
            value = re.sub(r"[\n\r\t]", " ", value)
            return value.strip()

        # Prepare YAML values
        title = escape_yaml(item.get("title", ""))
        pub_date = escape_yaml(pub_date)
        description_d = escape_yaml(description_d)
        source = escape_yaml(item.get("source", ""))
        language = escape_yaml(language)
        image = escape_yaml(item.get("image", ""))

        # Generate YAML front matter
        content = f"""---
title: "{title}"
date: "{pub_date}"
summary: "{description_d}"
categories:
  - "{source}"
lang:
  - "{language}"
translations:
  - "{language}"
tags:
  - "{source}"
menu: ""
thumbnail: "{image}"
lead: ""
comments: false
authorbox: false
pager: true
toc: false
mathjax: false
sidebar: "right"
widgets:
  - "search"
  - "recent"
  - "taglist"
---

{description_md}

{original_link}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


def main():
    clone_repo()

    data_dir = os.path.join("news", "news", "data")
    # 修改基础内容目录
    content_dir = "content"

    if not os.path.exists(data_dir):
        print(f"Data directory not found: {data_dir}")
        return

    try:
        for folder in os.listdir(data_dir):
            print(f"Processing folder: {folder}")
            # 忽略部分文件夹
            if folder in ["yahoo", "bloomberg", "capitoltrades"]:
                continue

            folder_path = os.path.join(data_dir, folder)
            if not os.path.isdir(folder_path):
                continue

            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".json"):
                        process_json_file(os.path.join(root, file), content_dir, folder)
    finally:
        # Clean up the cloned repository
        if os.path.exists("news"):
            print("Cleaning up cloned repository...")
            shutil.rmtree('news')


if __name__ == "__main__":
    main()
