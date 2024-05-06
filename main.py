from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from os import path
from PIL import Image
import matplotlib.pyplot as plt

text = "Samp Suhradbhav Ekta Oneness Brotherhood Teamwork Sports Trust Kindness BAPS bapa Believe Unity Together"

#wordcloud = WordCloud().generate(text)

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()


shape_mask = np.array(Image.open("mask2.png"))
print(shape_mask)

def transform_format(val):
    if val == 1:
        return 255
    else:
        return val

transformed_shape_mask = np.ndarray((shape_mask.shape[0],shape_mask.shape[1]), np.int32)

for i in range(len(wine_mask)):
    transformed_shape_mask[i] = list(map(transform_format, shape_mask[i]))

print(transformed_shape_mask)

wc = WordCloud(background_color="white", mask=transformed_shape_mask, contour_width=3, contour_color='black')


wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
