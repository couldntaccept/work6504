# 第一步：下载

pip3 install -U spacy

python3 -m spacy download en_core_web_sm

python3 -m spacy download en_core_web_trf

# 第二步：run

python3 test_with_line_number.py

结果会出现在result.txt里面 

每次跑test_with_line_number.py的时候 记得清空result.txt



# 第三步：读+清理

现在的放在result.py里的形式是：
((line start, token start), (line end, token end)) - label = Line{line number}, [token start, token, label]

等号后面的东西是为了咱们方便阅读+检查

最终提交上去的还是要把每行等号后面的东西去除的