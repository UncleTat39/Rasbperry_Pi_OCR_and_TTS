使用 Raspberry Pi 5 搭配 Paddle OCR 和 Ekho TTS，构建一个支持粤语、普通话等多种中文方言的朗读系统。

Use Raspberry Pi 5 with Paddle OCR and Ekho TTS to build a read-aloud system that supports Cantonese, Mandarin and other Chinese dialects.


Python version:3.11.2 can run this project. And I use USB camera.


Install Ekho environment for Raspberry Pi:

===== Setup build environment for github code under Ubuntu =====

$ sudo apt install autoconf libtool 

$ cd ekho

$ ./autogen.sh

$ sudo apt install libsndfile1-dev libespeak-ng-dev libpulse-dev texinfo libltdl-dev libmpg123-dev libsonic-dev libutfcpp-dev

$ ./configure

$ make CXXFLAGS=-O0

$ ./ekho 123


Others can follow this link for install Ekho environment: https://github.com/hgneng/ekho/blob/master/INSTALL


Paddle OCR:

$ python -m pip install paddlepaddle==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

$ pip install paddleocr

This is the easiest way to use Paddle OCR.

Others can follow this link: https://paddlepaddle.github.io/PaddleOCR/latest/quick_start.html
