##Performance matrix

|Sum (n)| Macbook Pro | Raspberry Pi 3
|---:|---|---
|    1,000 |0.0002483749995008111|0.001810290999856079
|  10,000 |0.002767578000202775|0.018751290001091547
|  100,000 |0.027524688048288226|0.1898588660005771
| 1,000,000 |0.27050671295728534|1.9154432000013912
|10,000,000 |2.7073497190140188|19.21548801999961

It looks like my MBP runs integer computations in python about 7 times as fast as the RPi 3.

|101 byte lines written| Macbook Pro | Raspberry Pi 3
|---:|---|---
|    1,000 |0.0.00718|0.00226
|  10,000 |0.0489|0.0118
|  100,000 |0.463|0.152
| 1,000,000 |5.47|1.13

Writing to disk is only about 4 times as fast



rMBP (Mid 2012) 
running El Capitan 10.11.3
2.6 GHz Intel Cor i7 
8 GB 1600 Mhz DDR3 
