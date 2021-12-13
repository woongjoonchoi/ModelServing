보통 머신러닝을 web으로 배포를 한다고 한다면 자주 쓰는 프레임워크는 Flask,Django ,FastAPI입니다. 이 3개의 framework는 scratch 부터 custmoize해서 web application을 배포할 수 있게 해주는 프레임워크 입니다. 하지만, 오늘 제가 소개할것은 streamlit입니다. streamlit은 interactive 한 web service framework입니다. 실제로 ,production을 한다면 flask,Django,FastAPI가 더 나을 수 있습니다. 하지만, 단순히 demo 배포를 위하거나 혹은 prototype을 만들기 위함이라면 streamlit은 좋은 선택지가 될 수 있다고 생각합니다. 
![image](https://user-images.githubusercontent.com/50165842/145832769-33091740-76ce-48b5-b4b1-26c47bd5f8af.png)
https://streamlit.io/
## QA 데모 in streamlit
보통 유튜브에는 Flask를 이용한 nlp, image classification 튜토리얼들이 많이 있습니다. BoostCamp AI tech 2기 강의에서도 여러 mask classification task를 배포하는 task를 했습니다. 
저는 여기서 더 나아가서 Streamlit으로 QA데모를 진행 해보았습니다. final project에서 ODQA 시스템을 구축할 것이기 때문에 어떻게 resource를 주고 받는지에 대한 감을 잡을 수 있을거 같아서 QA task를 진행했습니다.





### cache

```python
@st.cache() 
def 


  return
```
위와 같은 코드로 hf의 pipeline을 caching을 하려고 하면 오류가 발생합니다. 필자는 streamlit의 hash func의 기능에 대해 자세히 알아야만 할 수 있다고 생각했습니다. 따라서, 우선 필자는 모델만 cache하고 나머지 , tokenizer등등의 부품들은 prediction 과정에서 loading하였 습니다. 그리고 , 추후 docs를 통해서 어떻게 하는지 자세히 알아볼려고 했습니다. 
필자는 이를  멘토링 시간에 이를 수행하실려는 멘토분의 tutorial 같은 office hour에 참석했습니다. 여기서 , 
``` python
@st.cache(allow_output_mutation=False) 
def 


  return
```
위 와 같이 코드를 작성하게 되면 된다고 합니다. tokenizer가 매번 mutation 되기 때문에 그걸 무시하기 위해 저런 argument를 넘겨줬다고 하는데 ,  좀 더 docs를 읽고 hf의 tokenizer의 대해서 알아봐야 될거 같습니다. 자세히 알게되면 추후 다시 자세히 적도록 하겠습니다.

### 데모

![12-12-23-41](https://user-images.githubusercontent.com/50165842/145717023-6e692dfb-58b9-4920-af91-0e9994f72444.gif)


데모는 위와 같이 구성을 해보앗습니다.
궁금해 라는 입력칸을 만든 이유는 너무 초라해서 사람들이 궁금해라고 입력을 하는동안 model loading 시간이 다 지나가도록 하기 위하여 일부러 넣어놨습니다. 
중간에 vscode의 화면이 나오는데  텍스트 가 기억이 안나서 일일이 복사해서 데모를 진행하였습니다. 

### 실행방법

```
streamlit run app.py --server.address=127.0.0.1
```

part2 디렉토리에 가서 위의 코드를 통해 실행하면 됩니다. 뒤의 server 지정은 local server에서 열겠다는 arguement 입니다





### Model

[wjc123/qa_finetuned · Hugging Face](https://huggingface.co/wjc123/qa_finetuned)
hub를 통해 모델을 관리하였습니다. 이렇게 하면 좀 더 팀원들 간의 협업이 효율적으로 진행될 수 있습니다.

### 함수설명

나중에 !~
