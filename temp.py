import glob
a = 'C:\\Users\\parks\\Desktop\\carplate_detect\\easy_ocr\\saved_models\\TPS-VGG-BiLSTM-CTC-Seed1111\\best_accuracy.pth'
save_path = glob.glob('\\'.join(a.split('\\')[:-1]) +"\\*.pth")