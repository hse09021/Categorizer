# 영상처리 기술을 적용한 쓰레기 분리수거 장치

## 목표
쓰레기를 자동으로 구분하고 분류

## 핵심내용
* 사용자가 병 또는 캔을 장치에 하나씩 투입
* 카메라를 이용해 병인지 캔인지 구분
* 장치 내부 도어를 움직여 캔 또는 병 통로를 개폐함
* 쓰레기가 담긴 리프트를 올려 쓰레기를 떨굼


## 중요성
* 분리수거율 증가
* 쓰레기 매립량 감소
* 높아진 재활용률을 통해 자원 낭비를 줄일 수 있음
* 바다로 유출되는 쓰레기 감소


## 서론
### 배경 설명, 사례 분석
쓰레기 배출량은 매년 늘고 있습니다. 특히 2020년 이후부터는 코로나19로 인해 집에 있는 시간이 많아져 **쓰레기 배출량이 크게 증가할 전망**이라고 합니다. 쓰레기 배출량이 늘어난 반면, **쓰레기를 매립 가능 토지가 점점 줄고 있는 추세**입니다.
분리수거가 쉽지 않다 보니, 분리수거 업체에서는 많은 쓰레기를 일일이 구별해내기 어렵다고 **분리수거가 된 채로 보내진 쓰레기들 역시 그대로 폐기**하는 경우가 많습니다.
![image](https://user-images.githubusercontent.com/51695816/145290895-45fe4a67-f1d5-48f0-bfe0-fec91648e510.png)

### 문제 정의
분리수거 업체에서 분리수거가 제대로 이루어지지 않고 있다.

### 극복 방안
영상처리 기술을 통해 쓰레기를 자동으로 분류하여 분리수거율을 높일 수 있을 것입니다.

## 본론
### 시스템 개요
![image](https://user-images.githubusercontent.com/51695816/145291711-1511a55c-406e-4375-b05b-e1e463572cd7.png)

### 필요한 기술 요소
![image](https://user-images.githubusercontent.com/51695816/145291528-dab74700-8839-408c-8f2c-c6468bc2de1c.png)

### 구현 방안 및 개발 방향
본 장치의 작동을 보여주기 위한 시연장치를 제작할 것입니다. 아래와 같은 과정을 통해 구현할 것입니다.
```
* 웹 크롤링을 통해 모델 학습을 위한 데이터셋을 수집
* Teachable Machine을 활용하여 Keras 모델을 구성
* 작동에 필요한 알고리즘을 Python, Open CV(이미지 분석), Tensorflow(머신러닝) 통해 구현
* 시연장치 구조를 Fusion 360으로 모델링하고, 아크릴 레이저 커팅으로 출력 및 제작
* Arduino(MCU)를 이용해 장치 구동부 제어 장치 구현
* 카메라를 이용해 쓰레기 분석부 구현
* 시리얼 통신을 이용해 MCU 제어 알고리즘 구현
* 머신러닝 모델 성능 추가 개선
```
### 시연장치 3D 모델
![image](https://user-images.githubusercontent.com/51695816/145291458-f2ed3b83-dc11-42ad-8d97-65b69699add5.png)
### 시연장치 회로 구조도
![image](https://user-images.githubusercontent.com/51695816/145291489-fe51ef6d-be53-4f7a-969c-7332fd08f6d0.png)

### 시연 영상
아래 사진을 클릭하면 시연 영상이 열립니다.\
[![video](https://img.youtube.com/vi/uG-Ktd_xKt0/0.jpg)](https://www.youtube.com/watch?v=uG-Ktd_xKt0)

## 결론
### 보고 내용 요약
대형 분리수거장에서의 재활용률을 높이기 위해선 분리 배출 기준에 맞게 쓰레기가 분류되어야 합니다. 따라서 본 장치는 미처 제대로 분리되지 않은 재활용 쓰레기를 한번 더 자동으로 분류합니다. 비슷한 사례로는 공원에서 서비스 중인 쓰레기 자동 분류 장치가 있지만, 본 장치는 개인이 아닌 대형 분리수거장에서 분류 자동화에 적용하기 쉬운 구조로 차별점을 두었습니다.

## PPT 자료링크
[[Power Point Download]](https://docs.google.com/presentation/d/1oqMaZnbnSjLDekYm4yTNcLnXJ8hX5mCb/edit?usp=sharing&ouid=108251390155860008883&rtpof=true&sd=true)
