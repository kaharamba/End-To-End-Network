import torch 
import torchvision 
import cv2
import matplotlib.pyplot as plt

import preprocessing 

from torch.utils.data import DataLoader
from torchvision import transforms 
from torchvision.transforms import v2
from nn import End_to_End_NN
from torch import nn
from PIL import Image


EPOCH = 100
transform = transforms.Compose([
    transforms.ToTensor()
]) 

def eval_model(): 
    model = torch.load("/Volumes/joeham/model.pth", weights_only=False) 
    model.eval()  

def is_correct(steering, output, threshold=0.1): 
    correct = torch.abs(steering - output) < threshold
    accuracy = correct.float().mean().item() 
    return accuracy 

def train():
    save_model = input("Save model? (y or n) ") 

    data = preprocessing.data_processing()
    train_dataloader = DataLoader(data, batch_size=1, shuffle=True)

	# Load the Model
    model = End_to_End_NN()
    loss_fn = nn.MSELoss() 
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001) 

    total_loss = 0  
    epoch = 1
    loss_every_epoch = [] 
    correct = 0


    for (front_img, steering) in train_dataloader: 

        if epoch > EPOCH: 
            break

        optimizer.zero_grad()
        output = model(front_img) 

        loss = loss_fn(output, steering) 
        accuracy = is_correct(steering, output)

        if accuracy == 1.0: 
            correct += 1

        loss.backward() 
        optimizer.step()

        loss_every_epoch.append(loss.item()) 
        print("The loss is: " + str(loss.item())) 
        total_loss = 0
        epoch += 1
    
    print("The accuracy is: " + str(correct / epoch))
    plt.plot(loss_every_epoch) 
    plt.xlabel("Iteration") 
    plt.ylabel("Loss") 
    plt.title("Training Loss") 
    plt.show() 

    if save_model == "y": 
        torch.save(model.state_dict(), "/Volumes/joeham/model.pth") 


def main(): 
    train()

if __name__ == '__main__': 
    main()
