# website-essencias


## Installation
---
`$ conda create --name website-essencias-dev`

`$ conda activate website-essencias-dev`

`$ pip install Django==2.2.5`

`$ pip install django-pwa`

`$ pip install corsheaders`

`$ python manage.py migrate`

## Starting the backend server
---

`$ cd /home/longlife/repositories/website-essencias/website_essencias_pwa`

`$ conda activate website-essencias-prod`

`# estes provavelmente nao sao precisos, só se houver algum problema com o certificado
$ export CATALOGO_KEY_FILE='/home/longlife/ssl/keys/c3c27_b0623_8585bb95d2c6f170c06cb248bc6fae54.key'`

`$ export CATALOGO_CERT_FILE='/home/longlife/ssl/certs/essenciasdeportugal_pt_c3c27_b0623_1611403200_a5ec7c83fc41caa5ba1fac428f90cafd.crt'`

`$ python manage.py runserver_plus --cert-file $CATALOGO_CERT_FILE --key-file $CATALOGO_KEY_FILE`




