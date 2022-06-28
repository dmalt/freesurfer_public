Docker container with freesurfer build + tools to work with anatomy files.

Based on the official [freesurfer image](https://hub.docker.com/r/freesurfer/freesurfer).

Installed tools
---
- [freesurfer](https://surfer.nmr.mgh.harvard.edu/)
- [mne-python](https://mne.tools/0.23/index.html)
- pydoit
- nibabel
- vtk

Freesurfer license
---
No license included. To add a license, create a new docker image.
From a folder containing `license.txt`, run:
```Dockerfile
FROM dmalt/freesurfer_public:7.1.1
COPY license.txt /usr/local/freesurfer/.license
```
