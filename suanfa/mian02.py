import easyocr
from PIL import Image

print(easyocr.__version__)
# "en" "ch_sim"
reader = easyocr.Reader(
    ["en", "ch_sim"],
    gpu=True,
)  # this needs to run only once to load the model into memory

# 图像路径
image_path = "./15889317528424945.png"
image_path_out = "./results/15889317528424945.png"
image = Image.open(image_path)
# image = image.resize((800, 600))
# image = image.resize((800, 300))
# image.show()
image.save(image_path_out)
# result = reader.readtext("./image/baidu_image/test5.jpg", detail=0)
results = reader.readtext(image_path_out, detail=0, batch_size=20, paragraph=True)
print("results==", results)

for result in results:
    print("result", result)
