## Problem Statement
Refractive error is one of the most common problems seen in general OPD. To find the accurate refraction and to prescribe glasses, one of the most important investigations is retinoscopy. Hence, to find the state of refraction, a standard technique using one arm distance (approximately 66 cm) is typically employed. However, arm length may vary from individual to individual, and there is a tendency to move further forward or backward while performing the retinoscopy procedure. Although this might seem like a simple problem, the change in distance can alter refraction values, leading to incorrect prescriptions.

## Project Overview
In response to this challenge, our project aims to implement the findings of the Microsoft AutoRetinoscopy paper, offering a practical and user-friendly solution. We have developed a simple UI integrated with a Flask-based application, leveraging the power of OpenCV for video processing.



### Demo Video

https://github.com/thisismrsanjay/auto-retinoscope/assets/37665041/e8b4167d-3d7e-4a6e-9a38-bbff368929c3




### Key Features
- Utilizes OpenCV for accurate video analysis.
- A Flask application for efficient data collection and processing.
- Input fields for patient information including age, sex, and hospital-assigned patient ID.
- Options for recording and recapturing videos for both eyes.
- Functionality to input refractive error measurements from autorefractor, retinoscopy, and subjective refraction methods.
- Storage of a comprehensive metadata file for each patient, including details like age, name, email, etc.



## How It Works
The application streamlines the process of retinoscopy by enabling data collectors to accurately capture and record patient information and videos. Here’s a step-by-step guide on how the application works:

1. **Data Entry**: For each patient, the data collector enters essential details such as age, sex, and patient ID.
2. **Eye Drops Selection**: If cycloplegic refraction is performed, the type of eye drops used can be selected, assisting the algorithm in compensating for accommodation effects.
3. **Video Recording**: The app facilitates video recording/ uploading video for each eye, with options to recapture or proceed to the next step.
4. **Refractive Error Input**: After recording, the data collector can input the refractive error measurements obtained.

