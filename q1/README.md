# Excelから当たりを探せ！

## 説明
* excelsフォルダの中に1000個のファイルがあります。
* この中に当たりがひとつだけあります。どーれだ？

## フォルダ構成
<pre>
.
└── q1
    ├── README.md  # このファイルです
    ├── answer  # 回答を入れるフォルダ
    │   └── answer.py   # 回答例
    ├── excels
    │   ├── 0000.xlsx
    │   ├── 0001.xlsx
    │     ... 全1000ファイル
    ├── make_excel.py
    └── requirements.txt
</pre>


## 回答
* answer/answe.pyを実行します。
* 以下を実行して下さい。
* 答えが出来たらpull requestで回答を送って下さい。

```
cd answer
install openpyxl -t ./site-packages/
python answer.py
```

