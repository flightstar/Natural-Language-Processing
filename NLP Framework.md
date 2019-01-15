[Tokenization](https://en.wikipedia.org/wiki/Tokenization) is a way to split text into tokens. These tokens could be paragraphs, sentences, or individual words. [NLTK](http://www.nltk.org/py-modindex.html) provides a number of [tokenizers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html) in the [tokenize module](https://www.nltk.org/api/nltk.tokenize.html). Some tokenizer in NLP as 

+ TreebankWordTokenizer: Uses regular expressions to tokenize text as in [Penn Treebank](https://web.archive.org/web/20131109202842/http://www.cis.upenn.edu/~treebank/).
  
  ![](https://lh3.googleusercontent.com/Fnhh8TBbab8xubraGlzpy6MzEhbnHVidgEQRZ7HCbKT3TparOsCHOCTp74cbNJhOZ_zK1RMobuMnQQKzhUumDpVl8fFP9Bgpz8Eq3RkmX1Wd_7QL1iEUNjBpHyBQafRyxL1HXxg3M3alm5YYlKxxGjY0vk5q6gNM8IY6cdfNA9g26rtKaTpouvSDls1lp7jTCU1yjBJ6rPMbNo5rmG3Fo5xTO1P3sf2PPbkj5lI5ihzYu3s29Y70FNXwrxp9JaiAOY4wb6XU9r8soJIKwPkn4YmBIUQZ3_aIFj53-AnSmNvdkdbf4PqYKMlmiqLOkmhlwPrdCtVqbXTRphYSdIHlqtgH5m0BSD5UMk1ViFrZCCFzmISeCyiQC4xUStNQfxX8axXssXeLljLApPBaus4DZwvj6Ul0Fkezx_Ct6Iu7XSBYjQV_NCPjqP2W5bBLJT6bICGUDT0B148D1ZD4FTGOgiBaipHJ5BmV1-Tua5bpZquB5uNaTBM5J1m-xpBHfe11lLx__6KQGiLD9yledxIw8UGLUFSh9DCF4iysPhT5AYcIV0TM5mrnbvKqXdVRd2mWeQeg0PFe3NlyfimXw96Wz-J72CTOmWuOpcgeIkdfuBJWUnybzSI5I1xnPEwJaWARiTWZhYUL7mlqNuddMzp1-zke3ISCf-vVjiojqpIaxYhr8lqzPlRIug3_Kng4cW4lyPYKEmHuugmjjw6npQ=w796-h525-no)
  
  Bảng chú giải tree bank:
  
  Name | description
  -----|------------
  N | Danh từ  
  Np| Danh từ riêng 
  Nc| Danh từ chỉ loại 
  Nu| Danh từ đơn vị 
  V | Động từ 
  A | Tính từ 
  P | Đại từ 
  L | Định từ 
  M | Số từ 
  R | Phụ từ 
  E | Giới từ 
  C | Liên từ 
  I | Thán từ 
  T | Trợ từ, tiểu từ, từ tình thái 
  U | Từ đơn lẻ 
  Y | Từ viết tắt 
  X | Các từ không phân loại được 
  NP (noun phrases)| Cụm danh từ  
  VP (verb phrases)| Cụm động từ  
  AP (adjective phrases)| Cụm tính từ  
  RP | Cụm phụ từ  
  PP | Cụm giới từ  
  QP | Cụm từ chỉ số lượng  
  MDP (model phrases)| Cụm từ tình thái  
  WHNP (wh-question noun phrases)| Cụm danh từ nghi vấn (ai, cái gì, con gì,...)  
  WHAP (wh-question adjective phrases)| Cụm tính từ nghi vấn (lạnh thế nào, đẹp ra sao,...)  
  WHRP | Cụm từ nghi vấn dùng khi hỏi về thời gian, nơi chốn,...  
  WHPP (wh-question preposition phrases)| Cụm giới từ nghi vấn (với ai, bằng cách nào,...) 
  S | Câu trần thuật (khẳng định hoặc phủ định)  
  SQ | Câu hỏi  
  SBAR | Mệnh đề phụ (bổ nghĩa cho danh từ, động từ, và tính từ) 
  SUB | Nhãn chức năng chủ ngữ 
  DOB | Nhãn chức năng tân ngữ trực tiếp 
  IOB | Nhãn chức năng tân ngữ gián tiếp
  TPC | Nhãn chức năng chủ đề
  PRD | Nhãn chức năng vị ngữ không phải cụm động từ 
  LGS | Nhãn chức năng chủ ngữ logic của câu ở thể bị động 
  EXT | Nhãn chức năng bổ ngữ chỉ phạm vi hay tần suất của hành động  
  H | Nhãn phần tử trung tâm (của cụm từ hoặc mệnh đề) 
  TC, CMD, EXC, SPL | Nhãn phân loại câu: đề-thuyết, mệnh lệnh, cảm thán, đặc biệt 
  TTL | Tít báo hay tiêu đề 
  VOC | Thành phần than gọi 
  TMP | Nhãn chức năng trạng ngữ chỉ thời gian
  LOC | Nhãn chức năng trạng ngữ chỉ nơi chốn 
  DIR | Nhãn chức năng trạng ngữ chỉ hướng 
  MNR | Nhãn chức năng trạng ngữ chỉ cách thức 
  PRP | Nhãn chức năng trạng ngữ chỉ mục đích hay lý do 
  ADV | Nhãn chức năng trạng ngữ nói chung (dùng khi trạng ngữ không thuộc một trong các loại cụ thể trên)
  
+ WordPunctTokenizer: Tokenize a text into a sequence of alphabetic and non-alphabetic characters, **using the regexp \w+|[^\w\s]+.**
+ PunctWordTokenizer: This tokenizer divides a text into a list of sentences by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences.  It must be trained on a large collection of plaintext in the target language before it can be used.

+ WhitespaceTokenizer: Tokenize a string on whitespace (space, tab, newline). In general, users should use the string split() method instead.

I show the most popular neural network frameworks and libraries that can be utilized for natural language processing (NLP) in the Python programming language.

+ [Parsing in English](https://www.clips.uantwerpen.be/pages/pattern-en) 
+ [Parsing in Dutch](https://www.clips.uantwerpen.be/pages/pattern-nl)
+ [Parsing in French](https://www.clips.uantwerpen.be/pages/pattern-fr)
+ [Parsing in Spanish](https://www.clips.uantwerpen.be/pages/pattern-es) 
+ [Parsing in Italian](https://www.clips.uantwerpen.be/pages/pattern-it)

