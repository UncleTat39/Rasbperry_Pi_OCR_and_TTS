from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np
import subprocess  # 用于调用 ekho 命令行工具

# 初始化 PaddleOCR
ocr = PaddleOCR(
    det_model_dir='./models/Multilingual_PP-OCRv3_det_infer/',
    rec_model_dir='./models/Multilingual_PP-OCRv3_rec_infer/',
    cls_model_dir='./models/ch_ppocr_mobile_v2.0_cls_slim_infer/',
    use_angle_cls=True,
    det_limit_side_len=320,
    lang='ch'
)

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头！")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取视频帧！")
        break

    # 将帧转换为 RGB 格式
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        # 进行 OCR 识别
        result = ocr.ocr(frame_rgb, cls=True)
        
        # 检查是否检测到文本
        if result and isinstance(result, list) and len(result) > 0 and result[0]:
            boxes = []
            txts = []
            scores = []
            
            # 提取检测结果
            for line in result[0]:
                boxes.append(line[0])
                txts.append(line[1][0])
                scores.append(line[1][1])

            # 绘制结果
            im_show = draw_ocr(frame_rgb, boxes, txts, scores, 
                             font_path='OCR/fonts/chinese_cht.ttf')
            im_show = cv2.cvtColor(np.array(im_show), cv2.COLOR_RGB2BGR)

            # 显示结果
            cv2.imshow("OCR Result", im_show)

            # 输出识别结果并用 ekho 播报（粤语）
            for text, score in zip(txts, scores):
                print(f"识别结果: {text} (置信度: {score})")
                
                # 调用 ekho 进行粤语语音合成
                subprocess.run(["ekho", "-v", "Cantonese", text])
                
        else:
            # 如果没有检测到文本，显示原始帧
            cv2.imshow("OCR Result", frame)

    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")
        cv2.imshow("OCR Result", frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()