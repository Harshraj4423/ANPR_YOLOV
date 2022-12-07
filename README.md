# ANPR using YOLOv7

### The goal of our project is to identify a vehicle of interest based on its number plate and mantain record of it's location along with owner's detail. This system can be implemented in public safety domain with law-enforcemnet purposes. Moreover ANPR can be used in advance parking system , tracking vechile speed and identifying  model of vehicle, plus the system can be consider alternative for fastag (which requires some protocols) like speed limit

ANPR automatically reads vehicle registration marks for comparison against database records. The police and government agencies use ANPR as a tactical option to disrupt, prevent and detect criminal activity. ANPR is also used by commercial companies, for example, garages, shopping centres and car parks.

## Inference

On video:
``` shell
python detection.py # change video path in main function 
```

On image(GUI):
``` shell
python app.py
```

<div align="center">
    <a href="./">
        <img src="./figure/gui.png" width="59%"/>
    </a>
</div>

Database in csv file:

<div align="center">
    <a href="./">
        <img src="./figure/record.png" width="59%"/>
    </a>
</div>
 
 

## Install requirements 

``` shell
pip install -r  requirements.txt
```

