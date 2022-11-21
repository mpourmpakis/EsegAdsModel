# EsegAdsModel
Segregation Energy Model In the Presence of Adsorbate Model for Single Atom Alloys (SAA)
Incorporates Three Different Adsorbates (R-NH2, R-NH, and R-S) 


## Predicts Eseg in the Presence of an Adsorbate

```python
from model_ads_eseg import eseg_ads_model
model = eseg_ads_model()
predicted_eseg = model.predict(X)
```

## Features

Eseg Ads Model utilizes 4 features, 3 of which are tabulated:

### ΔCE / CN
- ΔCE = CE<sub>host</sub> - CE<sub>dopant</sub>
- CE<sub>i</sub> = bulk cohesive energy of monometallic material (eV)
- CN = coordination number of the slab (number of neighboring atoms)

### ΔBE / CN<sub>adsorbate</sub>
- ΔBE = BE<sub>host</sub> - BE<sub>dopant</sub>
- Binding energy of an adsorbate on a single atom (5 to 7 atom system)
- CN<sub>ads</sub> is the coorindation number of the adsorbate on the metal surface. 

### ΔWS
- ΔWS = WS<sub>host</sub> - WS<sub>dopant</sub>
- WS= Wigner seitz (au)

### ΔEA
- ΔEA = EA<sub>host</sub> - EA<sub>dopant</sub>
- EA = electron affinity (eV)





