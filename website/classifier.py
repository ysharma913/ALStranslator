from PIL import Image, ImageOps
def classify(filepath):
    img = Image.open(filepath)
    width, height = img.size   # Get dimensions
    new_width = 300
    new_height = 300

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    img = img.crop((left, top, right, bottom))
    im_small = img.resize((28, 28))
    im_grey = im_small.convert('L')
    from torchvision import transforms
    from torch import FloatTensor
    import torch.nn.functional as F
    transform = transforms.Compose([transforms.PILToTensor()])
    im_tensor = transform(im_grey).type(FloatTensor).unsqueeze(0)
    mean: float =0.485 * 255
    std: float =0.229 * 255
    transform = transforms.Normalize(mean = [mean], std = [std])
    im_tensor = 0.9 - ((im_tensor) / 255)
    transform = transforms.Compose([transforms.ToPILImage()])
    img = transform(im_tensor.reshape(1,28,28))
    import onnx
    import onnxruntime as ort

    import torch.nn as nn



    fname = "asl_model.onnx"
    # check exported model
    model = onnx.load(fname)
    onnx.checker.check_model(model)  # check model is well-formed

    # create runnable session with exported model
    ort_session = ort.InferenceSession(fname)
    net = lambda inp: ort_session.run(None, {'input': inp.data.numpy()})[0]

    sig = nn.Sigmoid()
    labels = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return labels[net(im_tensor).argmax()]



