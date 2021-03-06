# 3dReconstruction
![alt text](https://3dexport.com/items/2012/08/01/138218/93631/my_little_pony_fluttershy_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_1138912_o.jpg?style=centerme)

# Requirements

## 1. PURPOSE
The goal of this project is to provide mobile application which reconstruct the 3D model of an object from multiple images of it.

## 2. SCOPE
"Application Name" is a mobile application for 3D reconstruction. User should provide multiple images from a different perspective with some object on it. These images will be sent to a server, which will proceed incoming images and will return the 3D model of the particular object.
![alt text](https://raw.githubusercontent.com/daniilBerezhansky/3dReconstruction/master/DFD.png)

## 3. PRODUCT PERSPECTIVE
The mobile application requires Internet connection to send images and receive the 3D model. Reconstruction from images is carried out on a web-server.

  ### 3.1  USER INTERFACES
A first-time user of the mobile application should see the log-in. If the user has not registered, he/she should be able to do that on the log-in page. If the user is not a first-time user, he/she should be able to see a dialog which helps to sent data to the server. If the user has receieved the 3D model or he/she has it from the previous session, the user should be able to open the window through which the user can interact with the 3D model.
* Back-end software: Django
* Photometry software: Python2+


### 3.2. SOFTWARE INTERFACES
| Software used  | Description |
|----------------|-------------|
| Server operating system  | Ubuntu 16.04+  |
|Database|MySQL|

### Flow diagram
![alt text](https://raw.githubusercontent.com/daniilBerezhansky/3dReconstruction/master/image.png)
### Systems Development Life Cycle
![alt text](https://www.pro-technix.com/services/software/images/evolvem.gif)

### Architecture
![alt text](https://raw.githubusercontent.com/daniilBerezhansky/3dReconstruction/master/ARCHITECTURE.png)

Structure from Motion pipeline  - https://github.com/mapillary/OpenSfM
©Nikita_Ignatenko_2019
