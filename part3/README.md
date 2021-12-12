## Poetry

### poetry란?

가상환경을 계층화해서 관리하는것인듯

### 사용방법

#### poetry init

![image](https://user-images.githubusercontent.com/50165842/145700328-61cd125d-d646-4131-b683-1ef2a738e66b.png)

```
poetry init
```



poetry init을 하게 되면 dependency -> dev 순으로 라이브러리를 지정하게 된다.

역순(dev-> dependency)으로 다시 돌아가는 방법은 없다.

#### poetry add

![image](https://user-images.githubusercontent.com/50165842/145700368-359dc006-3e66-421e-be57-a733b7997c9b.png)

```
poetry add [name]
```

혹시 실수로 까먹거나 , 새로 설치를 해야하는 경우 다시 poetry init을 하지말고 poetry add로 첨부를 한다.



#### poetry.lock

![image](https://user-images.githubusercontent.com/50165842/145700409-1b072304-7b4f-4248-9160-18a1c9e2842f.png)

저 파일이 있으면 프로젝트가 동일한 dependency를 가지고 진행될 수 있다,





#### poetry shell

![image](https://user-images.githubusercontent.com/50165842/145700503-1ad5eea9-cbe3-4293-8d19-a197d32c05ba.png)

기존의 가상환경이 있다면 비활성화를 하고 poetry shell을 활성화해야한다.



![image](https://user-images.githubusercontent.com/50165842/145700523-c98feec9-9e16-4ca6-9c77-85d2bc247acf.png)

activate 하면 이렇게 된다.



#### poetry exit

```
poetry exit
```

poetry exit을 하지 않으면 poetry shell로 다시 새창을 열수가 없다. 



![image](https://user-images.githubusercontent.com/50165842/145700562-a329c869-2660-4698-82a2-9844701d35d6.png)

[Basic usage | Documentation | Poetry - Python dependency management and packaging made easy (python-poetry.org)](https://python-poetry.org/docs/basic-usage/)

위 docs를 참고하면 된다.



