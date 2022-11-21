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
- ΔCE = CE<sup>host</sup> - CE<sup>dopant</sup>
- CE<sup>i</sup> = bulk cohesive energy of monometallic material (eV)
- CN = coordination number of the slab (number of neighboring atoms)

### ΔBE / CN_adsorbate
- ΔBE = BE<sup>host</sup> - BE<sup>dopant</sup>
- Binding energy of an adsorbate on a single atom (5 to 7 atom system)
- CN_ads is the coorindation number of the adsorbate on the metal surface. 

### ΔWS
- ΔWS = WS<sup>host</sup> - WS<sup>dopant</sup>
- WS= Wigner seitz (au)

### ΔEA
- ΔEA = EA<sup>host</sup> - EA<sup>dopant</sup>
- EA = electron affinity (eV)





