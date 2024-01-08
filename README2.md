### Background

- Refractive error comprises three components:
    - Spherical error 
    - cylidrical errror
    - cylindrical axis


- In retinoscopy, the examiner shines a linear streak
- After reflection from the retina, the light travels back through the same
refractive surfaces in reverse order to form another image, which is viewed by the examiner through a peephole and a semi-silvered mirror in the head of the retinoscope


-  The examiner observes four characteristics of the
reflex movement–size, brightness, direction, and speed–and tries to achieve neutralization by adding corrective
lenses. 
- The speed of reflex aids in identifying if the eye is close/far from neutralization


- In this work, we capture retinoscopy videos by moving the vertical streak of the beam along the horizontal meridian of the patient’s eye. The captured video is passed through a video processing pipeline, which estimates the working distance between the patient’s eye and the smartphone, tracks the retinoscopic beam and the position of reflex to output the net refractive error of the eye along the horizontal meridian.


- Most retinoscope devices provide two controls - a streak rotator , vergence sleeve 

- retinoscope attached to the smartphone camera at the peephole

- To collect video data, patients were asked to wear a comfortable size of our paper frame. They were seated on a
chair with their chin placed on an adjustable chin-rest and were instructed to focus on the LogMAR chart placed
at a 3m distance along the eye’s optical axis for relaxing the eye to minimize accommodation


### Working 

- After entering the patient’s demographic information (gender, age) and patient ID on the data collection app, the app prompts the data collector to record the video for the left eye, followed by the right eye. For each eye, the data collector needs
to rotate the retinoscope attached to the smartphone such that the beam moves from one end of the paper frame to the center and back. This is referred to as a pass. This process is repeated to obtain four passes (2 left-to-right
and 2 right-to-left) for a single eye in a video 


- room in dark
- 30cm distance from patient
- more fps vs high res


-  For estimating refractive power, four data points are needed: 
(1) camera parameters,
(2) pixel location of the fiducial centers, 
(3) pixels moved by the retinoscopic beam between timestamps 𝑡1 and 𝑡2, and 
(4) pixels moved by the retinal reflex between timestamps 𝑡1 and 𝑡2.


steps 

1. Image Cropping and Tracking
2. Fiducial Detection
3.  Perspective Correction
4.  Beam Detection
5. Pupil Detection
6. Reflex Edge Localization
7.  Refractive Error Estimation

 net refractive error = spherical + (cylindrical × 𝑠𝑖𝑛(𝑎𝑥𝑖𝑠)^2 ) 