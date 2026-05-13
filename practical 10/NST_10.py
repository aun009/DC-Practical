import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torchvision.models import vgg19, VGG19_Weights
from PIL import Image
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load Image
def load_img(path, size=256):
    img = Image.open(path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    return transform(img).unsqueeze(0).to(device)

content = load_img("content.jpg")
style = load_img("style.jpg")

# VGG Model (UPDATED)
vgg = vgg19(weights=VGG19_Weights.DEFAULT).features.to(device).eval()

# Layers
content_layer = '21'
style_layers = ['0', '5', '10', '19', '28']

# Gram Matrix
def gram_matrix(t):
    b, c, h, w = t.size()
    t = t.view(c, h * w)
    return torch.mm(t, t.t())

# Extract Features
def get_features(x):
    features = {}
    for name, layer in vgg._modules.items():
        x = layer(x)
        if name == content_layer:
            features['content'] = x
        if name in style_layers:
            features[name] = x
    return features

# FIXED TARGET FEATURES (IMPORTANT)
content_features = {k: v.detach() for k, v in get_features(content).items()}
style_features = {k: v.detach() for k, v in get_features(style).items()}
style_grams = {l: gram_matrix(style_features[l]).detach() for l in style_layers}

# Output Image
target = content.clone().requires_grad_(True).to(device)
optimizer = optim.Adam([target], lr=0.003)

# Training
for i in range(200):
    target_features = get_features(target)
    
    # Content Loss
    c_loss = torch.mean((target_features['content'] - content_features['content'])**2)
    
    # Style Loss
    s_loss = 0
    for l in style_layers:
        t_gram = gram_matrix(target_features[l])
        s_gram = style_grams[l]
        s_loss += torch.mean((t_gram - s_gram)**2)
        
    # Total Loss
    loss = c_loss + 1e6 * s_loss
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Keep image values valid
    target.data.clamp_(0, 1)
    
    if i % 50 == 0:
        print(f"Step {i}, Loss: {loss.item():.2f}")

# Show Output
img = target.detach().cpu().squeeze().permute(1, 2, 0).numpy()
plt.imshow(img)
plt.title("Stylized Image")
plt.axis("off")
plt.show()

# Save Output Image (NEW)
output_img = Image.fromarray((img * 255).astype('uint8'))
output_img.save("output.jpg")
print("Output saved as output.jpg")
